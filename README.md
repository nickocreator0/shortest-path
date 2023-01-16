# shortest-path
# A simple investigation on two greedy algortihms and calculating running times when being implemented.

## Motivation
This is a project done for the purpose of Advanced Algorithms course the final project.

## Files
This project contains two parts
First, follwoing files that are associated with FloydWarshall algorithm implementation:
FloydWarshall.py
FW_test.py
RunningTimePlot.py

Second, files implementing Dijkstra's algorithm using Fibonacci Heap.
Dijkstra_FiboHeap.py
fibheap.py
Graph.py

**Note** To run 'Dijkstra_FiboHeap.py' without errors, you have to pip install these libraries:
numpy, matplotlib, mpl_toolkits, seaborn, sklearn.
Also, you need to have 'Graph.py' and 'fibheap.py' in the same directory as your project's file. 

## Features
'Dijkstra_FiboHeap.py' contains a 'time_taken_func' that returns the time taken for dijkstra call for a single graph of arbitraty size. 
'Dijkstra_FiboHeap.py' contains a 'plot_growth_rate' function that plots the visualizations needed to investigate the running time with regard to the input size.

## How To Use

###About Dijkstra_FiboHeap.py: To get shortest distances from a specific sourse in Dijkstra_FiboHeap.py, 'dijkstra' fucntion needs to be called with a 'DirectedGraph' object and a source vertex which can be an id for a vertex and is treated as a vertex object in DirectedGraph class implemented in Graph.py. An example of how to initialize this object is given below:

graph = DirectedGraph([(0,1,4), (1,2,8)]) 

time_taken_func function 
Takes the number of vertices you'd like your graph to have and produces a graph with that many vertices and random number of edges with random costs. Then calls 'dijkstra' function and calculates the running time of dijkstra for that specific number of vertices it has been given.

plot_growth_rate function
It can help you find a functional relationship between a list and two others by returning the coefficients forming that relation. The lists mean for this function's input arguments are Running Times for different inputs, number of vertices and number of edges. The goal was to know whether the funtion is indeed O(E+V log V) as it was supposed to be or not. 

All the other files are already given the inputs in the main functions. 

## Credits
Graph.py and FiboHeap.py have been extracted from a project done in the Advanced Algorithms in Cambridge University. 
The link can be found here respectively ("https://gitlab.developers.cam.ac.uk/djw1005/algorithms/-/blob/master/ucamcl_alg_utils.py") , 
("https://gitlab.developers.cam.ac.uk/djw1005/algorithms/-/blob/master/fibheap.py")
