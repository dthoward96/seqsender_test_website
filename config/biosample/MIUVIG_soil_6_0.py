from pandera import DataFrameSchema, Column, Check, Index, MultiIndex

schema = DataFrameSchema(
	columns={
		"bs-sample_name": Column(
			dtype="object",
			checks=[
				Check.str_matches(r"^(?!\s*$).+"),
			],
			nullable=False,
			unique=True,
			coerce=False,
			required=True,
			description="Identifier name used for BioSample. Max length is 50 characters.",
			title="sample_name",
		),
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
		"bs-host": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=True,
			description="At least one required: Group \"Source\". The natural (as opposed to laboratory) host to the organism from which the sample was obtained. Use the full taxonomic name, eg, \"Homo sapiens\".",
			title="host",
		),
		"bs-isolation_source": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=True,
			description="At least one required: Group \"Source\". Describes the physical, environmental and/or local geographical source of the biological sample from which the sample was derived.",
			title="isolation source",
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
		"bs-source_uvig": Column(
			dtype="object",
			checks=Check.str_matches(r"(?i)(\W|^)(metagenome (not viral targeted)|viral fraction metagenome (virome)|sequence-targeted metagenome|metatranscriptome (not viral targeted)|viral fraction RNA metagenome (RNA virome)|sequence-targeted RNA metagenome|microbial single amplified genome (SAG)|viral single amplified genome (vSAG)|isolate microbial genome|missing|not applicable|not collected|not provided|restricted access)(\W|$)"),
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="Type of dataset from which the UViG was obtained",
			title="source of UViGs",
		),
		"bs-virus_enrich_appr": Column(
			dtype="object",
			checks=Check.str_matches(r"(?i)(\W|^)(filtration|ultrafiltration|centrifugation|ultracentrifugation|PEG Precipitation|FeCl Precipitation|CsCl density gradient|DNAse|RNAse|targeted sequence capture|missing|not applicable|not collected|not provided|restricted access)(\W|$)"),
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="Approach used to enrich the sample for viruses, if any. If more than one approach was used, include multiple ‘virus_enrich_appr’ fields.",
			title="virus enrichment approach",
		),
		"bs-agrochem_addition": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="addition of fertilizers, pesticides, etc. - amount and time of applications",
			title="agrochemical additions",
		),
		"bs-al_sat": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="aluminum saturation (esp. for tropical soils)",
			title="aluminium saturation",
		),
		"bs-al_sat_meth": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="reference or method used in determining Al saturation",
			title="aluminium saturation method",
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
		"bs-annual_precpt": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="The average of all annual precipitation values known, or an estimated equivalent value derived by such methods as regional indexes or Isohyetal maps",
			title="mean annual precipitation",
		),
		"bs-annual_temp": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Mean annual temperature",
			title="mean annual temperature",
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
		"bs-crop_rotation": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="whether or not crop is rotated, and if yes, rotation schedule",
			title="crop rotation",
		),
		"bs-cur_land_use": Column(
			dtype="object",
			checks=Check.str_matches(r"(?i)(\W|^)(cities|farmstead|industrial areas|roads/railroads|rock|sand|gravel|mudflats|salt flats|badlands|permanent snow or ice|saline seeps|mines/quarries|oil waste areas|small grains|row crops|vegetable crops|horticultural plants (e.g. tulips)|marshlands (grass,sedges,rushes)|tundra (mosses,lichens)|rangeland|pastureland (grasslands used for livestock grazing)|hayland|meadows (grasses,alfalfa,fescue,bromegrass,timothy)|shrub land (e.g. mesquite,sage-brush,creosote bush,shrub oak,eucalyptus)|successional shrub land (tree saplings,hazels,sumacs,chokecherry,shrub dogwoods,blackberries)|shrub crops (blueberries,nursery ornamentals,filberts)|vine crops (grapes)|conifers (e.g. pine,spruce,fir,cypress)|hardwoods (e.g. oak,hickory,elm,aspen)|intermixed hardwood and conifers|tropical (e.g. mangrove,palms)|rainforest (evergreen forest receiving >406 cm annual rainfall)|swamp (permanent or semi-permanent water body dominated by woody plants)|crop trees (nuts,fruit,christmas trees,nursery trees))(\W|$)"),
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="present state of sample site",
			title="current land use",
		),
		"bs-cur_vegetation": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="vegetation classification from one or more standard classification systems, or agricultural crop",
			title="current vegetation",
		),
		"bs-cur_vegetation_meth": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="reference or method used in vegetation classification",
			title="current vegetation method",
		),
		"bs-drainage_class": Column(
			dtype="object",
			checks=Check.str_matches(r"(?i)(\W|^)(very poorly|poorly|somewhat poorly|moderately well|well|excessively drained)(\W|$)"),
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="drainage classification from a standard system such as the USDA system",
			title="drainage classification",
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
		"bs-experimental_factor": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Variable aspect of experimental design",
			title="experimental factor",
		),
		"bs-extreme_event": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="unusual physical events that may have affected microbial populations",
			title="extreme event",
		),
		"bs-fao_class": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="soil classification from the FAO World Reference Database for Soil Resources",
			title="FAO classification",
		),
		"bs-fire": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="historical and/or physical evidence of fire",
			title="fire",
		),
		"bs-flooding": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="historical and/or physical evidence of flooding",
			title="flooding",
		),
		"bs-heavy_metals": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="heavy metals present and concentrationsany drug used by subject and the frequency of usage; can include multiple heavy metals and concentrations",
			title="heavy metals",
		),
		"bs-heavy_metals_meth": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="reference or method used in determining heavy metals",
			title="heavy metals method",
		),
		"bs-horizon_meth": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="reference or method used in determining the horizon",
			title="horizon method",
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
		"bs-link_addit_analys": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			title="links to additional analysis",
		),
		"bs-link_class_info": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="link to digitized soil maps or other soil classification information",
			title="link to classification information",
		),
		"bs-link_climate_info": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="link to climate resource",
			title="link to climate information",
		),
		"bs-local_class": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="soil classification based on local soil classification system",
			title="local classification",
		),
		"bs-local_class_meth": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="reference or method used in determining the local soil classification",
			title="local classification method",
		),
		"bs-microbial_biomass": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="the part of the organic matter in the soil that constitutes living microorganisms smaller than 5-10 µm. IF you keep this, you would need to have correction factors used for conversion to the final units, which should be mg C (or N)/kg soil).",
			title="microbial biomass",
		),
		"bs-microbial_biomass_meth": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="reference or method used in determining microbial biomass",
			title="microbial biomass method",
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
		"bs-ph_meth": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="reference or method used in determining pH",
			title="pH method",
		),
		"bs-pool_dna_extracts": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="were multiple DNA extractions mixed? how many?",
			title="pooling of DNA extracts",
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
		"bs-previous_land_use": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="previous land use and dates",
			title="previous land use",
		),
		"bs-previous_land_use_meth": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="reference or method used in determining previous land use and dates",
			title="previous land use method",
		),
		"bs-profile_position": Column(
			dtype="object",
			checks=Check.str_matches(r"(?i)(\W|^)(summit|shoulder|backslope|footslope|toeslope)(\W|$)"),
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="cross-sectional position in the hillslope where sample was collected.sample area position in relation to surrounding areas",
			title="profile position",
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
		"bs-salinity_meth": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="reference or method used in determining salinity",
			title="salinity method",
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
		"bs-season_precpt": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="The average of all seasonal precipitation values known, or an estimated equivalent value derived by such methods as regional indexes or Isohyetal maps",
			title="mean seasonal precipitation",
		),
		"bs-season_temp": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Mean seasonal temperature",
			title="mean seasonal temperature",
		),
		"bs-sieving": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="collection design of pooled samples and/or sieve size and amount of sample sieved",
			title="sieving",
		),
		"bs-size_frac": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Filtering pore size used in sample preparation, e.g., 0-0.22 micrometer",
			title="size fraction selected",
		),
		"bs-slope_aspect": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="the direction a slope faces. While looking down a slope use a compass to record the direction you are facing (direction or degrees); e.g., NW or 315°. This measure provides an indication of sun and wind exposure that will influence soil temperature and evapotranspiration.",
			title="slope aspect",
		),
		"bs-slope_gradient": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="commonly called “slope.” The angle between ground surface and a horizontal line (in percent). This is the direction that overland water would flow. This measure is usually taken with a hand level meter or clinometer.",
			title="slope gradient",
		),
		"bs-soil_horizon": Column(
			dtype="object",
			checks=Check.str_matches(r"(?i)(\W|^)(O horizon|A horizon|E horizon|B horizon|C horizon|R layer|Permafrost)(\W|$)"),
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="specific layer in the land area which measures parallel to the soil surface and possesses physical characteristics which differ from the layers above and beneath",
			title="soil horizon",
		),
		"bs-soil_text_measure": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="the relative proportion of different grain sizes of mineral particles in a soil, as described using a standard system; express as % sand (50 um to 2 mm), silt (2 um to 50 um), and clay (<2 um) with textural name (e.g., silty clay loam) optional.",
			title="soil texture measurement",
		),
		"bs-soil_texture_meth": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="reference or method used in determining soil texture",
			title="soil texture method",
		),
		"bs-soil_type": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="soil series name or other lower-level classification",
			title="soil type",
		),
		"bs-soil_type_meth": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="reference or method used in determining soil series name or other lower-level classification",
			title="soil type method",
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
		"bs-store_cond": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="explain how and for how long the soil sample was stored before DNA extraction.",
			title="storage conditions",
		),
		"bs-tillage": Column(
			dtype="object",
			checks=Check.str_matches(r"(?i)(\W|^)(drill|cutting disc|ridge till|strip tillage|zonal tillage|chisel|tined|mouldboard|disc plough)(\W|$)"),
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="note method(s) used for tilling",
			title="tillage",
		),
		"bs-tot_n_meth": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="reference or method used in determining the total N",
			title="total N method",
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
		"bs-tot_nitro_cont_meth": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Reference or method used in determining the total nitrogen",
			title="total nitrogen content method",
		),
		"bs-tot_org_c_meth": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="reference or method used in determining total organic C",
			title="total organic carbon method",
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
		"bs-water_content_soil_meth": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="reference or method used in determining the water content of soil",
			title="water content of soil method",
		),
	},
	checks=[
		Check(lambda df: ~(df["bs-host"].isnull() & df["bs-isolation_source"].isnull()), ignore_na = False),
	],
	index=None,
	coerce=False,
	strict="filter",
	name="biosample_package_MIUVIG.soil.6.0_schema",
	ordered=False,
	unique=None,
	report_duplicates="all",
	unique_column_names=True,
	add_missing_columns=False,
	title="BioSample package MIUVIG.soil.6.0 schema",
	description="Schema validation for BioSample database using MIUVIG.soil.6.0 package.",
)