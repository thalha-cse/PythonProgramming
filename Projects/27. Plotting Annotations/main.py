'''Plotting annotations while visualizing your data is considered good practice to make the graphs self-explanatory. 
Sometimes it gets very hard for us to understand what curves and dots represents which data points. In such situations using annotations is very helpful. 
In the Python programming language, the matplotlib library provides matplotlib.pyplot.annotate which makes it easy to annotate any type of graph.'''

import matplotlib.pyplot as plt
x = [3, 5, 7, 8, 4]
y = [5, 3, 7, 8, 2]
plt.scatter(x, y)
plt.show()
