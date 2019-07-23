'''
Created on 3 Dec 2018

@author: benjaminsenyonyi
'''
from hash_dictionary import select_double_hashtag_dict, select_hashtag_dict, sel_double_htags, select_time_dict

import time
from functionals import hash_sim
from binary_social_val import determine_social_value
from cascade_builder import casc_creator, csv_hash_cascade, combi_cascade
 


if __name__ == '__main__':
    print("##########################################################")

#     Folder Directories

    json_folder = \
    ".../iswc2015/split-cascades"
    
    combi_startTime = time.time()
    print(combi_cascade(json_folder))
#     print(csv_hash_cascade(json_folder))
    combi_endtime = time.time() - combi_startTime
    print(combi_endtime)
#     print(determine_social_value(2310416978, 408521540))
    print("##########################################################")
    pass