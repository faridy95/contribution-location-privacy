import random
import xml.etree.ElementTree as ET
from xml.dom import minidom

# Définition des catégories valides (issues de ta structure JSON)
categories_dict = {
    "healthcare": ["hospital", "clinic", "social_facility", "pharmacy", "dentist", "nursing_home"],
    "religious_sites": ["place_of_worship", "place_of_mourning", "mosque", "synagogue", "temple"],
    "education": ["school", "university", "college", "kindergarten"],
    "finance": ["bank", "atm", "bureau_de_change", "money_transfer"],
    "social_services": ["social_facility", "community_centre", "welfare_office"],
    "residential": ["apartments", "house", "residential", "dormitory"],
    "transportation": ["train_station", "airport", "ferry_terminal"],
    "law_enforcement": ["police", "prison", "courthouse"],
    "government": ["townhall", "government", "embassy"],
    "shopping": ["marketplace", "mall", "department_store"]
}

# Aplatir toutes les catégories possibles
all_valid_categories = [item for sublist in categories_dict.values() for item in sublist]

# Autres paramètres possibles
stay_times = [15, 30, 45, 60, 90]
frequencies = [1, 3, 5, 7, 10, 14]
days = ["All", "Weekdays", "Weekends", "Holidays"]
time_slots = ["Morning", "Noon", "Evening", "Night"]

# Génération des règles (150)
rules = []
for _ in range(150):
    rule = {
        "category": random.choice(all_valid_categories),
        "stay_time": random.choice(stay_times),
        "frequency": random.choice(frequencies),
        "day": random.choice(days),
        "time_slot": random.choice(time_slots),
        "sensitivity": round(random.uniform(0, 1), 2)
    }
    rules.append(rule)

# Construction de la structure XML
root = ET.Element("PrivacyRules")
for rule in rules:
    rule_elem = ET.SubElement(root, "Rule")
    for key, val in rule.items():
        child = ET.SubElement(rule_elem, key)
        child.text = str(val)

# Formattage du XML avec indentation
xml_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="  ")

# Sauvegarde dans un fichier
output_path = "privacy_rules_no_obfuscation.xml"
with open(output_path, "w") as f:
    f.write(xml_str)
print(f"XML file privacy rules generated: {output_path}")
