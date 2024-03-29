from pandera import DataFrameSchema, Column, Check, Index, MultiIndex

schema = DataFrameSchema(
	columns={
		"bs-strain": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			description="microbial or eukaryotic strain name",
			title="strain",
		),
		"bs-isolate": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			description="identification or description of the specific individual from which this sample was obtained",
			title="isolate",
		),
		"bs-cultivar": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			description="cultivar name - cultivated variety of plant",
			title="cultivar",
		),
		"bs-ecotype": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			description="a population within a given species displaying genetically based, phenotypic traits that reflect adaptation to a local habitat, e.g., Columbia",
			title="ecotype",
		),
		"bs-api": Column(
			dtype="object",
			checks=None,
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="API gravity is a measure of how heavy or light a petroleum liquid is compared to water (source: https://en.wikipedia.org/wiki/API_gravity), e.g. 31.1 API",
			title="API gravity",
		),
		"bs-basin_name": Column(
			dtype="object",
			checks=None,
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="Name of the basin, e.g. Campos",
			title="basin name",
		),
		"bs-collection_date": Column(
			dtype="object",
			checks=None,
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="the date on which the sample was collected; date/time ranges are supported by providing two dates from among the supported value formats, delimited by a forward-slash character; collection times are supported by adding \"T\", then the hour and minute after the date, and must be in Coordinated Universal Time (UTC), otherwise known as \"Zulu Time\" (Z); supported formats include \"DD-Mmm-YYYY\", \"Mmm-YYYY\", \"YYYY\" or ISO 8601 standard \"YYYY-mm-dd\", \"YYYY-mm\", \"YYYY-mm-ddThh:mm:ss\"; e.g., 30-Oct-1990, Oct-1990, 1990, 1990-10-30, 1990-10,  21-Oct-1952/15-Feb-1953, 2015-10-11T17:53:03Z; valid non-ISO dates will be automatically transformed to ISO format",
			title="collection date",
		),
		"bs-env_broad_scale": Column(
			dtype="object",
			checks=None,
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="Add terms that identify the major environment type(s) where your sample was collected. Recommend subclasses of biome [ENVO:00000428]. Multiple terms can be separated by one or more pipes e.g.: Â mangrove biome [ENVO:01000181]|estuarine biome [ENVO:01000020]",
			title="broad-scale environmental context",
		),
		"bs-env_local_scale": Column(
			dtype="object",
			checks=None,
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="Add terms that identify environmental entities having causal influences upon the entity at time of sampling, multiple terms can be separated by pipes, e.g.: Â shoreline [ENVO:00000486]|intertidal zone [ENVO:00000316]",
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
		"bs-hc_produced": Column(
			dtype="object",
			checks=None,
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="Main hydrocarbon type produced from resource, e.g., oil, gas-condensate, gas, bitumen, coalbed methane",
			title="hydrocarbon type produced",
		),
		"bs-hcr": Column(
			dtype="object",
			checks=None,
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="Main hydrocarbon resource type. The term Hydrocarbon Resource is defined as a natural environmental feature containing large amounts of hydrocarbons at high concentrations potentially suitable for commercial exploitation, e.g., oil reservoir, gas reservoir, oil sand, coalbed, shale, tight oil reservoir, tight gas reservoir",
			title="hydrocarbon resource type",
		),
		"bs-hcr_temp": Column(
			dtype="object",
			checks=None,
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="Original temperature of the hydrocarbon resource",
			title="hydrocarbon resource original temperature",
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
		"bs-samp_mat_type": Column(
			dtype="object",
			checks=None,
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="The type of material from which the sample was obtained. For the Hydrocarbon package, samples include types like core, rock trimmings, drill cuttings, piping section, coupon, pigging debris, solid deposit, produced fluid, produced water, injected water, swabs, etc. For the Food Package, samples are usually categorized as food, body products or tissues, or environmental material. This field accepts terms listed under environmental specimen (http://purl.obolibrary.org/obo/GENEPIO_0001246)",
			title="sample material type (host or environmental context)",
		),
		"bs-sulfate_fw": Column(
			dtype="object",
			checks=None,
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="Original sulfate concentration in the hydrocarbon resource",
			title="sulfate in formation water",
		),
		"bs-temp": Column(
			dtype="object",
			checks=None,
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="temperature of the sample at time of sampling",
			title="temperature",
		),
		"bs-vfa_fw": Column(
			dtype="object",
			checks=None,
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="Original volatile fatty acid concentration in the hydrocarbon resource",
			title="vfa in formation water",
		),
		"bs-additional_info": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Information that doesn't fit anywhere else",
			title="additional info",
		),
		"bs-alkalinity": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="alkalinity, the ability of a solution to neutralize acids to the equivalence point of carbonate or bicarbonate",
			title="alkalinity",
		),
		"bs-alkalinity_method": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Method used for alkalinity measurement",
			title="alkalinity method",
		),
		"bs-ammonium": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="concentration of ammonium",
			title="ammonium",
		),
		"bs-aromatics_pc": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Saturate, Aromatic, Resin and Asphaltene (SARA) is an analysis method that divides crude oil components according to their polarizability and polarity. There are three main methods to obtain SARA results. The most popular one is known as the Iatroscan TLC-FID and is referred to as IP-143 (source: https://en.wikipedia.org/wiki/Saturate,_aromatic,_resin_and_asphaltene)",
			title="aromatics wt%",
		),
		"bs-asphaltenes_pc": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Saturate, Aromatic, Resin and Asphaltene (SARA) is an analysis method that divides crude oil components according to their polarizability and polarity. There are three main methods to obtain SARA results. The most popular one is known as the Iatroscan TLC-FID and is referred to as IP-143 (source: https://en.wikipedia.org/wiki/Saturate,_aromatic,_resin_and_asphaltene)",
			title="asphaltenes wt%",
		),
		"bs-benzene": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Concentration of benzene in the sample",
			title="benzene",
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
		"bs-calcium": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="concentration of calcium",
			title="calcium",
		),
		"bs-chloride": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="concentration of chloride",
			title="chloride",
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
		"bs-density": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="density of sample",
			title="density",
		),
		"bs-depos_env": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Main depositional environment (https://en.wikipedia.org/wiki/Depositional_environment), e.g., continental - alluvial, continental - aeolian, continental - fluvial, continental - lacustrine, transitional - deltaic, transitional - tidal, transitional - lagoonal, transitional - beach, transitional - lake, marine - shallow, marine - deep, marine - reef, other - evaporite, other - glacial, other - volcanic",
			title="depositional environment",
		),
		"bs-diss_carb_dioxide": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="concentration of dissolved carbon dioxide",
			title="dissolved carbon dioxide",
		),
		"bs-diss_inorg_carb": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="dissolved inorganic carbon concentration",
			title="dissolved inorganic carbon",
		),
		"bs-diss_inorg_phosp": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="concentration of dissolved inorganic phosphorus",
			title="dissolved inorganic phosphorus",
		),
		"bs-diss_iron": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Concentration of dissolved iron in the sample",
			title="dissolved iron",
		),
		"bs-diss_org_carb": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="concentration of dissolved organic carbon",
			title="dissolved organic carbon",
		),
		"bs-diss_oxygen_fluid": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Concentration of dissolved oxygen in the oil field produced fluids as it contributes to oxgen-corrosion and microbial activity, e.g. Mic",
			title="dissolved oxygen in fluids",
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
		"bs-ethylbenzene": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Concentration of ethylbenzene in the sample",
			title="ethylbenzene",
		),
		"bs-extrachrom_elements": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Plasmids that have significance phenotypic consequence",
			title="extrachromosomal elements",
		),
		"bs-field": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Name of the hydrocarbon field, e.g., Albacora",
			title="field name",
		),
		"bs-hcr_fw_salinity": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Original formation water salinity (prior to secondary recovery e.g. Waterflooding) expressed as TDS",
			title="formation water salinity",
		),
		"bs-hcr_geol_age": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Geological age of hydrocarbon resource (additional info: https://en.wikipedia.org/wiki/Period_(geology)), e.g., archean, cambrian, carboniferous, cenozoic, cretaceous, devonian, jurassic, mesozoic, neogene, ordovician, paleogene, paleozoic, permian, precambrian, proterozoic, silurian, triassic",
			title="hydrocarbon resource geological age",
		),
		"bs-hcr_pressure": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Original pressure of the hydrocarbon resource",
			title="hydrocarbon resource original pressure",
		),
		"bs-host": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="The natural (as opposed to laboratory) host to the organism from which the sample was obtained. Use the full taxonomic name, eg, \"Homo sapiens\".",
			title="host",
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
		"bs-lithology": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Hydrocarbon resource main lithology (Additional information: http://petrowiki.org/Lithology_and_rock_type_determination), e.g., basement, chalk, chert, coal, conglomerate, diatomite, dolomite, limestone, sandstone, shale, siltstone, volcanic",
			title="lithology",
		),
		"bs-magnesium": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="concentration of magnesium",
			title="magnesium",
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
		"bs-nitrate": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="concentration of nitrate",
			title="nitrate",
		),
		"bs-nitrite": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="concentration of nitrite",
			title="nitrite",
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
			description="A unique identifier of the omics-enabled observatory (or comparable time series) your data derives from. This identifier should be provided by the OMICON ontology; if you require a new identifier for your time series, contact the ontology's developers. Information is available here:Â https://github.com/GLOMICON/omicon. This field is only applicable to records which derive from an omics time-series or observatory.",
			title="Omics Observatory ID",
		),
		"bs-org_count_qpcr_info": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="If qpcr was used for the cell count, the target gene name, the primer sequence and the cycling conditions should also be provided, e.g., 16S rrna; FWD:ACGTAGCTATGACGT REV:GTGCTAGTCGAGTAC; initial denaturation:90C_5min; denaturation:90C_2min; annealing:52C_30 sec; elongation:72C_30 sec; 90 C for 1 min; final elongation:72C_5min; 30 cycles",
			title="organism count qPCR information",
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
		"bs-owc_tvdss": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Depth of the original oil water contact (OWC) zone (average) (m TVDSS)",
			title="oil water contact depth",
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
		"bs-permeability": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Measure of the ability of a hydrocarbon resource to allow fluids to pass through it. Additional information: https://en.wikipedia.org/wiki/Permeability_(earth_sciences)",
			title="permeability",
		),
		"bs-ph": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="pH measurement",
			title="pH",
		),
		"bs-ploidy": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Ploidy level of genome (eg., haploid, diploid)",
			title="ploidy",
		),
		"bs-porosity": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="porosity of deposited sediment is volume of voids divided by the total volume of sample",
			title="porosity",
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
		"bs-potassium": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="concentration of potassium",
			title="potassium",
		),
		"bs-pour_point": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Temperature at which a liquid becomes semi solid and loses its flow characteristics. In crude oil a high pour point is generally associated with a high paraffin content, typically found in crude deriving from a larger proportion of plant material (source: https://en.wikipedia.org/wiki/pour_point)",
			title="pour point",
		),
		"bs-pressure": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="pressure to which the sample is subject, in atmospheres",
			title="pressure",
		),
		"bs-propagation": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="phage: lytic/lysogenic/temperate/obligately lytic; plasmid: incompatibility group; eukaryote: asexual/sexual",
			title="propagation",
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
		"bs-reservoir_name": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Name of the reservoir, e.g., Carapebus",
			title="reservoir name",
		),
		"bs-resins_pc": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Saturate, Aromatic, Resin and Asphaltene (SARA) is an analysis method that divides crude oil components according to their polarizability and polarity. There are three main methods to obtain SARA results. The most popular one is known as the Iatroscan TLC-FID and is referred to as IP-143 (source: https://en.wikipedia.org/wiki/Saturate,_aromatic,_resin_and_asphaltene)",
			title="resins wt%",
		),
		"bs-salinity": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="salinity measurement",
			title="salinity",
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
		"bs-samp_md": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="In non deviated well, measured depth is equal to the true vertical depth, TVD (TVD=TVDSS plus the reference or datum it refers to). In deviated wells, the MD is the length of trajectory of the borehole measured from the same reference or datum. Common datums used are ground level (GL), drilling rig floor (DF), rotary table (RT), kelly bushing (KB) and mean sea level (MSL). If \"other\" is specified, please propose entry in \"additional info\" field",
			title="sample measured depth",
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
		"bs-samp_subtype": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Name of sample sub-type, e.g., oil phase, water phase, biofilm, not applicable",
			title="sample subtype",
		),
		"bs-samp_transport_cond": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Sample transport duration (in days or hrs) and temperature the sample was exposed to (e.g., 5.5 days; 20C)",
			title="sample transport conditions",
		),
		"bs-samp_tvdss": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Depth of the sample i.e. The vertical distance between the sea level and the sampled position in the subsurface. Depth can be reported as an interval for subsurface samples e.g., 1325.75-1362.25 m",
			title="sample true vertical depth subsea",
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
		"bs-samp_well_name": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Name of the well where sample was taken, e.g., BXA1123",
			title="sample well name",
		),
		"bs-saturates_pc": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Saturate, Aromatic, Resin and Asphaltene (SARA) is an analysis method that divides crude oil components according to their polarizability and polarity. There are three main methods to obtain SARA results. The most popular one is known as the Iatroscan TLC-FID and is referred to as IP-143 (source: https://en.wikipedia.org/wiki/Saturate,_aromatic,_resin_and_asphaltene)",
			title="saturates wt%",
		),
		"bs-sodium": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="sodium concentration",
			title="sodium",
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
		"bs-sr_dep_env": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Source rock depositional environment (https://en.wikipedia.org/wiki/Source_rock), e.g., lacustine, fluvioldeltaic, fluviomarine, marine",
			title="source rock depositional environment",
		),
		"bs-sr_geol_age": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Geological age of source rock (Additional info: https://en.wikipedia.org/wiki/Period_(geology)), e.g., archean, cambrian, carboniferous, cenozoic, cretaceous, devonian, jurassic, mesozoic, neogene, ordovician, paleogene, paleozoic, permian, precambrian, proterozoic, silurian, triassic",
			title="source rock geological age",
		),
		"bs-sr_kerog_type": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Origin of kerogen. Type I: Algal (aquatic), Type II: planktonic and soft plant material (aquatic or terrestrial), Type III: terrestrial woody/ fibrous plant material (terrestrial), Type IV: oxidized recycled woody debris (terrestrial) (additional information: https://en.wikipedia.org/wiki/Kerogen), e.g., type I, type II, type III, type IV",
			title="source rock kerogen type",
		),
		"bs-sr_lithology": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Lithology of source rock (https://en.wikipedia.org/wiki/Source_rock), e.g., clastic, carbonate, coal, biosilicieous",
			title="source rock lithology",
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
		"bs-sulfate": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="concentration of sulfate",
			title="sulfate",
		),
		"bs-sulfide": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="concentration of sulfide",
			title="sulfide",
		),
		"bs-suspend_solids": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="concentration of substances including a wide variety of material, such as silt, decaying plant and animal matter, etc,; can include multiple substances",
			title="suspended solids",
		),
		"bs-tan": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Total Acid Number (TAN) is a measurement of acidity that is determined by the amount of potassium hydroxide in milligrams that is needed to neutralize the acids in one gram of oil. It is an important quality measurement of crude oil. (source: https://en.wikipedia.org/wiki/Total_acid_number)",
			title="total acid number",
		),
		"bs-toluene": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Concentration of toluene in the sample",
			title="toluene",
		),
		"bs-tot_iron": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Concentration of total iron in the sample",
			title="total iron",
		),
		"bs-tot_nitro": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="total nitrogen content of the sample",
			title="total nitrogen",
		),
		"bs-tot_phosp": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="total phosphorus concentration, calculated by: total phosphorus = total dissolved phosphorus + particulate phosphorus. Can also be measured without filtering, reported as phosphorus",
			title="total phosphorus",
		),
		"bs-tot_sulfur": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Concentration of total sulfur in the sample",
			title="total sulfur",
		),
		"bs-trophic_level": Column(
			dtype="object",
			checks=Check.str_matches(r"(?i)(\W|^)(autotroph|carboxydotroph|chemoautotroph|chemoheterotroph|chemolithoautotroph|chemolithotroph|chemoorganoheterotroph|chemoorganotroph|chemosynthetic|chemotroph|copiotroph|diazotroph|facultative|heterotroph|lithoautotroph|lithoheterotroph|lithotroph|methanotroph|methylotroph|mixotroph|obligate|chemoautolithotroph|oligotroph|organoheterotroph|organotroph|photoautotroph|photoheterotroph|photolithoautotroph|photolithotroph|photosynthetic|phototroph)(\W|$)"),
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Feeding position in food chain (eg., chemolithotroph)",
			title="trophic level",
		),
		"bs-tvdss_of_hcr_press": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="True vertical depth subsea (TVDSS) of the hydrocarbon resource where the original pressure was measured, e.g., 1578 m",
			title="depth (TVDSS) of hydrocarbon resource pressure",
		),
		"bs-tvdss_of_hcr_temp": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="True vertical depth subsea (TVDSS) of the hydrocarbon resource where the original temperature was measured, e.g., 1345 m",
			title="depth (TVDSS) of hydrocarbon resource temperature",
		),
		"bs-vfa": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Concentration of Volatile Fatty Acids in the sample",
			title="volatile fatty acids",
		),
		"bs-viscosity": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="A measure of oil's resistance to gradual deformation by shear stress or tensile stress (e.g., 3.5 cp; 100C)",
			title="viscosity",
		),
		"bs-win": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="A unique identifier of a well or wellbore. This is part of the Global Framework for Well Identification initiative which is compiled by the Professional Petroleum Data Management Association (PPDM) in an effort to improve well identification systems. (Supporting information: https://ppdm.org/ and http://dl.ppdm.org/dl/690)",
			title="well identification number",
		),
		"bs-xylene": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Concentration of xylene in the sample",
			title="xylene",
		),
	},
	checks=[
		pa.Check(lambda df: df[["strain","isolate","cultivar","ecotype"]].isnull().all()),
	],
	index=None,
	dtype=None,
	coerce=False,
	strict="filter",
	name="biosample_package_MIGS.eu.hydrocarbon-cores.6.0_schema",
	ordered=False,
	unique=None,
	report_duplicates="all",
	unique_column_names=True,
	add_missing_columns=False,
	itle="BioSample package MIGS.eu.hydrocarbon-cores.6.0 schema",
	description="Schema validation for BioSample database using MIGS.eu.hydrocarbon-cores.6.0 package.",
)