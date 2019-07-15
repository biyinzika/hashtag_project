'''
Created on 27 Sep 2018

@author: benjaminsenyonyi
'''
import json
import objectpath
import os
import glob
from distutils import filelist


# Functioning well returns texts of the tweets.
def select_tweet_text(json_folder):
    filelist = []
    os.chdir(json_folder)
    for counter, files in enumerate(glob.glob("*.json")):
        filelist.append(files)
    for fileName in filelist:
        with open(fileName, 'r') as file_to_read:
            for line in file_to_read:
                json_tree = objectpath.Tree(json.loads(line))
                tweet_texts = tuple(json_tree.execute('$.text'))
    print("Tweets loaded successfully")
    return tweet_texts

# May not be used; for future reference
def select_hashtags(json_folder):
    filelist = []
    os.chdir(json_folder)
    for counter, files in enumerate(glob.glob("*.json")):
        filelist.append(files)
    for fileName in filelist:
        with open(fileName, 'r') as file_to_read:
            for line in file_to_read:
                json_tree = objectpath.Tree(json.loads(line))
                hashtags = tuple(json_tree.execute('$.entities.hashtags.text'))
    print("Tweets loaded successfully")
    return hashtags