from sklearn import tree

__author__ = "Johan Louwers"
__copyright__ = "Copyright 2019, Johan Louwers"
__license__ = "MIT"
__email__ = "louwersj@gmail.com"

''' 
    This example code is based upon an example provided by Google and showcases classifier used in a supervised 
    machine learning example to predict if an object is an apple (0) or an orange (1) based upon the weight and the 
    skin type  bumpy (0) or smooth (1). the weight and skin are used as the features and mapped against the labels. 
    
    When using a clf.predict and provide two new features if model will decide if it is an apple (0) or an orange (1) 
    based upon the learning data it already has in the form a features and label set.  
'''

features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = [0, 0, 1, 1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

print clf.predict([[150, 0]])
