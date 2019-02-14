__author__ = "Johan Louwers"
__copyright__ = "Copyright 2019, Johan Louwers"
__license__ = "MIT"
__email__ = "louwersj@gmail.com"

''' 
    This example code is a private example code and comes as-is without any warranty under the mentioned license.

    This example shows how to load a simple .json file into a DataFrame based upon a local .json file.
'''

import pandas as pd

# load the json structure into a pandas DataFrame based upon a local json file
df0 = pd.read_json('../../data/dataset_6.json', orient='columns')
print ('show the content of the dataframe containing data from the local .json file')
print(df0.head())