# Swapping with temporary variable
a = int(input("Enter the number:- "))
b = int(input("Enter the number:- "))

temp = a
a = b
b = temp

print("The value of a is {0}".format(a))
print("The value of b is {0}".format(b))

# Swapping without temporary variable
a = int(input("Enter the number:- "))
b = int(input("Enter the number:- "))
a, b = b, a
print("The value of a is {0}".format(a))
print("The value of b is {0}".format(b))
