import pandas as pd
import matplotlib
matplotlib.use('Agg') #quick fix to select the backend and prevent MacOs issues
import matplotlib.pyplot as ppl

# create a dataframe using Pandas, reading the .csv file with a ';' delimiter.
df = pd.read_csv('../../data/dataset_2.csv', delimiter=";", thousands=',')

# Uncomment if you want to see the head of the dataframe
print(df.head())


# create a scatter chart based upon the LEERLINGEN and AFSTAND datapoints in the dataframe.
#ppl.scatter(df.LEERLINGEN, df.AFSTAND)

ppl.scatter(df.AFSTAND, df.LEERLINGEN)
# Safe the scatter plot to example_1.png and close ppl.
ppl.savefig('xx.png')


print('done')


