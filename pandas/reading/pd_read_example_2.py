__author__ = "Johan Louwers"
__copyright__ = "Copyright 2019, Johan Louwers"
__license__ = "MIT"
__email__ = "louwersj@gmail.com"

''' 
    This example code is a private example code and comes as-is without any warranty under the mentioned license.

    This example shows how to load a simple .json file into a DataFrame
'''

import pandas as pd

# Create URL to JSON file (alternatively this can be a filepath)
url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/data.json'
#url = '../../data/dataset_6.json'


# Load the first sheet of the JSON file into a data frame
df0 = pd.read_json('../../data/dataset_6.json', orient='columns')
print ('show the content of the dataframe containing data from the local .json file')
print(df0.head())