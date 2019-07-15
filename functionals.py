'''
Created on 27 Sep 2018

@author: benjaminsenyonyi
'''
from scipy.fftpack.basic import istype
from collections import Counter
import itertools
from collections import defaultdict


def hash_sim(dictionary_name):
    '''
    Run set similarity over the default dictionary
    Find similar values in the hashtag dictionary, check timing on these relations and list them.
    for all combinations of the hashtags find all ids that have 2 or more. 
    '''
    sort_dict = sorted(dictionary_name)
    combinations = itertools.product(*(dictionary_name[Name] for Name in sort_dict))
    for values in dictionary_name.values():
        combinat = list(itertools.product(*values))
    
    comb_list = set(list(combinations))
    for v in comb_list:
        count = 0
        if v in dictionary_name.values():
            count +=1
            if count >=1:
                print(v, count )
    
    leng = len(comb_list)
    '''
    Here is the second method
    '''
    dd = defaultdict(set)
    
    for k, v in dictionary_name.items():
        dd[tuple(v)].add(k)
    dict_copy = {}
    key_list = []
    dict_copy = dd.copy()
    for k in dict_copy.keys():
        for keys in dd.keys():
#             key_list.append(set(k and keys)) # Too heavy on the computer. Not optimal.
            key_list.append(k)
    
    return key_list

def key_similarity(key_dictionary):
    '''
    find similarity in keys
    '''
    words = {}
    for key in key_dictionary.keys():
        for w in key.split():
            if w not in words:
                words[w] = set()
            words[w].add(key)
    
    
    def lookup(search_string, words, programs):
        result_keys = None
        for w in search_string.split():
            w = w.lower()
            if w not in words:
                return []
            result_keys = words[w] if result_keys is None else result_keys.intersection(words[w])
        return [programs[k] for k in result_keys]
    pass

def extract_userid(message_id, userid_dictionary):
    '''
    Input is message ID and UserID dictionary for the hashtag extraction.
    Returns user ID number of message ID.
    '''
    for k,v in userid_dictionary.items():
        if message_id == k:
            number = v
    return number

def extract_time(message_id, time_dictionary):
    '''
    Input is message ID and Time dictionary for the time extraction.
    Returns time of message ID.
    '''
    for k,v in time_dictionary.items():
        if message_id == k:
            time_val = v
    return time_val
 
def count_dict_values(dict):
    """
    Prints a list of sets of hashtags per message and the number of times these combinations occurred.
    """
    end = "Completed"
    value_list = list(dict.values())
    value_list.sort(key=None, reverse=True)
    result = {}
    for d in value_list:
        if tuple(d) not in result:
            result[tuple(d)] = value_list.count(d)

#     print result

# # Original
#     for x in value_list:
#         print (x, value_list.count(x))
#         
#     return end   
## Second Option using collections.Counter
#     result = Counter(tuple(x) for x in value_list)   
    return result

  
def value_counter(v_dict):
    '''
    Returns a unique list of the hashtags with each unique output and the number of times that output appears
    '''
    end = "Completed Value Count"
    count = 0
    unique_list=[]
    value_list = tuple(v_dict.values())
    for x in value_list:
        if x not in unique_list: 
            unique_list.append(x)
        
    for y in unique_list:
        for z in value_list:
            if y==z:
                count+=1
                print (y, count)
    return end

 
def unique_list_output(dict):
    """
    Working and outputting a unique list of the hashtags in the cascade
    """
    unique_list = [] 
    value_list = list(dict.values())
#     traverse over all elements 
#     for x in value_list:
#         print (x, value_list.count(x))
    for x in value_list: 
        if x not in unique_list: 
            unique_list.append(x)
    
    return unique_list

# Counts the number of hashtags that appear in a message for a given cascade.
# Input is the dictionary formed.
def count_ht_apps(dict):
    """
    Counting the number of hashtag appearances in the (specifically) hashtag dictionary.
    """
    value_list = list(dict.values())
#     Initialize counters per value
    count_0_array = 0
    count_1_array = 0
    count_2_array = 0
    count_3_array = 0
    count_4_array = 0
    count_5_array = 0
    count_6_array = 0
    count_7_array = 0
    count_8_array = 0
    count_9_array = 0
    count_10_array = 0
    value_list = tuple(dict.values())
    
    for spec_value in value_list:
        if isinstance(spec_value, (list,)):
            if len(spec_value) == 0:
                count_0_array +=1
            if len(spec_value) == 1:
                count_1_array +=1
            if len(spec_value) == 2:
                count_2_array +=1
            if len(spec_value) ==3:
                count_3_array +=1
            if len(spec_value) ==4:
                count_4_array +=1
            if len(spec_value) ==5:
                count_5_array +=1
            if len(spec_value) ==6:
                count_6_array +=1
            if len(spec_value) ==7:
                count_7_array +=1
            if len(spec_value) ==8:
                count_8_array +=1
            if len(spec_value) ==9:
                count_9_array +=1
            if len(spec_value) ==10:
                count_10_array +=1
#             print (spec_value, value_list.count(spec_value))
#     Return order (0 hashtags, 1 hashtag, 2 hashtags, 3 hashtags, 4 hashtags)
    return count_0_array, count_1_array, count_2_array, count_3_array, count_4_array, count_5_array, \
         count_6_array, count_7_array, count_8_array, count_9_array, count_10_array