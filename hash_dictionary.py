'''
Created on 20 Sep 2018

@author: benjaminsenyonyi
'''
import json
import os
import glob
import objectpath
import ast
from file_select import select_hashtags, select_message_id, \
    get_text_tree

def create_id_dictionary():
#     Use tuples selected from hashtags and ID's and select maps for use.
#     map to record JSON values for calculations; 
#     [key : value] [message-id : tweet text, hashtag text, time, user ID]       
    pass


def select_final_dict(json_folder):
    """
    Dictionary for all key values
    MessageID : Hashtags, time, user_id
    Dictionary working and creating the right values.
    """
    filelist = []
    f_dict={}
    os.chdir(json_folder)
    for counter, files in enumerate(glob.glob("*.json")):
        filelist.append(files)
    for fileName in filelist:
        with open(fileName, 'r') as file_to_read:
            for line in file_to_read:
                data = json.loads(line)
                json_tree = objectpath.Tree(data)
                json.dumps(data, ensure_ascii=True, indent=4)
                hashlist = list(json_tree.execute('$.entities.hashtags.text'))
                newhash_list = []
                for word in hashlist:
                    str(word) #String removes the unicode value sign at the beginning!
                    newhash_list.append(str(word).lower())
                    for item in newhash_list:
                        if 'iswc2015' in newhash_list:
                            newhash_list.remove('iswc2015')
#                 final_list.append(json_tree.execute('$.id'), newhash_list,json_tree.execute('$.created_at'),json_tree.execute('$.user.id'))
                f_dict[json_tree.execute('$.id')] = \
                    ( newhash_list, \
                      json_tree.execute('$.created_at'), \
                        json_tree.execute('$.user.id')) 
                json.dumps(f_dict)
    print("Dictionary (hashtag_text, time, userID) loaded")
#     Dictionary format {message_ID : hashtag-text, time, User_ID}
    return f_dict


def select_hashtag_dict(json_folder):
    """
    new formula providing dictionary with hashtags in lower case.
    """
    filelist = []
    dict={}
    os.chdir(json_folder)
    for counter, files in enumerate(glob.glob("*.json")):
        filelist.append(files)
    for fileName in filelist:
        with open(fileName, 'r') as file_to_read:
            for line in file_to_read:
                data = json.loads(line)
                json_tree = objectpath.Tree(data)
                json.dumps(data, ensure_ascii=True, indent=4)
                hashlist = list(json_tree.execute('$.entities.hashtags.text'))
                newhash_list = []
                for word in hashlist:
                    newhash_list.append(str(word).lower())
                    for item in newhash_list:
                        if 'iswc2015' in newhash_list:
                            newhash_list.remove('iswc2015')
#                         if [] in newhash_list:
#                             newhash_list.remove()
#                 print newhash_list         
                dict[json_tree.execute('$.id')] = newhash_list
#                 dict[json_tree.execute('$.id')] = list(json_tree.execute('$.entities.hashtags.text'))
                
#                 Not working because list has no attribute lower()
#                 for key, value in dict.iteritems():
#                     dict[key] = value.lower()
    print("Hashtag Dictionary loaded")
    return dict

def select_double_hashtag_dict(json_folder):
    """
    Older unused method to produce dictionary with either two or more hashtags.
    """
    filelist = []
    dict={}
    os.chdir(json_folder)
    for counter, files in enumerate(glob.glob("*.json")):
        filelist.append(files)
    for fileName in filelist:
        with open(fileName, 'r') as file_to_read:
            for line in file_to_read:
                data = json.loads(line)
                json_tree = objectpath.Tree(data)
                json.dumps(data, ensure_ascii=True, indent=4)
                hashlist = list(json_tree.execute('$.entities.hashtags.text'))
                newhash_list = []
                for word in hashlist:
                    newhash_list.append(str(word).lower())
                    for item in newhash_list:
                        if 'iswc2015' in newhash_list:
                            newhash_list.remove('iswc2015')      
                dict[json_tree.execute('$.id')] = newhash_list
    print("Hashtag Dictionary loaded")
#     Begin listing of values to output only values with two or more hashtags
    new_val_list = []
    dict_inverse = {}
    value_list = tuple(dict.values())
    for spec_value in value_list:
        if isinstance(spec_value, (list,)):
            if len(spec_value) >= 2:
                new_val_list.append(spec_value)
                for or_key,or_val in dict.items():
                    if or_val == spec_value:
                        dict_inverse[or_key] = or_val
