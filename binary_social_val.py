'''
Created on 7 Dec 2018

@author: benjaminsenyonyi
'''
from social_connection import det_follower_conn, det_friend_conn


def determine_social_values(userID, check_id):
    '''
    Return rank value showing result of social connection
    
    check_id NOT ON LISt     --> 0
    check_id = friend        --> 1
    check_id = follower      --> 2
    both friend and follower --> 3
    check_id = userid        --> 4
    
    '''

    bin_value = 100
    
    if userID == check_id:
        bin_value = 4
    else:
        fol_val= det_follower_conn(userID, check_id)
        friend_val=det_friend_conn(userID, check_id)
        
        if fol_val and friend_val:
            bin_value = 3
        elif fol_val and not friend_val:
            bin_value = 2
        elif not fol_val and friend_val:
            bin_value = 1
        elif not fol_val and not friend_val:
            bin_value = 0
    return bin_value


def determine_social_value(userID, check_id):
    '''
    Old method
    Return binary value on result of social connection
    '''
#     If user id == check_id else all
    
    bin_value = 100
    
    if userID == check_id:
        bin_value = 1
    else:
        fol_val= det_follower_conn(userID, check_id)
        friend_val=det_friend_conn(userID, check_id)
#         print("Follower value : " + str(fol_val))
    #     print("friend value : " + str(friend_val))
        if fol_val or friend_val == 1:
            bin_value = 1
        else:
            bin_value = 0
    return bin_value  