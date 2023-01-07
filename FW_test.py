#!/usr/bin/env python
# coding: utf-8

# In[8]:


import math
from FloydWarshall import floyd_warshall

#Checks if the input inserted by the user is valid for a distance
def user_input_check(user_input):
    flag = False                 
    try:
        val = int(user_input)   
        flag = True              
    except ValueError:           
        if user_input == 'inf':  
            flag = True         
        else:                   
            #1 operation
            print(f"Please enter a valid input\n hint: Only integer and inf are allowed!")
    return flag  


# In[2]:


#Input collection from user 

def distance_entry():
    #Get the number of vertices from user
    n = int(input(f"Enter the number of vertices:"))

    D_mat = []
    
    #Row-wise insertion
    for i in range(n):
        print(f"Enter the distances between vertix {i+1} and other nodes:\n") 
        print(f"***Type inf in case of no edge***\n")
        temp = []
        for j in range(n): 
            user_input = input()
            while(user_input_check(user_input) == False):
                user_input = input() 
            if user_input == 'inf':
                #Populate the rows
                temp.append(math.inf)
            else:
                temp.append(int(user_input))
        D_mat.append(temp)
        
    return D_mat


# In[3]:


# Print the solution
def print_distances(matrix):
    n = len(matrix)
    print(f"\n\nResulted Distance Matrix from Floyd-Warshall:")
    for i in range(n):
        for j in range(n):
            if(matrix[i][j] == math.inf):
                print(f"inf", end = ' ')
            else:
                print(matrix[i][j], end = ' ')
        print("\n")


# In[10]:


###Uncommonet the following line to get a matrix from user input###
#print_distances(floyd_warshall(distance_entry()))
###################################################################

