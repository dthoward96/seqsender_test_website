
# Python Libraries
import pathlib
import sys
from zipfile import ZipFile
import ftplib
import os
import json
import subprocess
import pandas as pd
import shutil
import platform
from urllib.request import urlopen
import gzip
import stat
import requests
import time
import xmltodict
import xml.etree.ElementTree as ET
from io import BytesIO
from typing import List, Dict, Any

# Local imports
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import create
import process
import report
import seqsender
import submit

# Get program directory
PROG_DIR: str = os.path.dirname(os.path.abspath(__file__))
# BioSample atribute html prefix
BIOSAMPLE_HTML_PREFIX: str = "https://www.ncbi.nlm.nih.gov/biosample/docs/packages"
# BioSample atribute html suffix
BIOSAMPLE_HTML_SUFFIX: str = "/?format=xml"
# Schema file header
SCHEMA_HEADER: str = """from pandera import DataFrameSchema, Column, Check, Index, MultiIndex

schema = DataFrameSchema(
	columns={"""

# Create example templates for testing
def create_zip_template(organism: str, database: List[str], submission_dir: str, submission_name: str) -> None:
	# Create output directory
	submission_dir = os.path.abspath(submission_dir)
	out_dir = os.path.join(submission_dir, submission_name)
	os.makedirs(out_dir, exist_ok = True)
	# Create sra directory
	out_sra_dir = os.path.join(out_dir, "raw_reads")
	# Create a list of files to output
	out_metadata_file = os.path.join(out_dir, "metadata.csv")
	out_config_file = os.path.join(out_dir, "config.yaml")
	out_sequence_file = os.path.join(out_dir, "sequence.fasta")
	out_fastq_1_r1_file = os.path.join(out_sra_dir, "fastq_1_R1.fastq.gz")
	out_fastq_1_r2_file = os.path.join(out_sra_dir, "fastq_1_R2.fastq.gz")
	out_fastq_2_r1_file = os.path.join(out_sra_dir, "fastq_2_R1.fastq.gz")
	out_fastq_2_r2_file = os.path.join(out_sra_dir, "fastq_2_R2.fastq.gz")
	# Create a list of template files to output
	temp_config_file = os.path.join(PROG_DIR, "template", organism, organism.lower()+"_config.yaml")
	temp_sequence_file = os.path.join(PROG_DIR, "template", organism, organism.lower()+"_sequence.fasta")
	temp_fastq_1_r1_file = os.path.join(PROG_DIR, "template", organism, organism.lower()+"_fastq_1_R1.fastq.gz")
	temp_fastq_1_r2_file = os.path.join(PROG_DIR, "template", organism, organism.lower()+"_fastq_1_R2.fastq.gz")
	temp_fastq_2_r1_file = os.path.join(PROG_DIR, "template", organism, organism.lower()+"_fastq_2_R1.fastq.gz")
	temp_fastq_2_r2_file = os.path.join(PROG_DIR, "template", organism, organism.lower()+"_fastq_2_R2.fastq.gz")
	# Print generating message
	print("\n"+"Generating submission template", file=sys.stdout)
	# Get combined metadata for all given databases
	for i in range(len(database)):
		df = pd.read_csv(os.path.join(PROG_DIR, "template", organism, organism.lower()+"_"+database[i].lower()+"_metadata.csv"), header = 0, dtype = str, engine = "python", encoding="utf-8", index_col=False, na_filter=False)
		if i == 0:
			combined_metadata = df
		else:
			combined_metadata = pd.merge(combined_metadata, df, how='left')
	# Write metadata to output directory
	combined_metadata.to_csv(out_metadata_file, index = False)
    # Write config file to output directory
	shutil.copy(temp_config_file, out_config_file)
    # Write fasta file to output directory
	if any([x in ["GENBANK", "GISAID"] for x in database]):
		shutil.copy(temp_sequence_file, out_sequence_file)
    # Write raw reads file to output directory
	if "SRA" in database:
		os.makedirs(out_sra_dir, exist_ok = True)
		shutil.copy(temp_fastq_1_r1_file, out_fastq_1_r1_file)
		shutil.copy(temp_fastq_1_r2_file, out_fastq_1_r2_file)
		shutil.copy(temp_fastq_2_r1_file, out_fastq_2_r1_file)
		shutil.copy(temp_fastq_2_r2_file, out_fastq_2_r2_file)
	print("Files are stored at: "+os.path.join(out_dir), file=sys.stdout)

