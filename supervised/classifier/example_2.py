import numpy as np
import pydot
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.externals.six import StringIO

__author__ = "Johan Louwers"
__copyright__ = "Copyright 2019, Johan Louwers"
__license__ = "MIT"
__email__ = "louwersj@gmail.com"

''' 
    This example code is based upon an example provided by Google and showcases classifier used in a supervised  
    machine learning example. It will use the iris dataset provided as an example dataset by sklearn. the dataset 
    consists of 3 different types of irises (Setosa, Versicolour, and Virginica) petal and sepal length, stored in a 
    150x4 numpy.ndarray
    
    the example code is to provide insight into splitting data into training data and test data. Additionally you can 
    use the below example code to predict what type of iris a flower is based upon dimensions of petals and sepals. 
    
    Included in the example data is a solution to visualize the execution of the decission tree which will use the 
    pydot.graph_from_dot_data approach. Do note that this will require the installation of dot on your local operating 
    system. Dot comes with the installation of graphviz - for more information look at graphviz.org or look at the 
    following blog http://johanlouwers.blogspot.com/2019/01/solved-oserror-errno-2-dot-not-found-in.html 
    
    Do note that parts of the code are commented and you can remove the comments to understand more of the working of 
    the code. 
'''


# load the iris dataset which is imported from sklearn.datasets
iris = load_iris()

# uncomment the below code line to see all iris feature names. The feature names should be:
# ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
#print iris.feature_names


# uncomment the below code line to see all iris target names. The target names should be:
# ['setosa' 'versicolor' 'virginica']
#print iris.target_names


# uncomment the below code line to see the data associated with the first record in the iris dataset. The data shown
# will be the values for the sepal length (cm), sepal width (cm), petal length (cm) and petal width (cm).
#print iris.data[0]

# uncomment the below code line to see the target associated with the first record in the iris dataset. This should be
# the value 0, in this the value 0 represents 'Setosa'. In the entire dataset the irises are mapped like  0 = setosa,
# 1 = versicolor and 2 = virginica.
#print iris.target[0]


# uncomment the below 2 code lines to see all the records from the dataset including labels and features. Each record is
# shown in a fashion like this:
# Example 102: label: 2, feature [7.1 3.  5.9 2.1]
#for i in range(len(iris.target)):
#   print "Example %d: label: %s, feature %s" % (i, iris.target[i], iris.data[i])


# training data
test_idx = [0, 50, 100]
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

# testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

# print the test targets, this is also the outcome we expect from clf.predict. If they match the prediction is a 100%
# score and our model is working as it should be.
print test_target

# print the outome of the prediction based upon the test
print clf.predict(test_data)




# the below code is to prepare the graphical representation of the decission tree. Uncomment the last two lines to
# get the actual PDF which contains the execution flow of the tree in a visual manner.
dot_data = StringIO()
tree.export_graphviz(clf,
                     out_file=dot_data,
                     feature_names=iris.feature_names,
                     class_names=iris.target_names,
                     filled=True, rounded=True,
                     impurity=False)

#(graph,) = pydot.graph_from_dot_data(dot_data.getvalue())
#graph.write_pdf("./iris.pdf")



