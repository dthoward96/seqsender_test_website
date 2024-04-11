from pandera import DataFrameSchema, Column, Check, Index, MultiIndex

schema = DataFrameSchema(
	columns={
		"sequence_name": Column(
			dtype="object",
			checks=[
				Check.str_matches(r"^(?!\s*$).+"),
				Check.str_length(max_value=50),
			],
			nullable=False,
			unique=True,
			coerce=False,
			description="Sequence identifier used in fasta file. This is used to create the fasta file for Genbank or GISAID.",
			title="sequence name",
		),
		"organism": Column(
			dtype="object",
			checks=[
				Check.str_matches(r"^(?!\s*$).+"),
			],
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="The most descriptive organism name for the samples.",
			title="organism",
		),
		"authors": Column(
			dtype="object",
			checks=[
				Check.str_matches(r"^(?!\s*$).+"),
			],
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="Citing authors. List of <b>Last, First Middle, suffix</b> separated by a semicolon \";\" E.g.: \"Baker, Howard Henry, Jr.; Powell, Earl Alexander, III.;\"",
			title="authors",
		),
		"collection_date": Column(
			dtype="object",
			checks=None,
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="Collection date for sequence. Must be in a valid format based on ISO 8601: \"YYYY-MM-DD\", \"YYYY-MM\", or \"YYYY\". Time is not supported.",
			title="collection date",
		),
		"bioproject": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="NCBI BioProject ID.",
			title="bioproject",
		),
	},
     checks=None,
     index=None,
     dtype=None,
     coerce=False,
     strict="filter",
     name="seqsender_schema",
     ordered=False,
     unique=None,
     report_duplicates="all",
     unique_column_names=True,
     add_missing_columns=False,
     title="seqsender pipeline schema",
     description="Schema validation for the base requirements to operate Seqsender for all databases.",
)