#                     for item in or_val:
#                         dict_inverse[item] = or_key
    print (new_val_list)
    return dict_inverse

def sel_double_htags(hash_dict):
    """
    Method to produce dictionary with either two or more hashtags appearing in the dictionary.
    Input is hashtag dictionary
    """
#     Begin listing of values to output only values with two or more hashtags
    new_val_list = []
    dict_double = {}
    value_list = tuple(hash_dict.values())
    for spec_value in value_list:
        if isinstance(spec_value, (list,)):
            if len(spec_value) >= 2:
                new_val_list.append(spec_value)
                for or_key, or_val in hash_dict.items():
                    if or_val == spec_value:
                        dict_double[or_key] = or_val
#                     for item in or_val:
#                         dict_inverse[item] = or_key
#     print (new_val_list)
    print("Double & more hashtag dictionary loaded")
    return dict_double


def select_hashtag_2(json_folder):
    """ 
    Old method
    ID to hashtags dictionary working and creating the right lowercase values.
    """
    filelist = []
    dict={}
    os.chdir(json_folder)
    for counter, files in enumerate(glob.glob("*.json")):
        filelist.append(files)
    for fileName in filelist:
        with open(fileName, 'r') as file_to_read:
            for line in file_to_read:
                data = json.loads(line)
                json_tree = objectpath.Tree(data)
                json.dumps(data, ensure_ascii=True, indent=4)
                hashlist = list(json_tree.execute('$.entities.hashtags.text'))
                newhash_list = []
                for word in hashlist:
                    newhash_list.append(str(word).lower())
                dict[json_tree.execute('$.id')] = newhash_list
                
#                 Not working because list has no attribute lower()
#                 for key, value in dict.iteritems():
#                     dict[key] = value.lower()
    print("Hashtag Dictionary loaded")
    return dict

 
def select_text_dict(json_folder):
    """
    create dictionary for ids and text tweets functioning well
    """
    filelist = []
    dict = {}
    os.chdir(json_folder)
    for counter, files in enumerate(glob.glob("*.json")):
        filelist.append(files)
    for fileName in filelist:
        with open(fileName, 'r') as file_to_read:
            for line in file_to_read:
                data = json.loads(line)
                json_tree = objectpath.Tree(data)
                json.dumps(data, ensure_ascii=True, indent=4)
#                 textlist = str()
# #                 for words in textlist:
# #                     str(words)
                dict[json_tree.execute('$.id')] = json_tree.execute('$.text')
    print("Texts loaded successfully")
    return dict


def select_time_dict(json_folder):
    """
    create dictionary for id and time functioning well
    """
    dict = {}
    filelist = []
    os.chdir(json_folder)
    for counter, files in enumerate(glob.glob("*.json")):
        filelist.append(files)
    for fileName in filelist:
        with open(fileName, 'r') as file_to_read:
            for line in file_to_read:
                data = json.loads(line)
                json_tree = objectpath.Tree(data)
#                 json.dumps(data, ensure_ascii=True, indent=4)
                dict[json_tree.execute('$.id')] = json_tree.execute('$.created_at')
    print("Time dictionary loaded")
    return dict

def select_userid_dict(json_folder):
    """
    create dictionary for id and time functioning well
    """
    dict = {}
    filelist = []
    os.chdir(json_folder)
    for counter, files in enumerate(glob.glob("*.json")):
        filelist.append(files)
    for fileName in filelist:
        with open(fileName, 'r') as file_to_read:
            for line in file_to_read:
                data = json.loads(line)
                json_tree = objectpath.Tree(data)
#                 json.dumps(data, ensure_ascii=True, indent=4)
                dict[json_tree.execute('$.id')] = json_tree.execute('$.user.id')
    print("UserID dictionary loaded")
    return dict


def create_hash_dictionary(json_folder):
    names = []
    filelist = []
    os.chdir(json_folder)
    for counter, files in enumerate(glob.glob("*.json")):
        filelist.append(files)
    for file_name in filelist:
            with open(file_name) as fh:
                for line in fh:
                    data = json.loads(line)
                    names.extend(get_text_tree(data))

    return names

