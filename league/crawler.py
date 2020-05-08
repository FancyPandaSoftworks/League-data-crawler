###Libraries
import json
import urllib.request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#######################################Get patch#######################################
###Get the latest patch
with urllib.request.urlopen("https://ddragon.leagueoflegends.com/api/versions.json") as url:
    patchVersion = json.loads(url.read().decode())
    print(patchVersion[0])

latestPatch = patchVersion[0]


#######################################Get items#######################################
with urllib.request.urlopen(
        "http://ddragon.leagueoflegends.com/cdn/" + latestPatch + "/data/en_US/item.json") as url:
    items = json.loads(url.read().decode())
    data = items['data']

item_df = pd.DataFrame()

###Crawl through every item id
item_list = []
for i in range(1001, 3917):
    item_id = str(i)
    item = data.get(item_id, {})
    if item:
        ###Information of the items
        item_name = item['name']
        item_descr = item['description']
        item_text = item['plaintext']
        item_tags = item['tags']
        item_gold = item['gold']
        item_stats = item['stats']
        item_effect = item.get('effect', {})

        ###All the information in a list
        item_info = [item_name, item_descr, item_text, item_tags, item_gold, item_stats, item_effect]

        ###Put that item into a collective list
        item_list.append(item_info)

###turn the list into a dataframe
item_df = pd.DataFrame(item_list, columns=['name', 'description', 'plaintext', 'tags', 'gold',
                                           'stats', 'effect'])

###Clean data
###Data: there is still information missingin some columns as well as having too much items that are not useful
###Transformations and modifications:
###Add information to stats where its necessary, and remove items like trinkets and vision items according to tags

###Write the dataframe to a csv
item_df.to_csv('item.csv')

##################################Get champion base stat##################################

###get the champion stats from the latest patch
with urllib.request.urlopen(
        "http://ddragon.leagueoflegends.com/cdn/" + latestPatch + "/data/en_US/champion.json") as url:
    champs = json.loads(url.read().decode())
    # print(champStat)

###Get the base numbers of the champs from the json file
champStat = pd.DataFrame()
champName = pd.DataFrame()
for i in champs['data']:
    stats = champs['data'][i]['stats']

    ###Add the values to the dataframes
    champStat = champStat.append(stats, ignore_index=True)
    champName = champName.append([i], ignore_index=True)

champName = champName.set_axis(['Champions'], axis=1, inplace=False)
# print(champName)

###Combine the two dataframe
champStat = pd.concat([champName.reset_index(drop=True), champStat], axis=1)

champStat.to_csv('champStat.csv')






#######################################Get champion spells#######################################
###get champion stats from the latest patch
###What we theoretically need to get:
###base damage
###ratio
###scales with ad/ap/health/etc
###Range
###Increased damage
###CC
###Interval between the spells


with urllib.request.urlopen("https://cdn.merakianalytics.com/riot/lol/resources/latest/en-US/champions.json") as url:
    champions = json.loads(url.read().decode())


def abilities(button, champ):
    # print(button)
    spell = champions[champ].get('abilities', {}).get(button, None)
    if not spell and button == 'Q':
        ###WHY GNAR IS Q2 AND NOT JUST Q ???????
        spell = champions[champ].get('abilities', {}).get('Q2', None)
    ###Description of the ability
    descr = spell[0]['effects']

    ###get all the  ability numbers
    ###It may happen that 1 ability has multiple description and numbers
    ###So we need to retrieve all of them
    ###For example: Aatrox has 4 descriptions on his Q
    ###Create list to put information
    champList = []
    for i in range(0, len(descr)):
        ###Start collecting information, champion and button as base
        information = [champ, button]

        ###Cooldown of the spell
        if spell[0]['cooldown']:
            coolDownSpell = spell[0]['cooldown'].get('modifiers', {})[0].get('values', None)
            # print('cooldown: ' + str(coolDownSpell))
        else:
            coolDownSpell = ''

        ###Put cooldown of the ability in the list
        information.append(coolDownSpell)
        spellDmg = descr[i].get('leveling')
        # print(spellDmg)
        if spellDmg:
            spellNumber = spellDmg[0].get('modifiers')
            attribute = spellDmg[0].get('attribute')

            ###list to store information
            l = []

            ###Get the specific values
            ###The first base and units are the base values, these don't scale
            ###The second base and units are often scaling numbers(Like +0.x ad/ap%)
            for j in range(0, len(spellNumber)):
                if len(spellNumber) == 1:
                    l.append('')
                base = spellNumber[j]['values']
                units = spellNumber[j]['units']

                l.append(base)
                if '' not in units:
                    l.append(units)

            information.append(attribute)
            information.extend(l)
            champList.append(information)

        else:
            pass
    return champList
    ###End function


###List to store all abilties of all champions
champAbilities = []

###get ability for each champion
for champ in champions:

    #####Get the ability numbers#####
    ###Input: A list containing QWER
    ###Output: All the information of the abilities

    ###List for all the abilities of all champions

    buttons = ['Q', 'W', 'E', 'R']
    for button in buttons:
        ###Store all the information in the list
        champAbilities.extend(abilities(button, champ))

###turn the list into a dataframe
df = pd.DataFrame(champAbilities, columns=['champion', 'ability', 'cooldown', 'type', 'baseDmg',
                                           'scaleDmg', 'ratio', 'col8', 'col9', 'col10'])

df.to_csv('champAbilities.csv')


