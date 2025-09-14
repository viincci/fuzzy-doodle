PRIORITY_PLANTS = ["""Priority rare South African plants for automated article generation"""

    {

        "common_name": "Conophytum bilobum",PRIORITY_PLANTS = [

        "scientific_name": "Conophytum bilobum",    {

        "type": "Dwarf Succulent",        "common_name": "Conophytum bilobum",

        "conservation_status": "Critically Endangered",        "scientific_name": "Conophytum bilobum",

        "trade_status": "Legal via propagation",        "category": "Dwarf Succulents",

        "description": "Tiny, pebble-like succulent with fused leaves",        "conservation_status": "Critically Endangered",

        "region": "Northern Cape",        "trade_status": "CITES Appendix III",

        "export_notes": "Requires CITES permit"        "description": "Tiny, pebble-like succulent with fused leaves, highly sought after by collectors.",

    },        "habitat": "Succulent Karoo"

    {    },

        "common_name": "Conophytum minimum",    {

        "scientific_name": "Conophytum minimum",        "common_name": "Conophytum minimum",

        "type": "Dwarf Succulent",        "scientific_name": "Conophytum minimum",

        "conservation_status": "Critically Endangered",        "category": "Dwarf Succulents",

        "trade_status": "Legal via propagation",        "conservation_status": "Critically Endangered",

        "description": "Miniature succulent with unique stone-like appearance",        "trade_status": "CITES Appendix III",

        "region": "Northern Cape",        "description": "One of the smallest succulent species, forming tiny clusters.",

        "export_notes": "Requires CITES permit"        "habitat": "Succulent Karoo"

    },    },

    {    {

        "common_name": "Crassothonna clavifolia",        "common_name": "Club-leaved Crassothonna",

        "scientific_name": "Crassothonna clavifolia",        "scientific_name": "Crassothonna clavifolia",

        "type": "Succulent",        "category": "Dwarf Succulents",

        "conservation_status": "Least Concern",        "conservation_status": "Least Concern",

        "trade_status": "Legal",        "trade_status": "Non-threatened",

        "description": "Club-shaped leaves, adapted to quartz fields",        "description": "Club-shaped leaves adapted to quartz fields, rare in trade.",

        "region": "Gauteng",        "habitat": "Quartz fields"

        "export_notes": "Straightforward export as non-threatened"    },

    },    {

    {        "common_name": "Dwarf Spekboom",

        "common_name": "Portulacaria pygmaea",        "scientific_name": "Portulacaria pygmaea",

        "scientific_name": "Portulacaria pygmaea",        "category": "Dwarf Succulents",

        "type": "Dwarf Succulent",        "conservation_status": "Endangered",

        "conservation_status": "Endangered",        "trade_status": "Legal if propagated",

        "trade_status": "Legal if propagated",        "description": "Dwarf, bonsai-like plant with woody caudex.",

        "description": "Dwarf, bonsai-like with woody caudex",        "habitat": "Western Cape"

        "region": "Western Cape",    },

        "export_notes": "Legal for propagated specimens"    {

    },        "common_name": "Othonna armiana",

    {        "scientific_name": "Othonna armiana",

        "common_name": "Cape Sundew",        "category": "Specialized Caudiciforms",

        "scientific_name": "Drosera capensis",        "conservation_status": "Critically Endangered",

        "type": "Carnivorous Plant",        "trade_status": "CITES",

        "conservation_status": "Least Concern",        "description": "Flat-topped caudex with daisy-like flowers.",

        "trade_status": "Legal",        "habitat": "Northern Cape"

        "description": "Sticky-leaved, easy-to-grow carnivorous plant",    },

        "region": "Western Cape",    {

        "export_notes": "Export-friendly as non-threatened"        "common_name": "Tylecodon bodleyae",

    },        "scientific_name": "Tylecodon bodleyae",

    {        "category": "Specialized Caudiciforms",

        "common_name": "King Protea",        "conservation_status": "Critically Endangered",

        "scientific_name": "Protea cynaroides",        "trade_status": "CITES",

        "type": "Shrub",        "description": "Dwarf with swollen caudex, cliff-dwelling species.",

        "conservation_status": "Least Concern",        "habitat": "Cliff faces"

        "trade_status": "Legal",    },

        "description": "National flower, large blooms with rare color variants",    {

        "region": "Western Cape",        "common_name": "Cape Sundew",

        "export_notes": "Export legal for grown stock"        "scientific_name": "Drosera capensis",

    },        "category": "Carnivorous Plants",

    {        "conservation_status": "Least Concern",

        "common_name": "Red Disa",        "trade_status": "Non-threatened",

        "scientific_name": "Disa uniflora",        "description": "Sticky-leaved carnivorous plant, easy to grow.",

        "type": "Terrestrial Orchid",        "habitat": "Western Cape"

        "conservation_status": "Protected",    },

        "trade_status": "Legal for nursery hybrids",    {

        "description": "Iconic waterfall orchid with striking red flowers",        "common_name": "Roridula gorgonias",

        "region": "Cape Peninsula",        "scientific_name": "Roridula gorgonias",

        "export_notes": "Export requires permits"        "category": "Carnivorous Plants",

    }        "conservation_status": "Rare",

]        "trade_status": "Legal if certified",

        "description": "Proto-carnivorous shrub with resin-trapping leaves.",

def get_priority_plant(plant_name):        "habitat": "Endemic to South Africa"

    """    },

    Get priority plant information by name (common or scientific)    {

    """        "common_name": "King Sundew",

    plant_name = plant_name.lower()        "scientific_name": "Drosera regia",

    for plant in PRIORITY_PLANTS:        "category": "Carnivorous Plants",

        if plant_name in plant['common_name'].lower() or plant_name in plant['scientific_name'].lower():        "conservation_status": "Vulnerable",

            return plant        "trade_status": "Legal if propagated",

    return None        "description": "Large, dramatic carnivorous leaves.",

        "habitat": "KwaZulu-Natal"

def get_all_priority_plants():    },

    """    {

    Get list of all priority plants        "common_name": "Red Disa",

    """        "scientific_name": "Disa uniflora",

    return PRIORITY_PLANTS        "category": "Terrestrial Orchids",
        "conservation_status": "Protected",
        "trade_status": "Legal with permits",
        "description": "Iconic waterfall orchid with striking red flowers.",
        "habitat": "Cape fynbos"
    },
    {
        "common_name": "King Protea",
        "scientific_name": "Protea cynaroides",
        "category": "Proteas",
        "conservation_status": "Least Concern",
        "trade_status": "Legal",
        "description": "South Africa's national flower with large, striking blooms.",
        "habitat": "Fynbos regions"
    },
    {
        "common_name": "King Fern",
        "scientific_name": "Todea barbara",
        "category": "Ferns",
        "conservation_status": "Least Concern",
        "trade_status": "Non-restricted",
        "description": "Ancient, tree-like fern species.",
        "habitat": "Eastern Cape"
    }
]