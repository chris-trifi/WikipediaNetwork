# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 13:53:22 2020

@author: chris
"""
import networkx as nx
import wikipedia

G=nx.DiGraph()
#mylist = (wikipedia.page("Gödel's incompleteness theorems").links)

  
queue = []      
def visit(i):
    queue.append(i)
    G.add_node(i)

def FilterIdentifiers(i):      #filters out identifiers like ISBN that are not related 
    a = i.find("identifier")
    a+=1
    return a

def bfs(s,halt): #depth first search of wikipedia hyperlink network
        counter = 0
        visit(s)
        while queue:
            s = queue.pop(0)
            counter +=1
            print(counter)
            if counter > halt: #halting point
                break
            # Get all adjacent vertices of the dequeued vertex s. If a 
            # adjacent has not been visited, then visit it.
            try:
                mylist = (wikipedia.page(s).links)
            except wikipedia.exceptions.WikipediaException:
                print("error for id:" + s)
            for i in mylist:
                if i not in G.nodes() and FilterIdentifiers(i)==0:
                    visit(i)
                if (s,i) not in  G.edges() and FilterIdentifiers(i)==0:
                   G.add_edge(s , i)
                          
        
bfs("Gödel's incompleteness theorems", 300)   

#print("radius:" , min(nx.eccentricity(G)))

print("average clustering:", nx.average_clustering(G))

nx.write_gexf(G, "graph.gexf")