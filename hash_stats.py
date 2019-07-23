'''
Created on 4 Oct 2018

@author: benjaminsenyonyi
'''
import numpy as np

def create_similarity_list(dict):
    final_list = {}
    new_dict = []
    copy_dict = dict.copy()
    for key, value in dict.items():
        for c_key, c_value in copy_dict.items():
            if np.array(value) == np.array(c_value):
                new_dict[key] = value, c_value, c_key

                
        
    return new_dict

def counted_sims(data_dict):
    '''
    Returns dictionary showing count of the number of similar ... 
    '''
    new_data = {}
    for key in data_dict.keys():
        new_data[key] = {}
        x = []
        y = []
        for k, v in data_dict.items():
            if key == k: 
                pass
            else:
                shared = np.intersect1d(data_dict[key],v)
                for item in shared:
                    x.append(item)
                    y.append((k, len(shared))) 
                new_data[key] = (list(set(x)),y) #update the dict
            
    return new_data