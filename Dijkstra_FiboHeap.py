#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Dijksta's Algorithm with Fibonacci Heap - without Decrease-Key
#Author: Nicko.Creator0
#December 2022


# In[ ]:


#Required Libraries
import numpy as np
from sklearn.linear_model import LinearRegression
from Graph import DirectedGraph
from fibheap import FibHeap
import time
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#Dijkstra's algorithm with Fibonacci Heap
def dijkstra(graph, source):
    dist = {}
    for v in graph.vertices:
        v.distance = float('inf')
    source.distance = 0
    to_explore = FibHeap([source], sortkey = lambda v: v.distance)

    while not to_explore.is_empty():
        v = to_explore.popmin()
        #Assertion: v is never put back into to_explore
        for neighbor, edge_cost in v.neighbours:
            new_dist = v.distance + edge_cost
            if new_dist < neighbor.distance:
                neighbor.distance = new_dist
                if neighbor in to_explore:
                    to_explore.decreasekey(neighbor)
                else:
                    to_explore.push(neighbor)
    for v in graph.vertices:
        dist[v.id] = v.distance
    return dist


# In[3]:



#Testing
#With adjancency matrix below
#It's given to dijkstra as a directed graph though
#graph = 0, 4,  0,  0,  0,  0,  0,  8,  0 
#        4, 0,  8,  0,  0,  0,  0,  11, 0 
#        0, 8,  0,  7,  0,  4,  0,  0,  2 
#        0, 0,  7,  0,  9,  14, 0,  0,  0 
#        0, 0,  0,  9,  0,  10, 0,  0,  0 
#        0, 0,  4,  14, 10, 0,  2,  0,  0
#        0, 0,  0,  0,  0,  2,  0,  1,  6 
#        8, 11, 0,  0,  0,  0,  1,  0,  7
#        0, 0,  2,  0,  0,  0,  6,  7,  0 

"""graph = DirectedGraph([(0,1,4), (0,7,8), (1,0,4), (1,7,11), (1,2,8), (2,1,8),
                       (2,8,2), (2,5,4), (2,3,7),(3,2,7),(3,5,14), (3,4,9),
                       (4,3,9),(4,5,10),(5,4,10),(5,3,14),(5,2,4),(5,6,2),(6,5,2),
                       (6,8,6),(6,7,1),(7,0,8),(7,1,11),(7,8,7),(7,6,1),(8,7,7),
                       (8,2,2),(8,6,6), (9, 2, 6)])

time_log = {}
#Call Dijkstra n = 10
t0 = time.time()
dijkstra(graph, graph.vertex[0])
time_taken = time.time() - t0
time_log[10] = time_taken"""

time_log = []
in_vertices = []
in_edges = []

#input_size = 1000

def time_taken_func(in_):
    num_vertices = in_
    edges = []
    for i in range(num_vertices):
        num_neighbours = random.randint(0, num_vertices-1)
        neighbours = random.sample(range(num_vertices), num_neighbours)
        costs = random.sample(range(num_vertices), num_neighbours)
        for neighbour in neighbours:
            for cost in costs:
                edges.append((i, neighbour, cost))
    #Create the Directed Graph
    graph = DirectedGraph(edges)
    t0 = time.time()
    #Call Dijkstra
    dijkstra(graph, graph.vertex[0])
    time_taken = time.time() - t0
    #keep log
    in_edges.append(len(edges))
    in_vertices.append(num_vertices)
    time_log.append(time_taken)
    #time_log[input] = time_taken
    return time_taken

#Display the distances 
#dijkstra(graph, graph.vertex[0])
#for i,v in enumerate(graph.vertices):
#    print(f"{i} Shortest distance from 0 to {v} is {v.distance}")


# In[4]:


def plot_growth_rate(t_log, in_v, in_e):
    # Create a figure and a 3D Axes object
    fig = plt.figure(facecolor = 'black')
    ax = fig.add_subplot(111, projection = '3d', facecolor = 'black')


    # Plot the running time as a function of the number of vertices and edges
    ax.scatter(in_v, in_e, t_log, color = 'maroon')
    ax.set_xlabel('# of Vertices', color = 'silver')
    ax.set_ylabel('# of Edges', color = 'silver')
    ax.set_zlabel('Running Time', color = 'yellow')
    ax.set_title('Running Time vs. Number of Vertices and Edges', color = 'white')

    plt.show()
    
    #Time vs. number of vertices
    # Set the style of the plot
    sns.set_style('darkgrid', {'grid.color': 'gray', 'axes.facecolor': 'black'})

    # Create a figure and an Axes object
    fig, ax = plt.subplots()

    # Plot time_log as a function of in_vertices
    sns.lineplot(x=in_v, y=t_log, ax=ax, color='yellow', linestyle='dashed', marker='o', linewidth=3)

    # Add labels and title
    ax.set_xlabel('Number of Vertices', fontsize=14)
    ax.set_ylabel('Running Time', fontsize=14)
    ax.set_title('Running Time vs. Number of Vertices', fontsize=16)

    # Show the plot
    plt.show()

    # Create a figure and an Axes object
    fig, ax = plt.subplots()
    #Time vs. number of edges
    sns.lineplot(x=in_e, y=t_log, ax=ax, color='pink', linestyle='dashed', marker='o', linewidth=3)

    # Add labels and title
    ax.set_xlabel('Number of Edges', fontsize=14)
    ax.set_ylabel('Running Time', fontsize=14)
    ax.set_title('Running Time vs. Number of Edges', fontsize=16)

    # Show the plot
    plt.show()


# In[1]:


#plot_growth_rate(time_log, in_vertices, in_edges)


# In[6]:


#This code will perform a linear regression on the data 
#in time_log, in_vertices, and in_edges and print the 
#coefficients of the model. The coefficients represent 
#the relationship between the input variables (in_vertices and in_edges)
#and the output variable (time_log). Specifically, the coefficient 
#for in_vertices represents the change in time_log per unit change 
#in in_vertices, and the coefficient for in_edges represents the change
#in time_log per unit change in `in_ed

def functional_rel(t_log, in_v, in_e):
    # Convert the lists to numpy arrays
    X = np.array(in_v).reshape(-1, 1)
    Y = np.array(in_e).reshape(-1, 1)
    Z = np.array(t_log).reshape(-1, 1)

    # Combine the arrays into a single input array
    X = np.concatenate((X, Y), axis=1)

    # Create a Linear Regression model
    model = LinearRegression()

    # Fit the model to the data
    model.fit(X, Z)

    # Print the coefficients of the model
    print(model.coef_)

