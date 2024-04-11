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
		"bs-cultivar": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=True,
			description="cultivar name - cultivated variety of plant",
			title="cultivar",
		),
		"bs-ecotype": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=True,
			description="a population within a given species displaying genetically based, phenotypic traits that reflect adaptation to a local habitat, e.g., Columbia",
			title="ecotype",
		),
		"bs-depth": Column(
			dtype="object",
			checks=None,
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="Depth is defined as the vertical distance below surface, e.g. for sediment or soil samples depth is measured from sediment or soil surface, respectivly. Depth can be reported as an interval for subsurface samples.",
			title="depth",
		),
		"bs-elev": Column(
			dtype="object",
			checks=None,
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="The elevation of the sampling site as measured by the vertical distance from mean sea level.",
			title="elevation",
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
		"bs-alkyl_diethers": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="concentration of alkyl diethers",
			title="alkyl diethers",
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
		"bs-aminopept_act": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="measurement of aminopeptidase activity",
			title="aminopeptidase activity",
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
		"bs-bacteria_carb_prod": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="measurement of bacterial carbon production",
			title="bacterial carbon production",
		),
		"bs-biomass": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="amount of biomass; should include the name for the part of biomass measured, e.g. microbial, total. can include multiple measurements",
			title="biomass",
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
		"bs-bishomohopanol": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="concentration of bishomohopanol",
			title="bishomohopanol",
		),
		"bs-bromide": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="concentration of bromide",
			title="bromide",
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
		"bs-carb_nitro_ratio": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="ratio of amount or concentrations of carbon to nitrogen",
			title="carbon/nitrogen ratio",
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
		"bs-chlorophyll": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="concentration of chlorophyll",
			title="chlorophyll",
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
		"bs-diether_lipids": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="concentration of diether lipids; can include multiple types of diether lipids",
			title="diether lipids",
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
		"bs-diss_hydrogen": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="concentration of dissolved hydrogen",
			title="dissolved hydrogen",
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
		"bs-diss_org_nitro": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="dissolved organic nitrogen concentration measured as; total dissolved nitrogen - NH4 - NO3 - NO2",
			title="dissolved organic nitrogen",
		),
		"bs-diss_oxygen": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="concentration of dissolved oxygen",
			title="dissolved oxygen",
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
		"bs-glucosidase_act": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="measurement of glucosidase activity",
			title="glucosidase activity",
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
		"bs-mean_frict_vel": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="measurement of mean friction velocity",
			title="mean friction velocity",
		),
		"bs-mean_peak_frict_vel": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="measurement of mean peak friction velocity",
			title="mean peak friction velocity",
		),
		"bs-methane": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="methane (gas) amount or concentration at the time of sampling",
			title="methane",
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
		"bs-n_alkanes": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="concentration of n-alkanes; can include multiple n-alkanes",
			title="n alkanes",
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
		"bs-nitro": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="concentration of nitrogen (total)",
			title="nitrogen",
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
		"bs-org_carb": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="concentration of organic carbon",
			title="organic carbon",
		),
		"bs-org_matter": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="concentration of organic matter",
			title="organic matter",
		),
		"bs-org_nitro": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="concentration of organic nitrogen",
			title="organic nitrogen",
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
		"bs-part_org_carb": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="concentration of particulate organic carbon",
			title="particulate organic carbon",
		),
		"bs-particle_class": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="particles are classified, based on their size, into six general categories:clay, silt, sand, gravel, cobbles, and boulders; should include amount of particle preceded by the name of the particle type; can include multiple values",
			title="particle classification",
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
		"bs-petroleum_hydrocarb": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="concentration of petroleum hydrocarbon",
			title="petroleum hydrocarbon",
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
		"bs-phaeopigments": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="concentration of phaeopigments; can include multiple phaeopigments",
			title="phaeopigments",
		),
		"bs-phosphate": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="concentration of phosphate",
			title="phosphate",
		),
		"bs-phosplipid_fatt_acid": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="concentration of phospholipid fatty acids; can include multiple values",
			title="phospholipid fatty acid",
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
		"bs-redox_potential": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="redox potential, measured relative to a hydrogen cell, indicating oxidation or reduction potential",
			title="redox potential",
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
		"bs-sediment_type": Column(
			dtype="object",
			checks=Check.str_matches(r"(?i)(\W|^)(biogenous|cosmogenous|hydrogenous|lithogenous)(\W|$)"),
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="information about the sediment type based on major constituents",
			title="sediment type",
		),
		"bs-silicate": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="concentration of silicate",
			title="silicate",
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
		"bs-tidal_stage": Column(
			dtype="object",
			checks=Check.str_matches(r"(?i)(\W|^)(low|high)(\W|$)"),
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="stage of tide",
			title="tidal stage",
		),
		"bs-tot_carb": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="total carbon content",
			title="total carbon",
		),
		"bs-tot_depth_water_col": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="measurement of total depth of water column",
			title="total depth of water column",
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
		"bs-tot_org_carb": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Definition for soil: total organic C content of the soil units of g C/kg soil. Definition otherwise: total organic carbon content",
			title="total organic carbon",
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
		"bs-turbidity": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="turbidity measurement",
			title="turbidity",
		),
		"bs-water_content": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="water content measurement",
			title="water content",
		),
	},
	checks=[
		Check(lambda df: ~(df["bs-strain"].isnull() & df["bs-isolate"].isnull() & df["bs-cultivar"].isnull() & df["bs-ecotype"].isnull()), ignore_na = False),
	],
	index=None,
	dtype=None,
	coerce=False,
	strict="filter",
	name="biosample_package_MIGS.eu.sediment.6.0_schema",
	ordered=False,
	unique=None,
	report_duplicates="all",
	unique_column_names=True,
	add_missing_columns=True,
	title="BioSample package MIGS.eu.sediment.6.0 schema",
	description="Schema validation for BioSample database using MIGS.eu.sediment.6.0 package.",
)