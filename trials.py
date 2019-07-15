'''
Created on 21 Sep 2018

@author: benjaminsenyonyi
'''
import objectpath
import os
from collections import Counter
# from __builtin__ import set
import csv

from hash_dictionary import select_double_hashtag_dict, select_hashtag_dict, sel_double_htags

from cascade_builder import casc_creator, csv_hash_cascade
# from aifc import data

if __name__ == '__main__':
    print("##########################################################")
#     json_folder = \
#     "/Users/benjaminsenyonyi/Documents/Masters course/Sem 4/new_workspace/hashtag-project/jsonfolder/"
    json_folder = \
    "/Users/benjaminsenyonyi/Documents/Masters course/Sem 4/socialgraph/new_data/iswc2015/split-cascades"
    
#     create_hashdict = select_hashtag_dict(json_folder)
#     create_hashd = sel_double_htags(create_hashdict)
#     print(create_hashd)
    print(csv_hash_cascade(json_folder))
    
    print("##########################################################")    
    pass


def triedanddone():
    count_list = [['a', 'b'],['d', 'e'], ['e'], ['c'], ['a', 'b'], ['c']]
#     result = Counter(tuple(x) for x in count_list)
    results = {}
    for d in count_list:
        if tuple(d) not in results:
            results[tuple(d)] = count_list.count(d)

    print (results)
    count_list = [tuple(i) for i in count_list]

    d = {i: count_list.count(i) for i in set(count_list)}
    print(d)
    
    arr = [[1, 2], [3], [1, 2], [4], [3]]
    new_arr = []
    for elem in arr:
    # You are wrapping your element in a list, at the same scale
    # than the list you wish to output (meaning 3 dimensions depth list).
    # In other words, you have a list... that contains a list, containing
    # your element and its count. The first depth seems useless at first glance,
    # but it's just here to keep the same depth you will have appending to new_arr.

    # You can try by yourself doing "obj = [elem, arr.count(elem)]" if you don't
    # believe me.
        obj = [ [elem, arr.count(elem)] ]
        if obj[0] not in new_arr:
        # checking on first index to check our elem and not our ""wrapper""
            new_arr += obj

    print(new_arr)
#     distinct_list = []
#     count_list.sort()
#     for x in count_list:
#         if x not in distinct_list: 
#             distinct_list.append(x)       
#     for z in distinct_list:
#         for y in count_list:
#             if y == z:
#                 print(z, count_list.count(z))
                
#     print distinct_list
    
    alphabet = {1:['aseasHFUEBF JEIG FKEH UIEBjkahds', 'Yere'], 2: 'aygra', 3: 'DUER', 4:'jahgw', 5: 'UGfaigad', 6: 'kauydsgfIf'}
    newAlphabet = {}

    for key, value in alphabet.iteritems():
        newAlphabet[key] = value
#         print newAlphabet
    alpha = ['YETR', 'Ysjdfk', 'Trial', 'before', 'END']
    newlist = []
    for item in alpha:
#         item.lower()
        newlist.append((item.lower()))
#         print newlist
    
    
    data = {"entities":{"hashtags":[{"indices":[28,37],"text":"iswc2015"}],"symbols":[]}}
    json_tree = objectpath.Tree(data)
    result = json_tree.execute('$.entities.hashtags[@.text]')
    for entry in result:
#         print entry
        pass

def get_folder(jsonfolder):
    del_list = [['a', 'b'],['d', 'e'], ['e'], ['c'], ['a', 'b'], ['c'], [], ['a']]
    for values in del_list:
       if 'a' in del_list:
           del_list.remove('a')
#             if 'a' is del_list:
#                 del_list.remove('a')
    print(del_list)
    
    with open('names.csv', 'w') as csvfile:
               
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
        writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
        writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

def add_fruits(inventory, fruit, quantity=0):
    new_inventory = {} 
    new_inventory[fruit] = quantity
    return new_inventory


# json_raw = '''{
#   "_links": [
#     {
#       "self": "http://api.football-data.org/alpha/soccerseasons/354/teams"
#     },
#     {
#       "soccerseason": "http://api.football-data.org/alpha/soccerseasons/354"
#     }
#   ],
#   "count": 20,
#   "teams": [
#     {
#       "_links": {
#         "fixtures": {
#           "href": "http://api.football-data.org/alpha/teams/66/fixtures"
#         },
#         "players": {
#           "href": "http://api.football-data.org/alpha/teams/66/players"
#         },
#         "self": {
#           "href": "http://api.football-data.org/alpha/teams/66"
#         }
#       },
#       "code": "MUFC",
#       "crestUrl": "http://upload.wikimedia.org/wikipedia/de/d/da/Manchester_United_FC.svg",
#       "name": "Manchester United FC",
#       "shortName": "ManU",
#       "squadMarketValue": "425,000,000 \u20ac"
#     },
#     {
#       "_links": {
#         "fixtures": {
#           "href": "http://api.football-data.org/alpha/teams/72/fixtures"
#         },
#         "players": {
#           "href": "http://api.football-data.org/alpha/teams/72/players"
#         },
#         "self": {
#           "href": "http://api.football-data.org/alpha/teams/72"
#         }
#       },
#       "code": "SWA",
#       "crestUrl": "http://upload.wikimedia.org/wikipedia/de/a/ab/Swansea_City_Logo.svg",
#       "name": "Swansea City",
#       "shortName": "Swans",
#       "squadMarketValue": "104,000,000 \u20ac"
#     },
#     {
#       "_links": {
#         "fixtures": {
#           "href": "http://api.football-data.org/alpha/teams/338/fixtures"
#         },
#         "players": {
#           "href": "http://api.football-data.org/alpha/teams/338/players"
#         },
#         "self": {
#           "href": "http://api.football-data.org/alpha/teams/338"
#         }
#       },
#       "code": "LCFC",
#       "crestUrl": "http://upload.wikimedia.org/wikipedia/en/6/63/Leicester02.png",
#       "name": "Leicester City",
#       "shortName": "Foxes",
#       "squadMarketValue": "63,250,000 \u20ac"
#     },
#     {
#       "_links": {
#         "fixtures": {
#           "href": "http://api.football-data.org/alpha/teams/62/fixtures"
#         },
#         "players": {
#           "href": "http://api.football-data.org/alpha/teams/62/players"
#         },
#         "self": {
#           "href": "http://api.football-data.org/alpha/teams/62"
#         }
#       },
#       "code": "EFC",
#       "crestUrl": "http://upload.wikimedia.org/wikipedia/de/f/f9/Everton_FC.svg",
#       "name": "Everton FC",
#       "shortName": "Everton",
#       "squadMarketValue": "179,250,000 \u20ac"
#     }
#   ]
# }'''
# import json
# from pprint import pprint
# 
# json_dict = json.loads(json_raw)
# 
# # pprint(json_dict)
# 
# pprint(json_dict['teams'])
# 
# print '-'*10
# 
# for team in json_dict['teams']:
#     print team['_links']['fixtures']['href']



# data = {
#     "entities": {
#         "actions": {
#                 "name": "reading",
#                 "description": "blablabla"
#             },
#         "name": "John"
#     }
# }