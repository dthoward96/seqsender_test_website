from pandera import DataFrameSchema, Column, Check, Index, MultiIndex

schema = DataFrameSchema(
	columns={
		"bs-collected_by": Column(
			dtype="object",
			checks=None,
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="Name of persons or institute who collected the sample",
			title="collected by",
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
		"bs-isolation_source": Column(
			dtype="object",
			checks=None,
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="Describes the physical, environmental and/or local geographical source of the biological sample from which the sample was derived.",
			title="isolation source",
		),
		"bs-purpose_of_sampling": Column(
			dtype="object",
			checks=None,
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="the reason that the sample was collected, e.g., active surveillance in response to an outbreak, active surveillance not initiated by an outbreak, clinical trial, cluster investigation, environmental assessment, farm sample, field trial, for cause, industry internal investigation, market sample, passive surveillance, population based studies, research, research and development",
			title="purpose of sampling",
		),
		"bs-source_type": Column(
			dtype="object",
			checks=Check.str_matches(r"(?i)(\W|^)(human|animal|food|environmental|other|missing|not applicable|not collected|not provided|restricted access)(\W|$)"),
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="Controlled vocabulary describing the isolation_source.  Choose the best fit term: Human, Animal, Food, Environmental, Other, e.g., Food",
			title="source type",
		),
		"bs-strain": Column(
			dtype="object",
			checks=None,
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="microbial or eukaryotic strain name",
			title="strain",
		),
		"bs-animal_env": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="The environment from which the animal sample was taken, e.g., veterinary clinic",
			title="animal environment",
		),
		"bs-animal_intrusion": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Identification of animals intruding on the sample or sample site including invertebrates (such as pests or pollinators) and vertebrates (such as wildlife or domesticated animals). This field encourages terms under organism (http://purl.obolibrary.org/obo/NCIT_C14250). This field also encourages identification numbers from NCBI under https://www.ncbi.nlm.nih.gov/taxonomy. Multiple terms can be separated by pipes, e.g., large flies",
			title="animal intrusion near sample source",
		),
		"bs-biocide_used": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Substance intended for preventing, neutralizing, destroying, repelling, or mitigating the effects of any pest or microorganism; that inhibits the growth, reproduction, and activity of organisms, including fungal cells; decreases the number of fungi or pests present; deters microbial growth and degradation of other ingredients in the formulation. Indicate the biocide used on the location where the sample was taken. Multiple terms can be separated by pipes, e.g., Quaternary ammonium compound|SterBac",
			title="biocide used",
		),
		"bs-building_setting": Column(
			dtype="object",
			checks=Check.str_matches(r"(?i)(\W|^)(urban|suburban|exurban|rural|missing|not applicable|not collected|not provided|restricted access)(\W|$)"),
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="location (geography) where a building is set",
			title="building setting",
		),
		"bs-coll_site_geo_feat": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Text or terms that describe the geographic feature where the food sample was obtained by the researcher. This field encourages selected terms listed under the following ontologies: anthropogenic geographic feature (http://purl.obolibrary.org/obo/ENVO_00000002), for example agricultural fairground [ENVO:01000986]; garden [ENVO:00000011} or any of its subclasses; market [ENVO:01000987]; water well [ENVO:01000002]; or human construction (http://purl.obolibrary.org/obo/ENVO_00000070), e.g., grocery store [GENEPIO:0001020]",
			title="collection site geographic feature",
		),
		"bs-cult_isol_date": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="A culture isolation date is a date-time entity marking the end of a process in which a sample yields a positive result for the target microbial analyte(s) in the form of an isolated colony or colonies, e.g., 5/24/2020",
			title="culture isolation date",
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
		"bs-env_broad_scale": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Add terms that identify the major environment type(s) where your sample was collected. Recommend subclasses of biome [ENVO:00000428]. Multiple terms can be separated by one or more pipes e.g.: Â mangrove biome [ENVO:01000181]|estuarine biome [ENVO:01000020]",
			title="broad-scale environmental context",
		),
		"bs-env_local_scale": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Add terms that identify environmental entities having causal influences upon the entity at time of sampling, multiple terms can be separated by pipes, e.g.: Â shoreline [ENVO:00000486]|intertidal zone [ENVO:00000316]",
			title="local-scale environmental context",
		),
		"bs-env_medium": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Add terms that identify the material displaced by the entity at time of sampling. Recommend subclasses of environmental material [ENVO:00010483]. Multiple terms can be separated by pipes e.g.: estuarine water [ENVO:01000301]|estuarine mud [ENVO:00002160]",
			title="environmental medium",
		),
		"bs-env_monitoring_zone": Column(
			dtype="object",
			checks=Check.str_matches(r"(?i)(\W|^)(Zone 1|Zone 2|Zone 3|Zone 4|missing|not applicable|not collected|not provided|restricted access)(\W|$)"),
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="An environmental monitoring zone is a formal designation as part of an environmental monitoring program, in which areas of a food production facility are categorized, commonly as zones 1-4, based on likelihood or risk of foodborne pathogen contamination. This field accepts entries of zones 1-4, e.g., Zone 1",
			title="food production environmental monitoring zone",
		),
		"bs-extr_weather_event": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Unusual weather events that may have affected microbial populations. Multiple terms can be separated by pipes, listed in reverse chronological order, e.g., hail",
			title="extreme weather event",
		),
		"bs-facility_type": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Establishment details about the type of facility where the sample was taken. This is independent of the specific product(s) within the facility, e.g., manufacturing-processing",
			title="facility type",
		),
		"bs-farm_equip": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="List of relevant equipment used for planting, fertilization, harvesting, irrigation, land levelling, residue management, weeding or transplanting during the growing season.  This field encourages terms listed under agricultural implement (http://purl.obolibrary.org/obo/AGRO_00000416). Multiple terms can be separated by pipes, e.g., combine harvester [AGRO:00000473]",
			title="farm equipment used",
		),
		"bs-farm_water_source": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Source of water used on the farm for irrigation of crops or watering of livestock, e.g., water well",
			title="farm watering water source",
		),
		"bs-fertilizer_admin": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Type of fertilizer or amendment added to the soil or water for the purpose of improving substrate health and quality for plant growth. This field encourages terms listed under agronomic fertilizer (http://purl.obolibrary.org/obo/AGRO_00002062). Multiple terms may apply and can be separated by pipes, listing in reverse chronological order, e.g., fish emulsion [AGRO:00000082]",
			title="fertilizer administration",
		),
		"bs-food_additive": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="A substance or substances added to food to maintain or improve safety and freshness, to improve or maintain nutritional value, or improve taste, texture and appearance.  This field encourages terms listed under food additive (http://purl.obolibrary.org/obo/FOODON_03412972). Multiple terms can be separated by one or more pipes, but please consider limiting this list to the top 5 ingredients listed in order as on the food label.  See also, https://www.fda.gov/food/food-ingredients-packaging/overview-food-ingredients-additives-colors, e.g., xanthan gum [FOODON:03413321]",
			title="food additive",
		),
		"bs-food_clean_proc": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="The process of cleaning food to separate other environmental materials from the food source. Multiple terms can be separated by pipes, e.g., rinsed with water|scrubbed with brush",
			title="food cleaning process",
		),
		"bs-food_contact_surf": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="The specific container or coating materials in direct contact with the food. Multiple values can be assigned.  This field encourages terms listed under food contact surface (http://purl.obolibrary.org/obo/FOODON_03500010), e.g., aluminum surface [FOODON:03500042]",
			title="food contact surface",
		),
		"bs-food_contain_wrap": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Type of container or wrapping defined by the main container material, the container form, and the material of the liner lids or ends. Also type of container or wrapping by form; prefer description by material first, then by form. This field encourages terms listed under food container or wrapping (http://purl.obolibrary.org/obo/FOODON_03490100), e.g., bottle or jar [FOODON:03490203]",
			title="food container or wrapping",
		),
		"bs-food_industry_class": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="The US FDA Class is the second of five elements that comprise a FDA product code. This element is directly related to an Industry and designates the food group, source, product, use, pharmacological action, category or animal species of the product. A Class code is more specific than an Industry; for example, the Fishery/Seafood products Industry may contain Classes such as Smoked, Breaded and such, e.g., Coffee, Decaffeinated",
			title="FDA food industry class name",
		),
		"bs-food_industry_code": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="The US FDA Industry Code is the first of five elements that comprise an FDA product code. An Industry code determines the broadest area into which a product falls, e.g., 31 Coffee and Tea",
			title="FDA food industry code name",
		),
		"bs-food_origin": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="A reference to a place on the Earth, by its name or by its geographical location that describes the origin of the food commodity, either in terms of its cultivation or production. This field encourages terms listed under geographic location (http://purl.obolibrary.org/obo/GAZ_00000448), e.g., Thailand",
			title="food product origin geographic location",
		),
		"bs-food_pack_integrity": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="A term label and term id to describe the state of the packing material and text to explain the exact condition.  This field encourages terms listed under food packing medium integrity (http://purl.obolibrary.org/obo/FOODON_03530218), e.g., food packing medium compromised [FOODON:00002517]",
			title="food packing integrity",
		),
		"bs-food_pack_medium": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="The medium in which the food is packed for preservation and handling or the medium surrounding homemade foods, e.g., peaches cooked in sugar syrup. The packing medium may provide a controlled environment for the food. It may also serve to improve palatability and consumer appeal. This includes edible packing media (e.g. fruit juice), gas other than air (e.g. carbon dioxide), vacuum packed, or packed with aerosol propellant. This field encourages terms under food packing medium (http://purl.obolibrary.org/obo/FOODON_03480020). Multiple terms may apply and can be separated by pipes, e.g., vacuum-packed [FOODON:03480027]",
			title="food packing medium",
		),
		"bs-food_preserv_proc": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="The methods contributing to the prevention or retardation of microbial, enzymatic or oxidative spoilage and thus to the extension of shelf life. This field encourages terms listed under food preservation process (http://purl.obolibrary.org/obo/FOODON_03470107), e.g., food fermentation [FOODON:00001304]",
			title="food preservation process",
		),
		"bs-food_processing_method": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Methods for processing food, e.g., food (blanched) [FOODON:00002767]",
			title="food processing method",
		),
		"bs-food_prod": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Descriptors of the food production system or of the agricultural environment and growing conditions related to the farm production system. This field encourages terms listed under food production (http://purl.obolibrary.org/obo/FOODON_03530206). Multiple terms may apply and can be separated by pipes, e.g., restaurant food preparation process [FOODON:03530110]",
			title="food production system",
		),
		"bs-food_prod_synonym": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Other names by which the food product is known by (e.g., regional or non-English names), e.g., pinot gris",
			title="food product synonym",
		),
		"bs-food_product_type": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="A food product type is a class of food products that is differentiated by its food composition (e.g., single- or multi-ingredient), processing and/or consumption characteristics. This does not include brand name products but it may include generic food dish categories. This field encourages terms under food product type (http://purl.obolibrary.org/obo/FOODON:03400361). For terms related to food product for an animal, consult food product for animal (http://purl.obolibrary.org/obo/FOODON_03309997). If the proper descriptor is not listed please use text to describe the food type. Multiple terms can be separated by one or more pipes, e.g., multi-component food product [FOODON:00002501]",
			title="food product type",
		),
		"bs-food_quality_date": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="The date recommended for the use of the product while at peak quality, this date is not a reflection of safety unless used on infant formula this date is not a reflection of safety and is typically labeled on a food product as \"\"best if used by,\"\" best by,\"\" \"\"use by,\"\" or \"\"freeze by\"\", e.g., 5/24/2020",
			title="food quality date",
		),
		"bs-food_source": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Individual organism or category of organisms from which the food product or its major ingredient is derived, e.g., giant tiger prawn [FOODON:03412612]",
			title="food source",
		),
		"bs-food_type_processed": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Food type processed in facility, e.g., dairy",
			title="food type processed in facility",
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
		"bs-host_am": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="The class(es) or name(s) (generic or brand) of the antimicrobial(s) given to the food animal within the last 30 days, e.g., tetracycline [CHEBI:27902]",
			title="antimicrobial name",
		),
		"bs-host_animal_breed": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="The animal breed of the host organism.  Used mainly for animal hosts, e.g., duroc, angus, mixed breed",
			title="host animal breed",
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
		"bs-host_group_size": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="The number of food animals of the same species that are maintained together as a unit, i.e. a herd or flock, e.g., 80",
			title="food animal group size",
		),
		"bs-host_housing": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Description of the housing system of the livestock. This field encourages terms listed under terrestrial management housing system (http://opendata.inra.fr/EOL/EOL_0001605), e.g., pen [EOL:0001902]",
			title="animal housing system",
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
		"bs-host_variety": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="The variety or cultivar of the host organism; the name given to a particular variety of organism to distinguish it from otherwise similar organisms of the same species, e.g., romaine lettuce; Athena melons; Patio Snacker cucumbers",
			title="host variety or cultivar",
		),
		"bs-ifsac_category": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="The IFSAC food categorization scheme has five distinct levels to which foods can be assigned, depending upon the type of food. First, foods are assigned to one of four food groups (aquatic animals, land animals, plants, and other). Food groups include increasingly specific food categories; dairy, eggs, meat and poultry, and game are in the land animal food group, and the category meat and poultry is further subdivided into more specific categories of meat (beef, pork, other meat) and poultry (chicken, turkey, other poultry). Finally, foods are differentiated by differences in food processing (such as pasteurized fluid dairy products, unpasteurized fluid dairy products, pasteurized solid and semi-solid dairy products, and unpasteurized solid and semi-solid dairy products. An IFSAC food category chart is available from https://www.cdc.gov/foodsafety/ifsac/projects/food-categorization-scheme.html PMID: 28926300, e.g., Plants:Produce:Vegetables:Herbs:Dried Herbs",
			title="Interagency Food Safety Analytics Collaboration (IFSAC) category",
		),
		"bs-indoor_surf": Column(
			dtype="object",
			checks=Check.str_matches(r"(?i)(\W|^)(counter top|window|wall|cabinet|ceiling|door|shelving|vent cover|missing|not applicable|not collected|not provided|restricted access)(\W|$)"),
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="type of indoor surface",
			title="indoor surface",
		),
		"bs-indoor_surf_subpart": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="The subpart of the object(s) that was swabbed, like a cart, drain, counter, etc., e.g., wheel",
			title="indoor sampling surface or structure subpart",
		),
		"bs-intended_consumer": Column(
			dtype="object",
			checks=Check.str_matches(r"(?i)(\W|^)(human as food consumer|animal as food consumer|missing|not applicable|not collected|not provided|restricted access)(\W|$)"),
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Food consumer type, human or animal, for which the food product is produced and marketed, e.g., human",
			title="intended consumer",
		),
		"bs-isolate_name_alias": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Other IDs associated with this isolate or strain. Separate with '; ' if more than one",
			title="isolate name alias",
		),
		"bs-label_claims": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Descriptors of the food production system such as wild caught, free-range, organic, free-range, industrial, hormone-free, antibiotic free, cage free, e.g., wild caught",
			title="labeling claims",
		),
		"bs-lat_lon": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="The geographical coordinates of the location where the sample was collected. Specify as degrees latitude and longitude in format \"d[d.dddd] N|S d[dd.dddd] W|E\", eg, 38.98 N 77.11 W",
			title="latitude and longitude",
		),
		"bs-location_in_facility": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Name of the location or room in the facility where the sampling occurred, e.g., ripening room",
			title="location or room in facility",
		),
		"bs-material_condition": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Condition of material sampled, e.g., rusted",
			title="material condition",
		),
		"bs-mechanical_damage": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="information about any mechanical damage exerted on the plant; can include multiple damages and sites",
			title="mechanical damage",
		),
		"bs-plant_growth_med": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Type of the media used for growing sampled plants, e.g., soil [ENVO:00001998]",
			title="plant growth medium",
		),
		"bs-plant_water_method": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Description of the equipment or method used to distribute water to crops. This field encourages terms listed under irrigation process (http://purl.obolibrary.org/obo/AGRO_00000006). Multiple terms can be separated by pipes, e.g., drip irrigation process [AGRO:00000056]",
			title="plant water delivery method",
		),
		"bs-project_name": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="A concise name that describes the overall project, for example \"Analysis of sequences collected from Antarctic soil\"",
			title="project name",
		),
		"bs-reference_material": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Indicates that a standards body or external group asserts this sample is reference material, eg, 'NIST reference material for genome sequencing validation'.",
			title="reference material",
		),
		"bs-rel_location": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Location of sample to other parts of the farm, e.g. under crop plant, near irrigation ditch, from the dirt road, from air above crops, nearby river, e.g., furrow",
			title="relative location of sample",
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
		"bs-sanitizer_used_postharvest": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Substance intended for preventing, neutralizing, destroying, repelling, or mitigating the effects of any pest or microorganism; indicate the sanitizer used during the postharvest cleaning process. Multiple terms can be separated by pipes, e.g., chlorine bleach",
			title="sanitizer used during postharvest cleaning",
		),
		"bs-sequenced_by": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="The name of the agency that generated the sequence, e.g., Centers for Disease Control and Prevention",
			title="sequenced by",
		),
		"bs-serotype": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Taxonomy below subspecies; a variety (in bacteria, fungi or virus) usually based on its antigenic properties. Same as serovar and serogroup. e.g. serotype=\"H1N1\" in Influenza A virus CY098518.",
			title="serotype",
		),
		"bs-serovar": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Taxonomy below subspecies; a variety (in bacteria, fungi or virus) usually based on its antigenic properties. Same as serovar and serotype. Sometimes used as species identifier in bacteria with shaky taxonomy, e.g. Leptospira, serovar saopaolo S76607 (65357 in Entrez).",
			title="serovar",
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
		"bs-spec_intended_cons": Column(
			dtype="object",
			checks=Check.str_matches(r"(?i)(\W|^)(animal as food consumer|laboratory animal as food consumer|non-food animal as food consumer|pet animal as consumer|pet fish as consumer|pet cat as consumer|pet bird as consumer|pet dog as consumer|sheep or goat as consumer|food animal as consumer|food fish as consumer|poultry as consumer|pig as consumer|game as consumer|rabbit as consumer|cattle as consumer|horse as consumer|human as food consumer|adult human as food consumer|man as food consumer|woman as food consumer|senior as food consumer|athlete as food consumer|bodybuilder as food consumer|weight-reducer as food consumer|human as food consumer, four years and above|teenager as food consumer|child as food consumer, less than four years|infant or toddler as food consumer|toddler as food consumer, 12 months and onwards|infant as food consumer|missing|not applicable|not collected|not provided|restricted access)(\W|$)"),
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Food consumer type, human or animal, for which the food product is produced and marketed. This field encourages terms listed under food consumer group (http://purl.obolibrary.org/obo/FOODON_03510136), e.g., infant or toddler as food consumer [FOODON:03510020]",
			title="specific intended consumer",
		),
		"bs-surf_material": Column(
			dtype="object",
			checks=Check.str_matches(r"(?i)(\W|^)(concrete|wood|stone|tile|plastic|glass|vinyl|metal|carpet|stainless steel|paint|cinder blocks|hay bales|stucco|adobe|missing|not applicable|not collected|not provided|restricted access)(\W|$)"),
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="surface materials at the point of sampling",
			title="surface material",
		),
		"bs-surf_temp": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="temperature of the surface at the time of sampling",
			title="surface temperature",
		),
		"bs-surface_orientation": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Describe which surface of the object is swabbed. (e.g underside, top, corner), e.g., underside",
			title="surface orientation",
		),
		"bs-upstream_intervention": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="List any known health-related interventions (prophylactic, therapeutic, and/or metaphylactic) administered to the host, i.e. vaccinations, hormonal patches, antibiotics, injections in feed, etc., e.g., prophylactic/metaphylactic antibiotics",
			title="upstream intervention",
		),
	},
	checks=None,
	index=None,
	dtype=None,
	coerce=False,
	strict="filter",
	name="biosample_package_OneHealthEnteric.1.0_schema",
	ordered=False,
	unique=None,
	report_duplicates="all",
	unique_column_names=True,
	add_missing_columns=False,
	itle="BioSample package OneHealthEnteric.1.0 schema",
	description="Schema validation for BioSample database using OneHealthEnteric.1.0 package.",
)