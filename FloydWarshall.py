#!/usr/bin/env python
# coding: utf-8

# In[1]:


from copy import copy, deepcopy

def floyd_warshall(matrix):
    #kth iteration
    n = len(matrix)
    distances = copy(matrix)
    #Iterate through intermediate vertices
    for k in range(n):   
        #Iterate through rows
        for i in range(n):
            #Iterate through columns
            for j in range(n):
                distances[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
    return distances

