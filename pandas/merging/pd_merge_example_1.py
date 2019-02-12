__author__ = "Johan Louwers"
__copyright__ = "Copyright 2019, Johan Louwers"
__license__ = "MIT"
__email__ = "louwersj@gmail.com"

''' 
    This example code is a private example code and comes as-is without any warranty under the mentioned license.

    This example shows how to load two datasets each into their own individual dataframe and merge them into a new 
    dataframe based upon two columns that both datasets have in common. 
'''

import pandas as pd

# use pandas to read the data from the first file into a dataframe (df0)
df0 = pd.read_csv('../../data/dataset_4.csv', delimiter=";",)
print ('show the content of the first file via dataframe df0')
print (df0.head())


# use pandas to read the data from the second file into a dataframe (df1)
df1 = pd.read_csv('../../data/dataset_5.csv', delimiter=";",)
print ('show the content of the second file via dataframe df1')
print (df1.head())

# use pandas to merge the two dataframes (df0 & df1) into a new dataframe (df2). Merge is done based upon two columns
# that both dataframes have in common, namely; 'Country Code' and 'Country Name'
df2 = pd.merge(df0, df1, on=['Country Code','Country Name'])
print ('show the content of merged dataframes as a single dataframe')
print (df2.head())

# Additionally showing how this could be done in a single line of code
singleLineExampleDf = pd.merge((pd.read_csv('../../data/dataset_4.csv', delimiter=";",)),(pd.read_csv('../../data/dataset_5.csv', delimiter=";",)), on=['Country Code','Country Name'])
print ('show the content of merged (single line of code) dataframes as a single dataframe')
print (singleLineExampleDf.head())