import matplotlib
matplotlib.use('agg') #quick workarround for issue with matplotlib unable to find backend on MacOS
import matplotlib.pyplot as plt

plt.plot([1,3,6],[6,4,9])

plt.savefig('plt_simple_example_1.png')