def download_table2asn(table2asn_dir: str) -> None:
	# Determine which platform to download table2asn
	if platform.system() == "Windows":
		zip_url = "https://ftp.ncbi.nlm.nih.gov/asn1-converters/by_program/table2asn/win64.table2asn.zip"
		with urlopen(zip_url) as zip_response:
			with ZipFile(BytesIO(zip_response.read())) as zip_file:
				zip_file.extractall(table2asn_dir)
		return
	elif platform.system() == "Darwin":
		zip_url = "https://ftp.ncbi.nlm.nih.gov/asn1-converters/by_program/table2asn/mac.table2asn.gz"
	elif platform.system() == "Linux":
		zip_url = "https://ftp.ncbi.nlm.nih.gov/asn1-converters/by_program/table2asn/linux64.table2asn.gz"
	else:
		print("Error: Cannot identify correct system platform. Please download correct Table2asn version for system and place it in script directory.", file=sys.stderr)
		sys.exit(1)
	# Extract table2asn to tmp folder
	try:
		with open(table2asn_dir, "wb") as file:
			with urlopen(zip_url) as zip_response:
				file.write(gzip.decompress(zip_response.read()))
		st = os.stat(table2asn_dir)
		os.chmod(table2asn_dir, st.st_mode | stat.S_IXOTH | stat.S_IRWXU)
	except Exception as error:
		print("Downloading table2asn error", file=sys.stderr)
		print(error, file=sys.stderr)
		sys.exit(1)

# Download xml and write to a file
def download_xml(xml_url: str, output_file: str) -> None:
	r = requests.get(xml_url)
	r.encoding = "UTF-8"
	with open(output_file, "w+") as file:
		file.write(r.text.replace("\xa0", " "))

# Download list of BioSample packages then download the xml for each package
def download_biosample_xml_list() -> None:
	# Download list of all packages
	download_xml(xml_url = (BIOSAMPLE_HTML_PREFIX + BIOSAMPLE_HTML_SUFFIX), output_file = os.path.join(PROG_DIR, "config", "biosample", "biosample_package_list.xml"))
	with open(os.path.join(PROG_DIR, "config", "biosample", "biosample_package_list.xml")) as file:
		line = file.readline()
		i = 0
		while line:
			if "<Name>" in line:
				name = line.replace("<Name>","").replace("</Name>","").strip()
				# Skip hidden template xml on NCBI website
				if "Generic.1.0" in name:
					line = file.readline()
					continue
				print("Downloading Package: " + name)
				try:
					download_xml(xml_url = (BIOSAMPLE_HTML_PREFIX + "/" + name + BIOSAMPLE_HTML_SUFFIX), output_file = os.path.join(PROG_DIR, "config", "biosample", (name + ".xml")))
				except Exception as error:
					print("Error: BioSample package " + name + " failed to download.", file=sys.stderr)
					print(error, file=sys.stderr)
				try:
					biosample_package_to_pandera_schema(os.path.join(PROG_DIR, "config", "biosample", (name + ".xml")), name)
				except Exception as error:
					print("Error: BioSample package " + name + " failed to convert to schema.", file=sys.stderr)
					print(error, file=sys.stderr)
				time.sleep(5)
			line = file.readline()

