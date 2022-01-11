import pandas as pd


class Finder:
    def __init__(self, parameter, df, sinkValues) -> None:
        self.parameter = parameter
        self.df = df
        self.sink_values = sinkValues
        self.grade_df()

    def grade_df(self):
        df['grade'] = self.df.apply(self.grade_item, axis=1)
        df.to_csv("calculated.csv")
        pass

    
    
    def grade_item(self, parameterDict):
        parameterDict = parameterDict[list(self.sink_values.keys())]
        parameterDict = parameterDict.dropna()
        sum = 0
        included = False
        for key in parameterDict.keys():
            
            if key == self.parameter:
                sum += int(parameterDict[key])*float(sinkValues[key])
                included = True
            else:
                sum += int(parameterDict[key])*float(sinkValues[key])*0.5
        if not included:
            sum = 0
        return sum


sinkValues = {
    "Ap": "100",
    "Mp": "90",
    "Range": "51",
    "Summon": "30",
    "Critical Hit": "10",
    "Heal": "10",
    "%Fire Res": "6",
    "%Air Res": "6",
    "%Water Res": "6",
    "%Neutral Res": "6",
    "%Earth Res": "6",
    "Ap Res": "7",
    "Mp Res": "7",
    "Ap Red": "7",
    "Mp Red": "7",
    "Lock": "4",
    "Dodge": "4",
    "Damage": "20",
    "Air Damage": "5",
    "Earth Damage": "5",
    "Neutral Damage": "5",
    "Push Damage": "10",
    "Fire Damage": "5",
    "Water Damage": "5",
    "Crit. Damage": "10",
    "Trap Damage": "15",
    "Damage Refl.": "30",
    "Crit. Res": "10",
    "Push Res.": "10",
    "Earth Res.": "2",
    "Neutral Res.": "2",
    "Fire Res.": "2",
    "Air Res.": "2",
    "Water Res.": "2",
    "%Trap Dam": "2",
    "Power": "2",
    "Wisdom": "3",
    "Prospection": "3",
    "Strength": "1",
    "Agility": "1",
    "Intelligence": "1",
    "Pod": "0.25",
    "Initiative": "0.1",
    "Chance": "1",
    "Vitality": "0.2",
}


df = pd.read_csv('equipments.csv')
df.insert(0, 'grade', 0)
notRelevantCols = ["name", "type", "url", "lvl"]
finder = Finder(parameter="Strength", df=df, sinkValues=sinkValues)
# dict11 = {
#     "Strength": "50",
#     "Intelligence": "50",
#     "Vitality": "100",
# }

# finder.grade_item(dict11)
