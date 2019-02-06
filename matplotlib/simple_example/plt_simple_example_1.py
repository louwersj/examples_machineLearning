import matplotlib
matplotlib.use('agg') #quick workarround for issue with matplotlib unable to find backend on MacOS
import matplotlib.pyplot as plt

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

plt.plot([1,3,6],[6,4,9])

plt.savefig('plt_simple_example_1.png')