# Convert downloaded BioSample package xml to Pandera Schema
def biosample_package_to_pandera_schema(xml_file: str, name: str) -> None:
	tree = ET.parse(xml_file)
	root = tree.getroot()
	xmlstr = ET.tostring(root, encoding='utf-8', method='xml')
	# Convert xml to dictionary
	report_dict = xmltodict.parse(xmlstr)
	indentation = "\n\t\t"
	mandatory_group: Dict[str, Any] = dict()
	with open(os.path.join(PROG_DIR, "config", "biosample", (name.replace(".", "_") + ".py")), "w+") as file:
		file.writelines(SCHEMA_HEADER)
		for attribute in report_dict["BioSamplePackages"]["Package"]["Attribute"]:
			# If attribute in reserved words skip
			if attribute["HarmonizedName"] in ["collection_date"]:
				continue
			# NCBI canonical field name for submission
			file.write(indentation + "\"bs-" + attribute["HarmonizedName"] + "\": Column(")
			# Pandas datatypes
			indentation += "\t"
			file.write(indentation + "dtype=\"object\",")
			# Validation requirements
			if "Format" in attribute:
				if "@type" in attribute["Format"] and attribute["Format"]["@type"] == "select":
					# For columns with only certain valid values
					valid_values = attribute["Format"]["Description"].strip().split(" | ")
					file.write(indentation + "checks=Check.str_matches(r\"(?i)(\W|^)(" + ("|".join(valid_values)) + ")(\W|$)\"),")
				else:
					file.write(indentation + "checks=None,")
			else:
				file.write(indentation + "checks=None,")
			# Null fields allowed
			if attribute["@use"] == "mandatory":
				file.write(indentation + "nullable=False,")
			else:
				file.write(indentation + "nullable=True,")
			# Every field must be unique
			file.write(indentation + "unique=False,")
			# Coerce column into specified dtype
			file.write(indentation + "coerce=False,")
			# Column is required for submission
			if attribute["@use"] == "mandatory":
				file.write(indentation + "required=True,")
			elif attribute["@use"] == "either_one_mandatory":
				# Collect columns that are required but have different column options
				if attribute["@group_name"] in mandatory_group:
					mandatory_group[attribute["@group_name"]] = mandatory_group[attribute["@group_name"]] + " & df[\"bs-" + attribute["HarmonizedName"] + "\"].isnull()"
				else:
					mandatory_group[attribute["@group_name"]] = "df[\"bs-" + attribute["HarmonizedName"] + "\"].isnull()"
				file.write(indentation + "required=True,")
			else:
				file.write(indentation + "required=False,")
			# NCBI column description
			if attribute["Description"]:
				file.write(indentation + "description=\"" + attribute["Description"].strip().replace("\"", "\\\"").replace("\n"," ") + "\",")
			# Human readable field name for submission
			file.write(indentation + "title=\"" + attribute["Name"] + "\",")
			# Close attribute
			indentation = indentation[:-1]
			file.write(indentation + "),")
		# Close columns
		indentation = indentation[:-1]
		file.write(indentation + "},")
		# Create dataframe wide checks
		if bool(mandatory_group):
			file.write(indentation + "checks=[")
			# Validate columns that are required but have multiple options
			indentation += "\t"
			for key in mandatory_group:
				file.write(indentation + "Check(lambda df: ~(" + mandatory_group[key] + "), ignore_na = False),")
			# Close checks
			indentation = indentation[:-1]
			file.write(indentation + "],")
		else:
			file.write(indentation + "checks=None,")
		file.write(indentation + "index=None,")
		file.write(indentation + "coerce=False,")
		file.write(indentation + "strict=\"filter\",")
		file.write(indentation + "name=\"biosample_package_" + name + "_schema\",")
		file.write(indentation + "ordered=False,")
		file.write(indentation + "unique=None,")
		file.write(indentation + "report_duplicates=\"all\",")
		file.write(indentation + "unique_column_names=True,")
		file.write(indentation + "add_missing_columns=True,")
		file.write(indentation + "title=\"BioSample package " + name + " schema\",")
		file.write(indentation + "description=\"Schema validation for BioSample database using " + name + " package.\",")
		# Close schema
		indentation = indentation[:-1]
		file.write(indentation + ")")
