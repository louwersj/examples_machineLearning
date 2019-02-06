import pandas as pd
import matplotlib
matplotlib.use('TkAgg') #quick fix to select the backend and prevent MacOs issues
import matplotlib.pyplot as ppl

# create a dataframe using Pandas, reading the .csv file with a ';' delimiter
df = pd.read_csv('05-gemiddelde-afstand-tussen-woonadres-leerling-en-schoolvestiging-2017-2018.csv', delimiter=";")

# Uncomment if you want to see the head of the dataframe
print(df.head())


# create a scatter chart based upon the LEERLINGEN and AFSTAND datapoints in the dataframe.
ppl.scatter(df.LEERLINGEN, df.AFSTAND)

# Safe the scatter plot to example_1.png and close ppl.
ppl.savefig('xx.png')
ppl.close()

print('done')


