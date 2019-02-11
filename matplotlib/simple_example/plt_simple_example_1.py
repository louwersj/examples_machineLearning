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

    This example shows the most simple implementation of matplotlib and pyplot to plot a line graph and save it to a 
    local file. The data used is hardcoded. For this we use the average daily temp of a river during a one month periode
    by providing pyplot with two lists. The raw data can be located in dataset_1.csv
'''

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

# provide two lists, one for the values containing the average temperature of the water during a 24 hour period and one
# for the day of the month.
averageTemp = [23, 20.5, 22, 30.5, 31, 27.5, 26.25, 26.5, 23, 23.5, 27, 26.5, 28.5, 24.25, 12.25, 11.25, 17.5, 18, 15.5, 19.5, 15, 21, 21, 20, 28, 26.5, 23.5, 19.25, 13.5, 19]
dayOfMonth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

# use pyplot to plot both the lists on the graph.
plt.plot(dayOfMonth, averageTemp)

# save the plot as a figure using savefig.
plt.savefig('plt_simple_example_1.png')




