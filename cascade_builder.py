'''
Created on 21 Nov 2018

@author: benjaminsenyonyi

All routes to directories have been altered and can be altered for use.
'''
from hash_dictionary import sel_double_htags, select_hashtag_dict, \
    select_final_dict, select_time_dict, select_userid_dict
import csv
import pandas as pd
import itertools
# import tarjan
from collections import defaultdict
from binary_social_val import determine_social_values, determine_social_value
from functionals import extract_userid, extract_time
from itertools import combinations

def combi_cascade(json_folder):
    '''
    Find 2 or more shared hashtags in the dictionaries, and sort based on earlier time
    Print out intersection csv file including social connection value
    '''
    hashtag_dictionary = select_hashtag_dict(json_folder)
    doubles_dictionary = sel_double_htags(hashtag_dictionary)
    time_dictionary = select_time_dict(json_folder)
    userid_dictionary = select_userid_dict(json_folder)

     
#     for first, second in combinations(hashtag_dictionary.items(), r=2):
#     Files to be written

    f0 = open('.../combi_casc/intersections.csv','w')
#  
#      
    for first, second in combinations(doubles_dictionary.items(), r=2):
        intersection = set(first[1]) & set(second[1])
        if intersection:
            if len(intersection) >=2:
#             Get time values
                tim1 = extract_time(first[0], time_dictionary)
                tim2 = extract_time(second[0], time_dictionary)
    
    #                 Set constants for time values that can be used to redefine order.
                if tim1 < tim2:
                    early =first[0]
                    late = second[0]
                else:
                    early = second[0]
                    late = first[0]
    #             Get user ID values
                bin1 = extract_userid(early, userid_dictionary)
                bin2 = extract_userid(late, userid_dictionary)
    #             Social value generator
                soc_val = determine_social_values(bin1, bin2)
    #                 if soc_val != 0:
                early_time = extract_time(early, time_dictionary) 
                late_time = extract_time(late, time_dictionary)              
    #             Draw up list of intersections
    #             intersections.append((first[0], second[0], bin1, bin2, list(intersection)))
    #                 f0.write('%d , %d , %d , %d, %s' % (first[0], second[0], bin1, bin2, list(intersection)))
    #                 f0.write('%d , %d , %d , %d, %d, %d, %d, %s' % (early, bin1, late, bin2, early_time, late_time, soc_val, list(intersection)))
                f0.write('%d , %d , %d , %d, %d, Hashtag, %d' % (early, bin1, late, bin2, early_time, soc_val))
                f0.write('\n')
    return ('Combination cascade printed')


def csv_hash_cascade(json_folder):
    '''
    Final method using hashtag cascade method with earliest time
    Output = root message_ID; target message_ID ; time for root ID; time for target Id ; shared hashtag combination
    Combines all shared text hashtag values
    '''
    final_dictionary = select_final_dict(json_folder)
    hashtag_dictionary = select_hashtag_dict(json_folder)
    doubles_dictionary = sel_double_htags(hashtag_dictionary)
    time_dictionary = select_time_dict(json_folder)
    userid_dictionary = select_userid_dict(json_folder)
    
    cascade_dictionary = {}
    
#     Ideal for retrieving other values from dictionaries.
    for key, value in final_dictionary.items():
        if key in doubles_dictionary:
            cascade_dictionary[key] = value

    dd = defaultdict(list)
    
    for k, v in doubles_dictionary.items():
        dd[tuple(v)].append(k)
#     print(dd)
#     new_casc_dict = dict(dd)

#     New  method for creating listing for cascade printing.
    output_dict = {textval: sorted(
                      [[key_ID, final_dictionary[key_ID][1]]
                      for key_ID in dd[textval]
                      if key_ID in final_dictionary],
                    key=lambda x: x[1])
           for textval in dd}
    f0 = open('.../no_conn_cascade.csv','w') #files to open when writing to the csv files
    f1 = open('.../social_conn_cascade.csv','w') #file without social connections

    for textval, entries in output_dict.items():
        list_for_output = entries if len(entries) == 1 else entries[1:]

        for item in list_for_output:
            bin1 = extract_userid(entries[0][0], userid_dictionary)
            bin2 = extract_userid(item[0], userid_dictionary)
            soc_val = determine_social_value(bin1, bin2)
#             print('%d ; %d ; %d ; %d ; %s' % (entries[0][0], item[0],
#                                               entries[0][1], item[1], list(textval)))
            
            if soc_val ==1:
                f1.write('%d , %d , %d , %d, %d, %d, %d' % (entries[0][0], item[0], entries[0][1], item[1], bin1, bin2, soc_val))
                f1.write('\n')
            else:
                f0.write('%d , %d , %d , %d, %d, %d, %d' % (entries[0][0], item[0], entries[0][1], item[1], bin1, bin2, soc_val))
                f0.write('\n') 
    f0.close()
    f1.close()
    return ('Socially and None connected cascades completed')


def csv_hashntime_cascade(json_folder):
    '''
    Method using hashtags to output social connection and time
    Output = root message_ID; target message_ID ; time for root ID; time for target Id ; social connection
    ; number of shared hashtags, shared hashtag set combination
    '''
    final_dictionary = select_final_dict(json_folder)
    hashtag_dictionary = select_hashtag_dict(json_folder)
    doubles_dictionary = sel_double_htags(hashtag_dictionary)
    userid_dictionary = select_userid_dict(json_folder)
    
    cascade_dictionary = {}
    
#     Ideal for retrieving other values from dictionaries.
    for key, value in final_dictionary.items():
        if key in doubles_dictionary:
            cascade_dictionary[key] = value

    dd = defaultdict(list)
    
    for k, v in doubles_dictionary.items():
        dd[tuple(v)].append(k)
