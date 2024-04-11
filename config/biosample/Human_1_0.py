from pandera import DataFrameSchema, Column, Check, Index, MultiIndex

schema = DataFrameSchema(
	columns={
		"bs-isolate": Column(
			dtype="object",
			checks=None,
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="identification or description of the specific individual from which this sample was obtained",
			title="isolate",
		),
		"bs-age": Column(
			dtype="object",
			checks=None,
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="age at the time of sampling; relevant scale depends on species and study, e.g. could be seconds for amoebae or centuries for trees",
			title="age",
		),
		"bs-biomaterial_provider": Column(
			dtype="object",
			checks=None,
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="name and address of the lab or PI, or a culture collection identifier",
			title="biomaterial provider",
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
		"bs-sex": Column(
			dtype="object",
			checks=Check.str_matches(r"(?i)(\W|^)(male|female|pooled male and female|neuter|hermaphrodite|intersex|not determined|missing|not applicable|not collected|not provided|restricted access)(\W|$)"),
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="physical sex of sampled organism",
			title="sex",
		),
		"bs-tissue": Column(
			dtype="object",
			checks=None,
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="Type of tissue the sample was taken from.",
			title="tissue",
		),
		"bs-cell_line": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Name of the cell line.",
			title="cell line",
		),
		"bs-cell_subtype": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			title="cell subtype",
		),
		"bs-cell_type": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Type of cell of the sample or from which the sample was obtained.",
			title="cell type",
		),
		"bs-culture_collection": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Name of source institute and unique culture identifier. See the description for the proper format and list of allowed institutes, http://www.insdc.org/controlled-vocabulary-culturecollection-qualifier",
			title="culture collection",
		),
		"bs-dev_stage": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Developmental stage at the time of sampling.",
			title="development stage",
		),
		"bs-disease": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="list of diseases diagnosed; can include multiple diagnoses. the value of the field depends on host; for humans the terms should be chosen from DO (Disease Ontology), free text for non-human. For DO terms, please see http://gemina.svn.sourceforge.net/viewvc/gemina/trunk/Gemina/ontologies/gemina_symptom.obo?view=log",
			title="disease",
		),
		"bs-disease_stage": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="stage of disease at the time of sampling.",
			title="disease stage",
		),
		"bs-ethnicity": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="ethnicity of the subject",
			title="ethnicity",
		),
		"bs-health_state": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Health or disease status of sample at time of collection",
			title="health state",
		),
		"bs-karyotype": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			title="karyotype",
		),
		"bs-phenotype": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Phenotype of sampled organism. For Phenotypic quality Ontology (PATO) (v1.269) terms, please see http://bioportal.bioontology.org/visualize/44601",
			title="phenotype",
		),
		"bs-population": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="for human: ; for plants: filial generation, number of progeny, genetic structure",
			title="population",
		),
		"bs-race": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			title="race",
		),
		"bs-sample_type": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Sample type, such as cell culture, mixed culture, tissue sample, whole organism, single cell, metagenomic assembly",
			title="sample type",
		),
		"bs-treatment": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			title="treatment",
		),
	},
	checks=None,
	index=None,
	dtype=None,
	coerce=False,
	strict="filter",
	name="biosample_package_Human.1.0_schema",
	ordered=False,
	unique=None,
	report_duplicates="all",
	unique_column_names=True,
	add_missing_columns=True,
	title="BioSample package Human.1.0 schema",
	description="Schema validation for BioSample database using Human.1.0 package.",
)