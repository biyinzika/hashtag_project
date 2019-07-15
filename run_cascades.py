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

#     json_folder = \
#     "/Users/benjaminsenyonyi/Documents/Masters course/Sem 4/new_workspace/hashtag-project/jsonfolder/"
    json_folder = \
    "/Users/benjaminsenyonyi/Documents/Masters course/Sem 4/socialgraph/new_data/iswc2015/split-cascades"


#     trial_dict = {52384: ['text2015', 'webnet', 'biological'], 18720: ['datascience', 'bigdata', 'links'], 82465: ['biological', 'biomedics', 'datamining', 'datamodel', 'semantics'], 73120: ['links', 'scientometrics'], 22276: ['text2015', 'webnet'], 97376: ['text2015', 'webnet'], 43424: ['biological', 'biomedics', 'datamining', 'datamodel', 'semantics'], 23297: ['links', 'scientometrics']}
#     print(hash_sim(trial_dict))
    
    
    combi_startTime = time.time()
    print(combi_cascade(json_folder))
#     print(csv_hash_cascade(json_folder))
    combi_endtime = time.time() - combi_startTime
    print(combi_endtime)
#     print(determine_social_value(2310416978, 408521540))
    print("##########################################################")
    pass