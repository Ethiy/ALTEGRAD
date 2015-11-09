from numpy import *
import matplotlib.pyplot as plt

# Load the distance matrix
D = loadtxt('distanceMatrix.csv', delimiter=',')
cities = ['Atl','Chi','Den','Hou','LA','Mia','NYC','SF','Sea','WDC']
nCities = D.shape[0] # Get the size of the matrix


k = 2 # e.g. we want to keep 2 dimensions


#================= ADD YOUR CODE HERE ====================================
## TODO: Implement MDS
#
# Instructions: Use MDS to reduce the dimensionality of the data
#				while preserving the distances between all pairs
#				of points. Use the steps given in the description 
#				of the assignment. Initially, calculate matrix J
# 				and subsequently, matrix B. Perform SVD decomposition
#				of B. Calculate new representation. Save the new 
#				representation in variable X


D=pow(D,2);
J=eye(nCities)- 1.0/nCities * ones(nCities);
B=-.5*dot(J,dot(D,J));
U,S,V=linalg.svd(B);

Uk=U[:,:k];
Sk=S[:k];
sqrtSk=pow(Sk,0.5);

X=dot(Uk,diag(sqrtSk));




#=================================================================


# Plot distances in two dimensions
plt.figure(1)

# Plot cities in 2D space
plt.subplot(121)
plt.plot(-X[:,0],-X[:,1],'o')
for i in range(len(cities)):
     plt.text(-X[i,0], -X[i,1]+1.5, cities[i], color='k', ha='center', va='center')

# Plot also a US map
plt.subplot(122)
im = plt.imread("usamap.png")
implot = plt.imshow(im,aspect='auto')
plt.axis('off')
plt.show()


