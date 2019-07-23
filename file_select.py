'''
Created on 20 Sep 2018

@author: benjaminsenyonyi
'''

import os
import glob
import json
import objectpath
from objectpath.utils.colorify import string

# Get the tuple tree for the text in hashtags 
def get_text_tree(data):
    tree = objectpath.Tree(data)
    return tuple(tree.execute('$.entities.hashtags.text'))

def select_hashtag_data(json_folder):
    names = []
    filelist = []
    dict = {}
    os.chdir(json_folder)
    for counter, files in enumerate(glob.glob("*.json")):
        filelist.append(files)
    for fileName in filelist:
        with open(fileName) as file_to_read:
            for line in file_to_read:
                data = json.loads(line)
                json.dumps(data, ensure_ascii=False)
                names.extend(get_text_tree(data))

    return names       

# Old method (no longer in use).
def select_hashtags(fileName):
    data = []
    names = []
    with open(fileName, 'r') as file_to_read:
        for line in file_to_read:
            data.append(json.loads(line))
            json_tree = objectpath.Tree(data)
            hashtag_tuple = tuple(json_tree.execute('$.entities.hashtags.text'))
            new_tuple = hashtag_tuple
            print(new_tuple)
        print("Hashtag data loaded successfully")
    return hashtag_tuple

# Working well
def select_message_id(fileName):
    data = []
    with open(fileName, 'r') as file_to_read:
        for line in file_to_read:
            data.append(json.loads(line))
            json_tree = objectpath.Tree(data)
            id_tuple = tuple(json_tree.execute('$.id'))
    print("ID_s loaded successfully")
    return id_tuple

# select_time_text functioning as required
def select_time_text(fileName):
    dict={}
    with open(fileName, 'r') as file_to_read:
        content = file_to_read.read().splitlines()
        for line in content:
            json_tree = objectpath.Tree(json.loads(line))
            dict[json_tree.execute('$.id')] = json_tree.execute('$.created_at')
    print("Tweets loaded successfully")
    return dict