import pandas as pd
import json
import ast
import numpy as np
import matplotlib.pyplot as plt

###Read in data
champ_stat = pd.read_csv('champStat.csv')
champ_abilities = pd.read_csv('champAbilities.csv')
item_set = pd.read_csv('item.csv')

###All the information about the information is stored in the class
###Different functions store different information
###Champion contains base stats, spells and items


class Champion:

    def __init__(self, champ_name, level):
        self.champ_name = champ_name
        self.level = level
        self.items = []

    ###Input: Champion name and level
    ###Type: String and character
    ###Output: One row containing information
    ###Type: dataframe

    def base_stat(self):
        ###Get champ information from the dataframe
        champ_info = champ_stat.loc[champ_stat['Champions'] == self.champ_name]
        champ_info = champ_info.iloc[:, 1:len(champ_info.columns)]

        ###Stat that scales with level
        per_level = champ_info[['armorperlevel', 'attackdamageperlevel', 'attackspeedperlevel',
                                'hpperlevel', 'hpregenperlevel', 'mpperlevel', 'mpregenperlevel',
                                'spellblockperlevel']]

        per_level = per_level * self.level

        ###Stat based on level
        stat = champ_info[['armor', 'attackdamage', 'attackspeed',
                           'hp', 'hpregen', 'mp', 'mpregen',
                           'spellblock']]

        ###base stat + scaling stat
        for i in range(0, len(stat.columns)):
            stat[stat.columns[i]] = per_level[per_level.columns[i]] + stat[stat.columns[i]]

        ###Change into loc later
        stat['atttackrange'] = champ_info.loc[:, 'attackrange']
        stat['movespeed'] = champ_info.loc[:, 'movespeed']

        return stat

    ###Input: item name
    ###Type: character
    ###Output: List of items
    ###Output: List

    def add_item(self, item):
        self.items.append(item)

    def item_stat(self):
        item_value = []
        for i in range(0, len(self.items)):

            item_info = item_set.loc[item_set['name'] == self.items[i]]
            stats = item_info.iloc[0]['stats']
            if not stats == '{}':
                stats = json.loads(repr(stats))

                ###str to dict so we can catch the
                stats = ast.literal_eval(stats)

                ###Get the label and the value out of the converted json file
                for label, value in stats.items():
                    item_value.append([item_info.iloc[0]['name'], label, value])
        print(item_value)


###Get the types of items
item_type = []
for i in range(0, len(item_set.index)):
    item_stats = item_set.iloc[i]['stats']
    if not item_stats == '{}':
        item_stats = json.loads(repr(item_stats))

        ###str to dict so we can catch the
        item_stats = ast.literal_eval(item_stats)

        ###Get the label and the value out of the converted json file
        for l, v in item_stats.items():
            item_type.append([l, v])

###Sort list
item_type.sort()

###Extract the type from list
#item_type = [types[0] for types in item_type]
item_type = list(zip(*item_type))[0]

###Unique types only
###In total 12 variables
item_type = list(set(item_type))
print(item_type)

aatrox = Champion('Aatrox', 2)
aatrox.base_stat()
print(aatrox.base_stat())
###All items
for i in range(0, int(len(item_set.index)/2)):
    item_name = item_set.loc[i, 'name']
    aatrox.add_item(item_name)
print(aatrox.items)
aatrox.item_stat()

