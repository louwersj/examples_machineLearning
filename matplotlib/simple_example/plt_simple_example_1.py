__author__ = "Johan Louwers"
__copyright__ = "Copyright 2019, Johan Louwers"
__license__ = "MIT"
__email__ = "louwersj@gmail.com"

''' 
    This example code is based a private example code and comes as-is without any warranty under the mentioned license.

    DO NOTE : due to a 'bug' when using a virtualenv in combination with matplotlib on MacOS we have stated the used
    backend explicitly using matplotlib.use('agg') which might not be required in every situation and might not work
    in your specific situation. In case the code gives errors please check the backend setting required for your specific
    situation and operating system. 

    This example shows the most simple implementation of matplotlib and pyplot to plot a line graph and save it to a 
    local file. The data used is hardcoded. 
'''

import matplotlib
matplotlib.use('agg') #quick workarround for issue with matplotlib unable to find backend on MacOS
import matplotlib.pyplot as plt

plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], [1,2,4,7,8,9,8,6,5,3,1,0,2,4,6,8,9,3,2,1])

plt.savefig('plt_simple_example_1.png')