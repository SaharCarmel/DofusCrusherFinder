import pandas as pd
import json

f = open("data/dofus/allequipments.json", "r")
jsonData = json.load(f)
translator = {
    "Name": "name",
    "type": "type",
    "url": "url",
    "lvl": "lvl",
    "Vitalité": "Vitality",
    "Sagesse": "Wisdom",
    "Force": "Strength",
    "Intelligence": "Intelligence",
    "Chance": "Chance",
    "Agilité": "Agility",
    "Puissance": "Power",
    "PA": "AP",
    "PM": "MP",
    "Portée": "Range",
    "Invocations": "Summon",
    "Coups Critiques": "Critical Hit",
    "Initiative": "Initiative",
    "Prospection": "Prospection",
    "Tacle": "Lock",
    "Fuite": "Dodge",
    "Retrait PA": "AP Reduction",
    "Retrait PM": "MP Reduction",
    "Esquive PA": "AP Res",
    "Esquive PM": "MP Res",
    "Résistance Poussée": "Push Res.",
    "Résistance Critiques": "Crit. Res",
    "Pods": "Pods",
    "Dommages Pièges": "Trap Damage",
    "Puissance (pièges)": "%Trap Dam",
    "Dommages": "Damage",
    "Dommages Neutre": "Neutral Damage",
    "Dommages Terre": "Earth Damage",
    "Dommages Feu": "Fire Damage",
    "Dommages Eau": "Water Damage",
    "Dommages Air": "Air Damage",
    "Dommages Critiques": "Crit. Damage",
    "Dommages Poussée": "Push Damage",
    "Soins": "Heal",
    "Résistance Neutre": "Neutral Res.",
    "Résistance Terre": "Earth Res.",
    "Résistance Feu": "Fire Res.",
    "Résistance Eau": "Water Res.",
    "Résistance Air": "Air Res.",
    "% Résistance Neutre": "%Neutral Res",
    "% Résistance Terre": "%Earth Res",
    "% Résistance Feu": "%Fire Res",
    "% Résistance Eau": "%Water Res",
    "% Résistance Air": "%Air Res",
    "% Critique": "Critical Hit",
    "% Résistance mêlée": "%Melee Res",
    "% Résistance distance": "%Range Res",

}
len(jsonData)
df = pd.DataFrame(index=range(len(jsonData)),columns=list(translator.values()))
for i, item in enumerate(jsonData):
    stats = item["stats"]
    df.iloc[i]["name"] = item["name"]
    df.iloc[i]["type"] = item["type"]
    df.iloc[i]["url"] = item["url"]
    df.iloc[i]["lvl"] = item["lvl"]
    for stat in stats:
        statValue = list(stat.keys())
        try:
            translated = translator[statValue[0]]
            mean = stat[statValue[0]]['from']
            df.iloc[i][translated] = mean
        except KeyError:
            pass
        
df.to_csv("data/dofus/equipments.csv", index=False)