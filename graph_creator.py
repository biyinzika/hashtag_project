'''
Created on 27 Jan 2019

File that deals with (mostly) Retweet values

@author: benjaminsenyonyi
'''
import csv
import os
import glob
import numpy as np
from scipy.sparse import csr_matrix 
import networkx as nx
from networkx.algorithms import bipartite
from io import StringIO
from hash_dictionary import select_time_dict
from collections import Counter


def density_RetweetCasc(folderWithCsvs):
    '''
    Creates graph from individual retweet files and returns the densities for each cascade.
    '''
    
    edgeWeight = 0
    
    filelist = []
    os.chdir(folderWithCsvs)
    for counter, files in enumerate(glob.glob("*.csv")):
        filelist.append(files)
    
    file_number = len(filelist)
    for each_file in range(file_number):
        density_values = []
        for fileitem in filelist:
            nodes = set([])
            edges = {}
            
            with open(fileitem, "r") as cascFile:
                reader = csv.reader(cascFile, delimiter=';')
                for row in reader:
                    nodes.add(row[0])
                    nodes.add(row[1])
    
                    try:
                        # key is source and value is target
                        edges[row[1]].add(row[0])
                    except KeyError:
                        edges[row[1]] = set([row[0]])
    
            nodes = list(nodes)
            noOfNodes = len(nodes)
            
            graph = nx.Graph()
            graph.add_nodes_from(list(range(noOfNodes)))
            edgesList = []
        
            # build adjacency matrix
            row = []
            col = []
            val = []
            for key in edges.keys():
                # get source's index
                keyIndex = nodes.index(key)
                targets = edges[key]
                for target in targets:
                    # get target's index
                    targetIndex = nodes.index(target)
                    # put it into sparse matrix
                    row.append(keyIndex)
                    col.append(targetIndex)
                    val.append(edgeWeight)
                    
                    edgesList.append((keyIndex, targetIndex))
           
            graph.add_edges_from(edgesList)
            
            dense = nx.density(graph)
            density_values.append(dense)
            
 
    return density_values


def casc_lifetime(time_dict):
    '''
    Returns the lifetime of the cascade from the time dictionary
    '''
    largest_time = max(time_dict.items(), key=lambda k: k[1])
    lowest_time = min(time_dict.items(), key=lambda k: k[1])
    lifetime = (largest_time[1] - lowest_time[1])
    return lifetime

def Retweet_Reciprocity(fileName):
    '''
    Create ID lists for both roots and children, create a count and reciprocity method.
    create the row 1 iDS , row 3 ids
    '''
    root_ids =[]
    child_ids = []
    
    with open(fileName) as inputfile:
        reader = csv.reader(inputfile, delimiter = ',')
        for row in reader:
            child_ids.append(( row[3], row[1] ))
            root_ids.append(( int(row[1]) , int(row[3]) ))      


    this_count = Counter(root_ids)


    recip_array = []
    for k,v in root_ids:
        
        root_id_count = root_ids.count((k,v))
        second_count = root_ids.count((v,k))
        if second_count == 0:
            rec_city = 0
        else:
            rec_city = (root_id_count / second_count)
        recip_array.append(rec_city)
        
    print(sorted(recip_array, reverse = True))
         
    print(this_count)


    return recip_array

def Spread_Score(fileName):
    '''
    Calculating the spread score of a user in the graph 
    For each user :
    number of retweets / number of tweets 
    WReturns dictionary values showing reciprocity
    '''
    user_ids= []
    target_ids = []
    source_ids = []
    target_dict = {} #dictionary of retweet counts
    source_dict = {}
    
    with open(fileName) as inputfile:
        reader = csv.reader(inputfile, delimiter = ',')
        for row in reader:
#             add all retweeted values to target_ids
            target_ids.append(row[3]) #target users
            source_ids.append(row[1]) #source users
            
#             Begin adding all user IDs to one array
            if row[1] not in user_ids:
                user_ids.append(row[1])
            if row[3] not in user_ids:
                user_ids.append(row[3])
#     Count retweeted (target) users method
    for user in user_ids:
        rt_count = target_ids.count(user)
        target_dict[user] = rt_count

#     Count source users
    for user in user_ids:
        twt_count = source_ids.count(user)
        source_dict[user] = twt_count
    
    spread_dict = {}
    
    for k,v in source_dict.items():
        for key, value in target_dict.items():
            if k == key:
                spread_sco = v / (value+v)
                spread_dict[k] = spread_sco
    print(spread_dict)          
    
    return spread_dict.values()


def fractionRootNodes(fileName, value):
    '''
    Return number of times the value appears in the column
    '''
    
    all_ids =[]
    with open(fileName) as inputfile:
        reader = csv.reader(inputfile, delimiter = ',')
        for row in reader:
#             add all retweeted values to target_ids
            all_ids.append(row[2]) 
    count_nodes = Counter(all_ids)
    print(sum(count_nodes.values()))
    
    return count_nodes


def array_max(array_name):
    '''
    Returns maximum in given array
    '''
    return np.max(array_name)

def array_mean(array_name):
    '''
    Returns average from given array
    '''
    return np.mean(array_name)

def averageRetweet_Time(fileName):
    '''
    Calculate difference in values per row (4 and 3) and append to array
    --------
    '''
    time_diff =[]
    
    with open(fileName) as inputfile:
        reader = csv.reader(inputfile, delimiter = ',')
        for row in reader:
            row_diff = int(row[4]) - int(row[3])
            time_diff.append(row_diff) 
    return time_diff 







