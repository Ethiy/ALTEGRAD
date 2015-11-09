import networkx as nx
import matplotlib.pyplot as plt 
import numpy as np 
#from future import division

R = nx.fast_gnp_random_graph(200, 0.1);


plt.figure(5);
plt.plot(R,'b-',marker='o');
plt.ylabel("Frequency");
plt.xlabel("Degree");
plt.show();
plt.title("blabla");

degree_sequence = R. degree().values();

t_R=nx.triangles(R);

t_R_values = sorted(set(t_R.values()));
t_R_hist = [t_R.values().count(x) for x in t_R_values];

nx. average_clustering (R);

# Degree centrality
deg_R_centrality = nx.degree_centrality (R);
# Eigenvector centrality
eig_R_centrality = nx.eigenvector_centrality (R);

# Sort centrality values
sorted_deg_R_centrality = sorted(deg_R_centrality.items());
sorted_eig_R_centrality = sorted(eig_R_centrality.items());
# Extract centralities
deg_R_data=[b for a,b in sorted_deg_R_centrality];
eig_R_data=[b for a,b in sorted_eig_R_centrality];


# Kronecker graph model

A1 = np.array([0.99, 0.26], [0.26, 0.53]);
A_G=A1;

for i in range(10):
	A_G = np.kron(A_G,A_1);


# Create adjacency matrix
for i in range(A_G.shape[0]):
	for j in range(A_G.shape[1]):
		if random.random() <= A_G[i][j]:
			A_G[i][j] = 1;
		else:
			A_G[i][j] = 0;

# Convert adjacency matrix to graph 
G_kron=nx.from_numpy_matrix(A_G, create_using=nx.Graph() );

degree_sequence_random = G_kron.degree().values();
print "Min degree" , np.min(degree_sequence_random)
print "Max degree" , np.max(degree_sequence_random)
print "Median degree" , np.mmedian(degree_sequence_random)
print "Mean degree" , np.mean(degree_sequence_random)

# ============ Part 2:Community Detection

z=nx.read_gml(”karate.gml”)


