'''
Created on 27 Sep 2018

@author: benjaminsenyonyi
'''

import matplotlib.pyplot as plt
import numpy as np

def drawloggraph(g_list):
    plt.plot(g_list)
#     plt.title('Logged Hashtag Frequency')
    plt.ylabel('Frequency of hashtags')
    plt.yscale('log')
    plt.xlabel('Hashtags used per message')
    plt.show()

def drawgraph(g_list):
    plt.plot([0,1,2,3,4,5,6,7,8,9,10], g_list, 'ro')
#     plt.plot(g_list)
#     plt.xticks([0,1,2,3,4,5,6,7,8,9,10])
#     plt.title('Hashtag Frequency')
    plt.ylabel('Frequency of hashtags')
    plt.xlabel('Hashtags used per message')
    plt.show()

if __name__ == '__main__':  
    input_data = [7,5,6]
    green_diamond = dict(markerfacecolor='b', marker='D')
    plt.boxplot(input_data, flierprops=green_diamond)
    
    plt.title('Betweenness Centrality')
    
    plt.ylabel('')
    plt.xlabel('')
#     plt.xlabel('')
    plt.show()
    pass