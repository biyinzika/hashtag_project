'''
Created on 19 Oct 2018

@author: benjaminsenyonyi
'''
import os
import glob
import csv
# import pandas as pd


def det_follower_conn(userID, check_id):
    '''
    Takes two user IDs and returns a binary value on relationship.
    can return a list of followers of that user.
    '''
    
    sg_directory = ".../social-graph-iswc/followerdata"
    prefix = "followers"
    val_ret = False
    check_id = str(check_id)
    for root, dirs, files in os.walk(sg_directory):
#         Run over files in the followers directory
        for file in files:
            if (file == prefix + str(userID) + ".csv") :  #Select the specific file
                    user_file = file
                    new_f = os.path.join(root, user_file)
                    with open(new_f) as csvfile:
                        reader = csv.reader(csvfile)
                        next(reader) #Skip first line because it is date and time (irrelevant) data.
                        for row in reader:
                            for field in row:
                                if field == check_id:
#                                     Return the binary value here
                                    val_ret=True        
    return val_ret

def det_friend_conn(userID, check_id):
    '''
    Takes two user IDs and returns a binary value on the connection. 
    Can return a list of friends of that user.
    '''
    
    sg_directory = ".../social-graph-iswc/frienddata"
    prefix = "friends"
    val_ret = False
    check_id = str(check_id)
    for root, dirs, files in os.walk(sg_directory):
#         Run over files in the followers directory
        for file in files:
            if (file == prefix + str(userID) + ".csv") :  #Select the specific file
                    user_file = file
                    new_f = os.path.join(root, user_file)
                    with open(new_f) as csvfile:
                        reader = csv.reader(csvfile)
                        next(reader) #Skip first line because it is date and time (irrelevant) data.
                        for row in reader:
                            for field in row:
                                if field == check_id:
#                                     Return the binary value here
                                    val_ret=True
#             else:
#                 print("No user file with that number found")
    return val_ret

# Main method to check code
if __name__ == '__main__':
    sg_directory = ".../social-graph-iswc/followerdata"
    filelist = []
    prefix = "followers"
    userID = 2310416978
    user2  = 2892407547
    user3 = "%s" %user2
    val_ret = False
    print(user3)
    for root, dirs, files in os.walk(sg_directory):
#         Run over files in the followers directory
        for file in files:
            if (file == prefix + str(userID) + ".csv") :  #Select the specific file
                    user_file = file
                    new_f = os.path.join(root, user_file)
                    with open(new_f) as csvfile:
                        reader = csv.reader(csvfile)
                        next(reader) #Skip first line because it is date and time (irrelevant) data.
                        for row in reader:
                            for field in row:
                                if field == user3:
#                                     Return the binary value here
                                    print('###########################################')
                                    val_ret=True
    print(val_ret)                     
    pass
