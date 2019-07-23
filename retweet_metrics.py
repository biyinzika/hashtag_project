'''
Created on 28 Jan 2019

@author: benjaminsenyonyi

Main class for (most) retweet operations
'''

from graph_creator import density_RetweetCasc, casc_lifetime,  averageRetweet_Time,\
    array_max, array_mean, Retweet_Reciprocity, Spread_Score, fractionRootNodes
from hash_dictionary import select_time_dict
import numpy as np



# Calculate_Density(adjMatrix)
if __name__ == '__main__':
    folderWithCsvs = ".../retweet_casc/"
	fileName = ".../casc_spare/Casc_recip.csv"
    
    recipFile =".../casc_spare/Retweets.csv"
    
    retweet_file = ".../csv_folder/cascades/combi_casc/sections/retweets/retweets.csv"
    repquo_file = ".../csv_folder/cascades/combi_casc/sections/rep_and_quotes/ReplyOrQuote.csv"
    sim_file = ".../csv_folder/cascades/combi_casc/sections/message_similarity/Similarity.csv"
    hash_file = ".../csv_folder/cascades/combi_casc/sections/hashtags/intersections.csv"
    
    json_folder = \
    ".../iswc2015/split-cascades"
    
    time_dict = select_time_dict(json_folder)
    #############################
#     Other nethods
	density_values = density_RetweetCasc(folderWithCsvs)
    cascade_lifetime = casc_lifetime(time_dict)
    aveRet_time = averageRetweet_Time(fileName)
    spread_score = Spread_Score(recipFile)
    ret_reciprocity = Retweet_Reciprocity(recipFile)
    
    root_number = fractionRootNodes(repquo_file, '657341903936081920')
    print(root_number)
    print(array_mean(ret_reciprocity))
    
    
    #################################
#     Print results
#     print(density_values)
#     print(cascade_lifetime)
#     print(aveRet_time) 
#     print(spread_score)
    ################################
#     print(array_mean(aveRet_time))
    
    
    
    