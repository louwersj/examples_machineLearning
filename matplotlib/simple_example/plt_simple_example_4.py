__author__ = "Johan Louwers"
__copyright__ = "Copyright 2019, Johan Louwers"
__license__ = "MIT"
__email__ = "louwersj@gmail.com"

''' 
    This example code is a private example code and comes as-is without any warranty under the mentioned license.

    DO NOTE : due to a 'bug' when using a virtualenv in combination with matplotlib on MacOS we have stated the used
    backend explicitly using matplotlib.use('agg') which might not be required in every situation and might not work
    in your specific situation. In case the code gives errors please check the backend setting required for your specific
    situation and operating system. 

    This example shows how to change the colors of the plot and change some other behaviour of the plot
'''

import pandas as pd
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

# use pandas to read the data into a dataframe
df = pd.read_csv('../../data/dataset_3.csv')

# initiate plot1 as a dataframe plot via pandas.
plot1 = df.plot(kind='scatter', x='GDP_per_capita', y='life_expectancy', color='white', alpha=0.5, linewidth=0)

# set details on Y
plot1.set_ylim((0, 85))
plot1.set_ylabel('Life expectancy')

# set details on X
plot1.set_xlim((0, 60000))
plot1.set_xlabel('GDP per capita')

# Specify background color for the axis/plot
plot1.set_axis_bgcolor("lightslategray")

# save the plotted figure to the local disk
plt.savefig('plt_simple_example_4.png')