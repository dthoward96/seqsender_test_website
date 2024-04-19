from pandera import DataFrameSchema, Column, Check, Index, MultiIndex

schema = DataFrameSchema(
	columns={
		"bs-strain": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=True,
			description="microbial or eukaryotic strain name",
			title="strain",
		),
		"bs-isolate": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=True,
			description="identification or description of the specific individual from which this sample was obtained",
			title="isolate",
		),
		"bs-env_broad_scale": Column(
			dtype="object",
			checks=None,
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="Add terms that identify the major environment type(s) where your sample was collected. Recommend subclasses of biome [ENVO:00000428]. Multiple terms can be separated by one or more pipes e.g.:  mangrove biome [ENVO:01000181]|estuarine biome [ENVO:01000020]",
			title="broad-scale environmental context",
		),
		"bs-env_local_scale": Column(
			dtype="object",
			checks=None,
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="Add terms that identify environmental entities having causal influences upon the entity at time of sampling, multiple terms can be separated by pipes, e.g.:  shoreline [ENVO:00000486]|intertidal zone [ENVO:00000316]",
			title="local-scale environmental context",
		),
		"bs-env_medium": Column(
			dtype="object",
			checks=None,
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="Add terms that identify the material displaced by the entity at time of sampling. Recommend subclasses of environmental material [ENVO:00010483]. Multiple terms can be separated by pipes e.g.: estuarine water [ENVO:01000301]|estuarine mud [ENVO:00002160]",
			title="environmental medium",
		),
		"bs-geo_loc_name": Column(
			dtype="object",
			checks=None,
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="Geographical origin of the sample; use the appropriate name from this list http://www.insdc.org/documents/country-qualifier-vocabulary. Use a colon to separate the country or ocean from more detailed information about the location, eg \"Canada: Vancouver\" or \"Germany: halfway down Zugspitze, Alps\"",
			title="geographic location",
		),
		"bs-host": Column(
			dtype="object",
			checks=None,
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="The natural (as opposed to laboratory) host to the organism from which the sample was obtained. Use the full taxonomic name, eg, \"Homo sapiens\".",
			title="host",
		),
		"bs-isol_growth_condt": Column(
			dtype="object",
			checks=None,
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="PMID or url for isolation and growth condition specifications",
			title="isolation and growth condition",
		),
		"bs-lat_lon": Column(
			dtype="object",
			checks=None,
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="The geographical coordinates of the location where the sample was collected. Specify as degrees latitude and longitude in format \"d[d.dddd] N|S d[dd.dddd] W|E\", eg, 38.98 N 77.11 W",
			title="latitude and longitude",
		),
		"bs-propagation": Column(
			dtype="object",
			checks=None,
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="phage: lytic/lysogenic/temperate/obligately lytic; plasmid: incompatibility group; eukaryote: asexual/sexual",
			title="propagation",
		),
		"bs-altitude": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="The altitude of the sample is the vertical distance between Earth's surface above Sea Level and the sampled position in the air.",
			title="altitude",
		),
		"bs-ances_data": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Information about either pedigree or other ancestral information description, e.g., parental variety in case of mutant or selection, A/3*B (meaning [(A x B) x B] x B)",
			title="ancestral data",
		),
		"bs-biol_stat": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="The level of genome modification, e.g., wild, natural, semi-natural, inbred line, breeder's line, hybrid, clonal selection, mutant",
			title="biological status",
		),
		"bs-biotic_relationship": Column(
			dtype="object",
			checks=Check.str_matches(r"(?i)(\W|^)(free living|parasite|commensal|symbiont)(\W|$)"),
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Free-living or from host (define relationship)",
			title="observed biotic relationship",
		),
		"bs-chem_administration": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="list of chemical compounds administered to the host or site where sampling occurred, and when (e.g. antibiotics, N fertilizer, air filter); can include multiple compounds. For Chemical Entities of Biological Interest ontology (CHEBI) (v1.72), please see http://bioportal.bioontology.org/visualize/44603",
			title="chemical administration",
		),
		"bs-collection_method": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Process used to collect the sample, e.g., bronchoalveolar lavage (BAL)",
			title="collection method",
		),
		"bs-depth": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Depth is defined as the vertical distance below surface, e.g. for sediment or soil samples depth is measured from sediment or soil surface, respectivly. Depth can be reported as an interval for subsurface samples.",
			title="depth",
		),
		"bs-elev": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="The elevation of the sampling site as measured by the vertical distance from mean sea level.",
			title="elevation",
		),
		"bs-encoded_traits": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Traits like antibiotic resistance/xenobiotic degration phenotypes/converting phage genes",
			title="encoded traits",
		),
		"bs-estimated_size": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Estimated size of genome",
			title="estimated size",
		),
		"bs-genetic_mod": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Genetic modifications of the genome of an organism, which may occur naturally by spontaneous mutation, or be introduced by some experimental means, e.g. specification of a transgene or the gene knocked-out or details of transient transfection",
			title="genetic modification",
		),
		"bs-gravidity": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="whether or not subject is gravid, and if yes date due or date post-conception, specifying which is used",
			title="gravidity",
		),
		"bs-host_age": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Age of host at the time of sampling",
			title="host age",
		),
		"bs-host_blood_press_diast": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="resting diastolic blood pressureof the host, measured as mm mercury",
			title="host blood pressure diastolic",
		),
		"bs-host_blood_press_syst": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="resting systolic blood pressure of the host, measured as mm mercury",
			title="host blood pressure systolic",
		),
		"bs-host_body_habitat": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="original body habitat where the sample was obtained from",
			title="host body habitat",
		),
		"bs-host_body_product": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="substance produced by the host, e.g. stool, mucus, where the sample was obtained from",
			title="host body product",
		),
		"bs-host_body_temp": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="core body temperature of the host when sample was collected",
			title="host body temperature",
		),
		"bs-host_color": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="the color of host",
			title="host color",
		),
		"bs-host_common_name": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="The natural language (non-taxonomic) name of the host organism, e.g., mouse",
			title="host common name",
		),
		"bs-host_diet": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="type of diet depending on the sample for animals omnivore, herbivore etc., for humans high-fat, meditteranean etc.; can include multiple diet types",
			title="host diet",
		),
		"bs-host_disease": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Name of relevant disease, e.g. Salmonella gastroenteritis. Controlled vocabulary, http://bioportal.bioontology.org/ontologies/1009 or http://www.ncbi.nlm.nih.gov/mesh",
			title="host disease",
		),
		"bs-host_dry_mass": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="measurement of dry mass",
			title="host dry mass",
		),
		"bs-host_family_relationship": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			title="host family relationship",
		),
		"bs-host_genotype": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			title="host genotype",
		),
		"bs-host_growth_cond": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="literature reference giving growth conditions of the host",
			title="host growth conditions",
		),
		"bs-host_height": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="the height of subject",
			title="host height",
		),
		"bs-host_last_meal": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="content of last meal and time since feeding; can include multiple values",
			title="host last meal",
		),
		"bs-host_length": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="the length of subject",
			title="host length",
		),
		"bs-host_life_stage": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="description of host life stage",
			title="host life stage",
		),
		"bs-host_phenotype": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			title="host phenotype",
		),
		"bs-host_sex": Column(
			dtype="object",
			checks=Check.str_matches(r"(?i)(\W|^)(male|female|pooled male and female|neuter|hermaphrodite|intersex|not determined|missing|not applicable|not collected|not provided|restricted access)(\W|$)"),
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Gender or physical sex of the host",
			title="host sex",
		),
		"bs-host_shape": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="morphological shape of host",
			title="host shape",
		),
		"bs-host_subject_id": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="a unique identifier by which each subject can be referred to, de-identified, e.g. #131",
			title="host subject id",
		),
		"bs-host_subspecf_genlin": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Information about the genetic distinctness of the host organism below the subspecies level e.g., serovar, serotype, biotype, ecotype, variety, cultivar, or any relevant genetic typing schemes like Group I plasmid. Subspecies should not be recorded in this term, but in the NCBI taxonomy. Supply both the lineage name and the lineage rank separated by a colon, e.g., biovar:abc123",
			title="host subspecific genetic lineage",
		),
		"bs-host_substrate": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="the growth substrate of the host",
			title="host substrate",
		),
		"bs-host_symbiont": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="The taxonomic name of the organism(s) found living in mutualistic, commensalistic, or parasitic symbiosis with the specific host",
			title="observed host symbionts",
		),
		"bs-host_taxid": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="NCBI taxonomy ID of the host, e.g. 9606",
			title="host taxonomy ID",
		),
		"bs-host_tissue_sampled": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="name of body site where the sample was obtained from, such as a specific organ or tissue, e.g., tongue, lung. For foundational model of anatomy ontology (fma) (v 4.11.0) or Uber-anatomy ontology (UBERON) (v releases/2014-06-15) terms, please see http://purl.bioontology.org/ontology/FMA or http://purl.bioontology.org/ontology/UBERON",
			title="host tissue sampled",
		),
		"bs-host_tot_mass": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="total mass of the host at collection, the unit depends on host",
			title="host total mass",
		),
		"bs-isolation_source": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Describes the physical, environmental and/or local geographical source of the biological sample from which the sample was derived.",
			title="isolation source",
		),
		"bs-misc_param": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="any other measurement performed or parameter collected, that is not listed here",
			title="miscellaneous parameter",
		),
		"bs-neg_cont_type": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="The substance or equipment used as a negative control in an investigation, e.g., distilled water, phosphate buffer, empty collection device, empty collection tube, DNA-free PCR mix, sterile swab, sterile syringe",
			title="negative control type",
		),
		"bs-num_replicons": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Number of replicons in nuclear genome",
			title="number of replicons",
		),
		"bs-omics_observ_id": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="A unique identifier of the omics-enabled observatory (or comparable time series) your data derives from. This identifier should be provided by the OMICON ontology; if you require a new identifier for your time series, contact the ontology's developers. Information is available here: https://github.com/GLOMICON/omicon. This field is only applicable to records which derive from an omics time-series or observatory.",
			title="Omics Observatory ID",
		),
		"bs-organism_count": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="total count of any organism per gram or volume of sample,should include name of organism followed by count; can include multiple organism counts",
			title="organism count",
		),
		"bs-oxy_stat_samp": Column(
			dtype="object",
			checks=Check.str_matches(r"(?i)(\W|^)(aerobic|anaerobic)(\W|$)"),
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="oxygenation status of sample",
			title="oxygenation status of sample",
		),
		"bs-pathogenicity": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="To what is the entity pathogenic",
			title="pathogenicity",
		),
		"bs-perturbation": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="type of perturbation, e.g. chemical administration, physical disturbance, etc., coupled with time that perturbation occurred; can include multiple perturbation types",
			title="perturbation",
		),
		"bs-pos_cont_type": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="The substance, mixture, product, or apparatus used to verify that a process which is part of an investigation delivers a true positive",
			title="positive control type",
		),
		"bs-ref_biomaterial": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Primary publication or genome report",
			title="reference for biomaterial",
		),
		"bs-samp_capt_status": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Reason for the sample, e.g., active surveillance in response to an outbreak, active surveillance not initiated by an outbreak, farm sample, market sample",
			title="sample capture status",
		),
		"bs-samp_collect_device": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Method or device employed for collecting sample",
			title="sample collection device or method",
		),
		"bs-samp_dis_stage": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Stage of the disease at the time of sample collection, e.g., dissemination, growth and reproduction, infection, inoculation, penetration",
			title="sample disease stage",
		),
		"bs-samp_mat_process": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Processing applied to the sample during or after isolation",
			title="sample material processing",
		),
		"bs-samp_salinity": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			title="sample salinity",
		),
		"bs-samp_size": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Amount or size of sample (volume, mass or area) that was collected",
			title="sample size",
		),
		"bs-samp_store_dur": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			title="sample storage duration",
		),
		"bs-samp_store_loc": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			title="sample storage location",
		),
		"bs-samp_store_temp": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			title="sample storage temperature",
		),
		"bs-samp_vol_we_dna_ext": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="volume (mL) or weight (g) of sample processed for DNA extraction",
			title="sample volume or weight for DNA extraction",
		),
		"bs-source_material_id": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="unique identifier assigned to a material sample used for extracting nucleic acids, and subsequent sequencing. The identifier can refer either to the original material collected or to any derived sub-samples.",
			title="source material identifiers",
		),
		"bs-subspecf_gen_lin": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Information about the genetic distinctness of the lineage (eg., biovar, serovar)",
			title="subspecific genetic lineage",
		),
		"bs-temp": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="temperature of the sample at time of sampling",
			title="temperature",
		),
	},
	checks=[
		Check(lambda df: ~(df["bs-strain"].isnull() & df["bs-isolate"].isnull()), ignore_na = False),
	],
	index=None,
	coerce=False,
	strict="filter",
	name="biosample_package_MIGS.vi.host-associated.6.0_schema",
	ordered=False,
	unique=None,
	report_duplicates="all",
	unique_column_names=True,
	add_missing_columns=True,
	title="BioSample package MIGS.vi.host-associated.6.0 schema",
	description="Schema validation for BioSample database using MIGS.vi.host-associated.6.0 package.",
)