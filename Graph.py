#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import heapq, collections

### Graphs, vertices, edges
# This `DirectedGraph` class uses the adjacency list representation: a list of vertices, and each 
# vertex contains a list of its neighbours. This code also uses some cunning Python tricks...

# * We define a class `DirectedGraph`. We also define another class `Vertex`, within 
# `DirectedGraph`. Every Python name lives somewhere. If 
# there has to be a class `Vertex`, it has to belong somewhere, and if (as in this case) 
# we don't expect that other functions will create new `Vertex` objects, it makes sense 
# to put it inside `DirectedGraph`. Python doesn't have access modifiers like public or 
# private, and other code can still refer to it as `DirectedGraph.Vertex`; Python's 
# attitude is "we're all adults here".

# * The function name `__init__` denotes the constructor. The first argument is the object 
# that is in the process of being constructed.

# * Another magic function is `__str__`. This function is invoked whenever you call `print(g)`. 
# It's helpful for debugging to print out something informative.

# * I want to allow vertices to have custom attributes, e.g. breadth first search uses `v.seen`, 
# Dijkstra's algorithm uses `v.distance`. Python allows 'monkey patching', i.e. adding attributes 
# to an object after it has been created. You don't need to declare all member variables 
# in advance. Internally, Python sees each object as just an arbitrary dictionary. There is a 
# convention that one should declare all member variables in the constructor, but this is only for 
# readabilty, not a requirement of the language.

# * This class distinguishes between vertex ids and vertex objects. Vertex ids are passed in when the 
# graph is created, e.g. `DirectedGraph([('a','b'), ('b','c'), ('b','a')])`, where `a` etc. are vertex
# ids. Then, `Vertex` objects are created, one for each vertex id, and it is those objects which 
# have neighbours and other attributes like `seen` or `distance`.

# * For some graphs we want to store e.g. a weight for each edge. For other graphs, there is nothing 
# to store. This class permits either. The special syntax `*label` means 0 or 1 or more values.

class DirectedGraph:
    '''A directed graph, where edges is a list of (start_vertex, end_vertex, *label)'''
    def __init__(self, edges):
        src,dst = zip(*[e[:2] for e in edges])
        self.vertex = {k: DirectedGraph.Vertex(k) for k in set(src+dst)}
        for u,v,*label in edges:
            vv = self.vertex[v]
            self.vertex[u].neighbours.append((vv,*label) if len(label)>0 else vv)
        self.vertices = self.vertex.values()
        self.edges = [(self.vertex[u], self.vertex[v], *label) for u,v,*label in edges]

    class Vertex:
        def __init__(self, id_):
            self.id = id_
            self.neighbours = []
        # By providing these two magic methods, vertex objects will print out
        # nicely. Python has a whole list of magic methods that one can override:
        # https://docs.python.org/3/reference/datamodel.html#basic-customization
        def __str__(self):
            return str(self.id)
        def __repr__(self):
            return f"v[{repr(self.id)}]"


class UndirectedGraph(DirectedGraph):
    def __init__(self, edges):
        e1 = set(e[:2] for e in edges)
        e2 = set(e[1::-1] for e in edges)
        if (e1 & e2): raise ValueError("Both directions present")
        edges2 = edges + [(v,u,*a) for u,v,*a in edges]
        super().__init__(edges2)
        self.edges = [(self.vertex[u], self.vertex[v], *label) for u,v,*label in edges]

