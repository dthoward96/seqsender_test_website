from pandera import DataFrameSchema, Column, Check, Index, MultiIndex

schema = DataFrameSchema(
	columns={
		"gs-arbo_sequence_name": Column(
			dtype="object",
			checks=[
				Check.str_length(min_value=1,max_value=50),
			],
			nullable=False,
			unique=True,
			coerce=False,
			description="Sequence identifier used in fasta file. This is used to create the fasta file for Genbank or GISAID.",
			title="sequence name",
		),
		"gs-arbo_type": Column(
			dtype="object",
			checks=[
				Check.str_matches("Chikungunya virus"),
			],
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			default="Chikungunya virus",
			description="For hCoV-19, this will always be \"Chikungunya virus\".",
			title="virus type",
		),
		"gs-arbo_passage": Column(
			dtype="object",
			checks=[
				Check.str_matches(r"^(?!\s*$).+"),
			],
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="\"Original\" if the sample was sequenced directly from swabs, otherwise add the name of the cell line (e.g., \"Vero\") used to culture the specimen.",
			title="passage",
		),
		"gs-arbo_location": Column(
			dtype="object",
			checks=[
				Check.str_matches(r"^(?!\s*$).+"),
			],
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="Format as \"Continent / Country / Region / Sub-region\".",
			title="location",
		),
		"gs-arbo_add_location": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Additional location information (e.g. Cruise Ship, Convention, Live animal market).",
			title="additional location information",
		),
		"gs-arbo_host": Column(
			dtype="object",
			checks=[
				Check.str_matches(r"^(?!\s*$).+"),
			],
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="Host species name. For Wastewater use \"Environment\".",
			title="host",
		),
		"gs-arbo_add_host_info": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Additional information regarding patient (e.g. Patient infected while interacting with animal).",
			title="Additional host information",
		),
		"gs-arbo_sampling_strategy": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Sampling strategy for sequence (e.g. Sentinel surveillance (ILI), Sentinel surveillance (ARI), Sentinel surveillance (SARI), Non-sentinel-surveillance (hospital), Non-sentinel-surveillance (GP network), Longitudinal sampling on same patient(s), S gene dropout).",
			title="sampling strategy",
		),
		"gs-arbo_gender": Column(
			dtype="object",
			checks=[
				Check.str_matches(r"(?i)(\W|^)(male|m|female|f|unknown|missing)(\W|$)"),
			],
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="Synonym for \"Biological sex\". Should be \"Female\", \"Male\", or \"Unknown\".",
			title="gender",
		),
		"gs-arbo_patient_age": Column(
			dtype="object",
			checks=[
				Check.str_matches(r"^(?!\s*$).+"),
			],
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="Age in years of the person from whom the specimen was collected. May take format other than numeric years, for example, \"0.5\" (i.e., 6 months), \"5 days\", \"7 months\". If units are not given, they are assumed in years. If missing, use \"Unknown\".",
			title="patient age",
		),
		"gs-arbo_patient_status": Column(
			dtype="object",
			checks=[
				Check.str_matches(r"^(?!\s*$).+"),
			],
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="E.g., \"Hospitalized\", \"Released\", \"Live\", \"Deceased\", \"Unknown\".",
			title="patient status",
		),
		"gs-arbo_disease_manifestation": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Mild, Severe (e.g Guillain-Barré syndrome (GBS)/ encephalitis/ microcephaly), Fatal.",
			title="disease manifestation",
		),
		"gs-arbo_clinical_symptoms": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="e.g. fever, rash ,nausea, vomiting, retro-orbital pain, muscle pain.",
			title="clinical symptoms",
		),
		"gs-arbo_specimen": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Specimen source. For wastewater it must be \"Wastewater surveillance\".",
			title="specimen source",
		),
		"gs-arbo_outbreak": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Outbreak information (Date, Location e.g. type of gathering, Family cluster, etc.).",
			title="outbreak information",
		),
		"gs-arbo_last_vaccinated": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Provide details if applicable.",
			title="last vaccinated",
		),
		"gs-arbo_treatment": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Provide details if applicable (e.g. Drug name, dosage).",
			title="treatment",
		),
		"gs-arbo_seq_technology": Column(
			dtype="object",
			checks=[
				Check.str_matches(r"^(?!\s*$).+"),
			],
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="Add the sequencer brand and model (e.g. Illumina MiSeq, Sanger, Nanopore MinION).",
			title="sequencing technology",
		),
		"gs-arbo_assembly_method": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Genome assembly algorithm (e.g. CLC Genomics Workbench 12, Geneious 10.2.4, SPAdes/MEGAHIT v1.2.9, UGENE v. 33).",
			title="assembly method",
		),
		"gs-arbo_coverage": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Average genome coverage (e.g. 50x, 100x, 1,000x).",
			title="average coverage",
		),
		"gs-arbo_publications": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="e.g. DOI: 10.1081/15588742.2015.1017687.",
			title="publications",
		),
		"gs-arbo_orig_lab": Column(
			dtype="object",
			checks=[
				Check.str_matches(r"^(?!\s*$).+"),
			],
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="Full name of laboratory from where sample originated.",
			title="originating lab",
		),
		"gs-arbo_orig_lab_addr": Column(
			dtype="object",
			checks=[
				Check.str_matches(r"^(?!\s*$).+"),
			],
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="Complete building address of laboratory from where sample originated.",
			title="originating lab address",
		),
		"gs-arbo_provider_sample_id": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="ID used by originating lab.",
			title="provider sample id",
		),
		"gs-arbo_subm_lab": Column(
			dtype="object",
			checks=[
				Check.str_matches(r"^(?!\s*$).+"),
			],
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="Full name of laboratory submitting this record to GISAID.",
			title="submitting lab",
		),
		"gs-arbo_subm_lab_addr": Column(
			dtype="object",
			checks=[
				Check.str_matches(r"^(?!\s*$).+"),
			],
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="Complete building address of the submitting laboratory.",
			title="submitting lab address",
		),
		"gs-arbo_subm_sample_id": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="ID used by submitting lab.",
			title="submitter sample id",
		),
		"gs-arbo_consortium": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Sequencing consortium the submitting lab is affiliated with.",
			title="sequencing consortium",
		),
		"gs-arbo_comment": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=True,
			description="Leave blank.",
			title="comment",
		),
		"gs-comment_type": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=True,
			description="Leave blank.",
			title="comment type",
		),
	},
     checks=None,
     index=None,
     coerce=False,
     strict="filter",
     name="gisaid_arbo_schema",
     ordered=False,
     unique=None,
     report_duplicates="all",
     unique_column_names=True,
     add_missing_columns=True,
     title="seqsender GISAID ARBO schema",
     description="Schema validation for GISAID Arbovirus database.",
)
