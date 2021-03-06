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

    This example builds upon the code provided in plt_simple_example_1.py, the main difference is that we do not use
    a list to provide the values, we use pandas to read the data from the file and provide it to pyplot. This makes the
    code much more usable, as a side-effect we will now see all the data available the original dataset (dataset-1.csv)
'''

import pandas as pd
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

# Create a dataframe (df) by instructing pandas to read the dataset. This replaces the need to have two lists and makes
# the code more usable in real-life.
df = pd.read_csv('../../data/dataset_1.csv')

# Populate ax wih plt.gca (gca stands for 'get current axis')
ax = plt.gca()

# use the dataframe to do the plot, in the backend it will use matplotlib however it is initiated by the dataframe in
# this case.
df.plot(kind='line',x='ds',y='y',ax=ax)


# save the plot as a figure using savefig, we use plt instead of df (dataframe) as we now pull it to the frontend and we
# are not using the backend part of matplotlib. This should provide you with an 'ugly' graph.
plt.savefig('plt_simple_example_2.png')




