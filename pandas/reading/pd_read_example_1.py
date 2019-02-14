__author__ = "Johan Louwers"
__copyright__ = "Copyright 2019, Johan Louwers"
__license__ = "MIT"
__email__ = "louwersj@gmail.com"

''' 
    This example code is a private example code and comes as-is without any warranty under the mentioned license.

    This example shows how to load a .csv file into a pandas DataFrame
'''

import pandas as pd

# use pandas to read the data from a file into a pandas DataFrame.
df0 = pd.read_csv('../../data/dataset_4.csv', delimiter=";",)
print ('show the content of the first file via dataframe df0')
print (df0.head())