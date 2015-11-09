import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy
from scipy.spatial import distance

# Load and plot graph
plt.figure(1);
z=nx.read_gml('../karate.gml');
pos=nx.spring_layout(z);
nx.draw_networkx(z,pos);
plt.show();

# Create the distance matrix
path_length=nx.all_pairs_shortest_path_length(z) 
n = len(z.nodes())
distances=np. zeros ((n,n))

for u,p in path_length.iteritems(): 
	for v,d in p. iteritems ():
		distances[int(u)-1][int(v)-1] = d 

hier = hierarchy.average( distances )
plt.figure(2)
hierarchy.dendrogram(hier)
plt.show()