from numpy import *
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import rc

# Load the "gatlin" image data
X = loadtxt('gatlin.csv', delimiter=',')

#================= ADD YOUR CODE HERE ====================================
# Perform SVD decomposition
## TODO: Perform SVD on the X matrix
# Instructions: Perform SVD decomposition of matrix X. Save the 
#               three factors in variables U, S and V
#

U,S,V=linalg.svd(X);

#=========================================================================

# Plot the original image
plt.figure(1)
plt.imshow(X,cmap = cm.Greys_r)
plt.title('Original image (rank 480)')
plt.axis('off')
plt.draw()


#================= ADD YOUR CODE HERE ====================================
# Matrix reconstruction using the top k = [10, 20, 50, 100, 200] singular values
## TODO: Create four matrices X10, X20, X50, X100, X200 for each low rank approximation
## using the top k = [10, 20, 50, 100, 200] singlular values 
#

#X10 construction
U10=U[:,:10];
V10=V[:10,:];
S10=S[:10];
X10=dot(U10,dot(diag(S10),V10));

#X20 construction
U20=U[:,:20];
V20=V[:20,:];
S20=S[:20];
X20=dot(U20,dot(diag(S20),V20));

#X50 construction
U50=U[:,:50];
V50=V[:50:];
S50=S[:50];
X50=dot(U50,dot(diag(S50),V50));

#X100 construction
U100=U[:,:100];
V100=V[:100,:];
S100=S[:100];
X100=dot(U100,dot(diag(S100),V100));

#X200 construction
U200=U[:,:200];
V200=V[:200,:];
S200=S[:200];
X200=dot(U200,dot(diag(S200),V200));



#=========================================================================



#================= ADD YOUR CODE HERE ====================================
# Error of approximation
## TODO: Compute and print the error of each low rank approximation of the matrix
# The Frobenius error can be computed as |X - X_k| / |X|
#

Error10=linalg.norm(X-X10)/linalg.norm(X);
print Error10;

Error20=linalg.norm(X-X20)/linalg.norm(X);
print Error20;

Error100=linalg.norm(X-X100)/linalg.norm(X);
print Error100;

Error200=linalg.norm(X-X200)/linalg.norm(X);
print Error200;


#=========================================================================



# Plot the optimal rank-k approximation for various values of k)
# Create a figure with 6 subfigures
plt.figure(2)

# Rank 10 approximation
plt.subplot(321)
plt.imshow(X10,cmap = cm.Greys_r)
plt.title('Best rank' + str(5) + ' approximation')
plt.axis('off')

# Rank 20 approximation
plt.subplot(322)
plt.imshow(X20,cmap = cm.Greys_r)
plt.title('Best rank' + str(20) + ' approximation')
plt.axis('off')

# Rank 50 approximation
plt.subplot(323)
plt.imshow(X50,cmap = cm.Greys_r)
plt.title('Best rank' + str(50) + ' approximation')
plt.axis('off')

# Rank 100 approximation
plt.subplot(324)
plt.imshow(X100,cmap = cm.Greys_r)
plt.title('Best rank' + str(100) + ' approximation')
plt.axis('off')

# Rank 200 approximation
plt.subplot(325)
plt.imshow(X200,cmap = cm.Greys_r)
plt.title('Best rank' + str(200) + ' approximation')
plt.axis('off')

# Original
plt.subplot(326)
plt.imshow(X,cmap = cm.Greys_r)
plt.title('Original image (Rank 480)')
plt.axis('off')

plt.draw()


#================= ADD YOUR CODE HERE ====================================
# Plot the singular values of the original matrix
## TODO: Plot the singular values of X versus their rank k

plt.figure(3)
plt.plot(linspace(1,S.size,S.size),S)
plt.draw();


#=========================================================================

plt.show() 