#     print(dd)
#     new_casc_dict = dict(dd)

#     New  method for creating listing for cascade printing.
    output_dict = {textval: sorted(
                      [[key_ID, final_dictionary[key_ID][1]]
                      for key_ID in dd[textval]
                      if key_ID in final_dictionary],
                    key=lambda x: x[1])
           for textval in dd}
    f = open('.../full_cascade.csv','w')
    
#     userid_dict ={}
    
    for textval, entries in output_dict.items():
        list_for_output = entries if len(entries) == 1 else entries[1:]
        for item in list_for_output:
            bin1 = extract_userid(entries[0][0], userid_dictionary)
            bin2 = extract_userid(item[0], userid_dictionary)
            soc_val = determine_social_value(bin1, bin2)
#             print('%d ; %d ; %d ; %d ; %s' % (entries[0][0], item[0],
#             entries[0][1], item[1], list(textval)))
            
                            
            f.write('%d , %d , %d , %d' % (entries[0][0], item[0], entries[0][1], item[1]))
            f.write('\n') 
    f.close()
    print('Full cascade file printed')
# #     print(userid_dict)
    pass


def casc_creator(json_folder):
    '''
    Creating cascade list in specified cascadelist folder and pdf files for reading
    '''
    final_dictionary = select_final_dict(json_folder)
    hashtag_dictionary = select_hashtag_dict(json_folder)
    doubles_dictionary = sel_double_htags(hashtag_dictionary)
    time_dictionary = select_time_dict(json_folder)
    
    cascade_dictionary = {}
    
#     Ideal for retrieving other values from dictionaries.
    for key, value in final_dictionary.items():
        if key in doubles_dictionary:
            cascade_dictionary[key] = value

    dd = defaultdict(list)
    
    for k, v in doubles_dictionary.items():
        dd[tuple(v)].append(k)
#     print(dd)
#     new_casc_dict = dict(dd)
#     for values in new_casc_dict.values():
#         print(values)


    output_dict = {textval: sorted(
                      [[key_ID, final_dictionary[key_ID][1]]
                      for key_ID in dd[textval]
                      if key_ID in final_dictionary],
                    key=lambda x: x[1])
           for textval in dd}

    for textval, entries in output_dict.items():
        list_for_output = entries if len(entries) == 1 else entries[1:]
        for item in list_for_output:
            print('%d ; %d ; %d ; %d ; %s' % (entries[0][0], item[0],
            entries[0][1], item[1], list(textval)))
#     Writing cascades to CSV file
    count =0
    new_dictionary = {}
    for key, value in dd.items():
        for v in value:
            print(key, v)
#             for fkey, fvalue in cascade_dictionary():
#                 if v in cascade_dictionary:
#                     new_dictionary[v] = fvalue
        df = pd.DataFrame(value)
#         Insert iterator over different columns to find values.
        for index, columns in df.iteritems():
            print(index)
            print('####')
            print(columns)
            count+=1
#         Direction to cascade folder 
        df.to_csv('.../cascadelist/' + \
                   'casc__' + '_'.join(key) + '.csv', index=False)
    print(count)   
        
# #     Writing two or more hashtag dictionary
    with open('.../Two_or_more_hts_results.csv', 'w') as f:
        w = csv.writer(f, delimiter =';')
        w.writerows(doubles_dictionary.items())
        print('Print IDs with two or more hashtags completed')            

# #     Creating CSV 
#     with open('/Users/benjaminsenyonyi/Documents/Masters course/Sem 4/new_workspace/hashtag-project/csv_folder/cascades/Cascade_dictionary_results.csv', 'w') as f:
# #         w = csv.DictWriter(f, cascade_dictionary.values())
#         w = csv.writer(f, delimiter =';')
#         w.writerows(cascade_dictionary.values())
#         print('Cascade Dictionary completed')
#      
#  
#  
#     Using pandas for the final cascade dictionary CSV   
    data_file = pd.DataFrame(cascade_dictionary).transpose().reset_index()
    data_file.columns = ['message_id' , 'Hashtags', 'Time', 'user_id']
    data_file.groupby('Hashtags')
    data_file.set_index('message_id', inplace = True)
    data_file.to_csv('.../casc_dict_file.csv')
#     diff_file = data_file.diff(axis=1)
#     diff_file.to_csv('.../diff_file.csv')
    print('Pandas cascade dictionary file completed')   
    
#     Writing default dictionary to file
    f = open('.../DefaultDictionary.txt','w')
    f.write('Unique List :\r\n'+str(dd) + '\r\n\r\n') 
    f.close()
    print('File Printing Completed')
    
    return sorted(cascade_dictionary.items())

def old_creator(json_folder):
    '''
    Unused old methods
    '''
    hashtag_dictionary = select_hashtag_dict(json_folder)
    doubles_dictionary = sel_double_htags(hashtag_dictionary)
    
    
    for value in doubles_dictionary.values():
#         List of all keys found in the dictionary ++++ 
        allkeys = []
        for key in doubles_dictionary.keys():
            if doubles_dictionary[key] == value:
                allkeys.append(key)
        print(value, '---->' , allkeys)
    
    count =0
    value_dict = {}
    val_list = []
    for key, value in doubles_dictionary.items():
#         print(value)

#         for list_val in value:
#             if list_val in final_dictionary:
#                 for k,v in final_dictionary.items():
#                     fin_casc_dict[value]= v
        for v in doubles_dictionary.values():
            if v == value:
                count +=1
                val_list.append(v)
    print(count)
    print(val_list)
    
    cascade_dictionary = {}
    for key, value in cascade_dictionary.items():
        count = 0
        for k,v in cascade_dictionary.items():
            if value == v:
                fname = "file" + str(count)
                count[k] = value
                print(count)
                count+=1       
    pass



