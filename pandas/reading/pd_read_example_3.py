__author__ = "Johan Louwers"
__copyright__ = "Copyright 2019, Johan Louwers"
__license__ = "MIT"
__email__ = "louwersj@gmail.com"

''' 
    This example code is a private example code and comes as-is without any warranty under the mentioned license.

    This example shows how to load a simple .json file into a DataFrame based upon a remote .json file. The content of 
    the JSON structure is simple and is not in need of "complex" parsing. 
'''

import pandas as pd

# Load the first sheet of the JSON file into a data frame
#df0 = pd.read_json('https://raw.githubusercontent.com/louwersj/examples_machineLearning/master/data/dataset_6.json', orient='columns')
df0 = pd.read_json('https://raw.githubusercontent.com/louwersj/examples_machineLearning/master/data/dataset_6.json', orient='columns')

print ('show the content of the dataframe containing data from the remote .json file')
print(df0.head())



