#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Test FloydWarshal
#Import the required libraries and packages 
import numpy as np
import pandas as pd
import math 
import time
from FloydWarshall import floyd_warshall

###Uncommonet the following line to get a matrix from user input###
#print_distances(floyd_warshall(distance_entry()))
###################################################################

import matplotlib.pyplot as plt

def FW_time_plot(dimension):
    time_log = []
    #Tests running time of Floyd-Warshal with input sizes  
    #10*10 , 20*20, 30*30, ..., 100*100, ... dimension*dimension     
    input_size = []

    for index in range(dimension):
        if  index % 10 == 0 and index//10 > 1:
            #Assign the dimension
            dim = (index, index)
            #Creat a numpy array filled with zeros
            rand_mat = np.zeros(dim)
            #Generate the random int entries in the matrix
            rand_mat = np.random.randint(low = 0, high = 1000, size = (index, index))
            #Set the diagonal entries to zero
            rand_mat[range(index), range(index)] = 0
            #Set the t0 to before calling the Floyd-Warshall function
            t0 = time.time()
            (floyd_warshall(rand_mat))
            #Calculate the running time
            time_taken = time.time() - t0
            #Add the elapsed time for this matrix to the time_log dataset
            input_size.append(index)
            time_log.append(time_taken)


    plt.plot(input_size, time_log)
    plt.title('Floyd-Warshal Growth Rate (Arrays)')
    plt.xlabel('Input Size')
    plt.ylabel('Time')
    plt.show()

