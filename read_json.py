'''
Created on 20 Sep 2018

@author: benjaminsenyonyi
'''
import csv
import pandas
from file_select import select_hashtags, select_message_id, \
    select_hashtag_data, select_time_text
# import builtins
import numpy as np
from hash_dictionary import select_time_dict, select_hashtag_dict, select_final_dict, \
    select_userid_dict, select_text_dict, sel_double_htags
from folder_select import select_tweet_text
from draw_graph import drawgraph, drawloggraph
from functionals import count_dict_values, unique_list_output, value_counter, \
    count_ht_apps
from hash_stats import create_similarity_list, counted_sims

# Begin main method
#Note that file paths need to be input
if __name__ == '__main__':
    fileName = \
    ".../tester.json"
    json_folder = \
    ".../iswc2015/split-cascades"

    
#     List of methods that creates dictionaries with message ID and hashtags
    create_hashdict = select_hashtag_dict(json_folder)
    create_unique_list = unique_list_output(create_hashdict)
    final_dict =  (select_final_dict(json_folder))
    counted_values =  count_dict_values(create_hashdict)
    userid_dict = select_userid_dict(json_folder)
    text_dict = select_text_dict(json_folder)
    
    dou_more_hashtags = sel_double_htags(create_hashdict)
    
    

    
#     Writing ID CSV
    with open('.../UserID_results.csv', 'w') as f:
        w = csv.writer(f, delimiter =';')
        w.writerows(sorted(userid_dict.items()))
        print('Print UserID completed')
    
# #     Writing two or more hashtag dictionary
    with open('.../Two_or_more_hts_results.csv', 'w') as f:
        w = csv.writer(f, delimiter =';')
        w.writerows(dou_more_hashtags.items())
        print('Print IDs with two or more hashtags completed')
      
#     Writing Hashtag CSV alone
    with open('.../Hashtag_results.csv', 'w') as f:
        w = csv.writer(f, delimiter =';')

        w.writerows(sorted(create_hashdict.items()))
        print('Hashtag table completed')
    

#     Using pandas for the final CSV
    data_file = pandas.DataFrame(final_dict).transpose().reset_index()
    data_file.columns = ['message_id', 'Hashtags', 'Time', 'user_id']
    data_file.groupby('Hashtags')
    data_file.set_index('message_id', inplace = True)
    data_file.to_csv('.../final_dict_file.csv')
    print('Pandas final dictionary file completed')
   
    
#     Draw graph to show hashtag occurences
    graphlist = []
    graphlist = count_ht_apps(create_hashdict)
    print('Drawing count graph')
    print(graphlist)
    drawgraph(graphlist)
    drawloggraph(graphlist)
#     pass





