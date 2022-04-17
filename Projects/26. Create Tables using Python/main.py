"""Tabulate Module in Python
The tabulate module in Python allows us to create and display data in a tabular format which makes the data look more readable.
It can be used to organize your data to make it more understandable.
Below are some of the data structures in Python which are supported by the tabulate module:

Lists
Dictionary
NumPy Array
Pandas DataFrame"""

from tabulate import tabulate
data = [["Name", "Place", "Gender"], ["Rohan", "Mumbai", "Male"], ["Alisha", "Delhi", "Female"], ["Talha", "Dubai", "Male"]]
print(tabulate(data))

# now let’s have a look at how we can separate the headers from the values:
print(tabulate(data, headers="firstrow"))

#We can also design this table by adding a grid, here is how you can do it:
print(tabulate(data, headers="firstrow", tablefmt="grid"))

#We can also make the grid look better:
print(tabulate(data, headers="firstrow", tablefmt="fancy_grid"))
