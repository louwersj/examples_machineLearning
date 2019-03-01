import numpy as np
import matplotlib
matplotlib.use('Agg') #quick fix to select the backend and prevent MacOs issues
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# define two value set lists
value_x = [1, 5, 1.5, 8, 1, 9, 3, 5, 2, 7, 4, 6, 9, 6, 3, 1, 9]
value_y = [2, 8, 1.8, 8, 0.6, 11, 2, 6, 3, 8, 5, 9, 2, 5, 1, 8, 5]


# build a np array based upon list value_x and list value_y
X = np.column_stack((value_x, value_y))

# state the number of clusters we do want to find.
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

#define the centroids of the cluster and the labels
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

# set the colors to be used
colors = ["g.","r.","c.","y."]


# print to stdout and create a visual plot
print(centroids)
print(labels)

for i in range(len(X)):
    print("coordinate:",X[i], "label:", labels[i])
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10)
#    plt.plot(X[i][0], X[i][1], colors["g."], markersize = 10)

# use plt.scatter for a scatter chart which includes the cluster datapoints and the centroids
plt.scatter(centroids[:, 0],centroids[:, 1], marker = "x", s=150, linewidths = 5, zorder = 10)
#plt.scatter(centroids[:, 0],centroids[:, 1], marker = "", s=150, linewidths = 5, zorder = 10)

# ensure to save the scatterplot
plt.savefig('findClusterCenter_example_1.png')