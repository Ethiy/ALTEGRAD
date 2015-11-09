import networkx as nx

# Define the function of modularity

def modularity(G, clustering ):
	# Add the body of the function here
	return modularity



# Use the main function as it follows
G = nx.read gml(”karate.gml”)

# Different clustering solutions

clustering = []
clustering.append( [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 1 , 0 , 0 , 0 , 0 , 1 , 1 , 0 , 0 , 1 , 0 , 1 , 0 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ] )
clustering.append( [ 0 , 1 , 0 , 1 , 0 , 0 , 1 , 0 , 1 , 1 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 1 , 1 , 0 , 1 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 , 0 , 1 ] )
clustering.append( [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 1 , 1 , 0 , 0 , 1 , 0 , 1 , 0 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 0 , 1 , 1 ] )

# Compute modularity for each case and print the graph
for i in range(len(clustering )):
	print modularity(G,clustering[i])
	nx.draw(G,pos=nx.spring layout(G), node color=clustering[i]) 
	plt .show()