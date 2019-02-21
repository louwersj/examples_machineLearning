import numpy as np
import matplotlib.pyplot as plt
#from matplotlib import style
#style.use("ggplot")
from sklearn.cluster import KMeans

value_x = [1, 5, 1.5, 8, 1, 9, 3, 5, 2, 7, 4, 6, 9, 6, 3, 1, 9]
value_y = [2, 8, 1.8, 8, 0.6, 11, 2, 6, 3, 8, 5, 9, 2, 5, 1, 8, 5]


# build a np array based upon value_x and value_y
X = np.column_stack((value_x, value_y))

# state the number of clusters we do want to find.
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_

print(centroids)
print(labels)

#plt.scatter(x,y)
#plt.savefig('test2.png')


colors = ["g.","r.","c.","y."]

for i in range(len(X)):
    print("coordinate:",X[i], "label:", labels[i])
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10)


plt.scatter(centroids[:, 0],centroids[:, 1], marker = "x", s=150, linewidths = 5, zorder = 10)

plt.savefig('test3.png')