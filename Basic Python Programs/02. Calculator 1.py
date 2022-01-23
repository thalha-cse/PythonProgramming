def add_num(x, y):
    add = x + y
    return add

def sub_num(x, y):
    sub = x - y
    return sub

def mul_num(x, y):
    multi = x * y
    return multi

def div_num(x, y):
    div = x / y
    return div

x = int(input("Enter a number:- "))
y = int(input("Enter a number:- "))

print("Addition: ", add_num(x, y))
print("Subtraction: ", sub_num(x, y))
print("Multiplication: ", mul_num(x, y))
print("Divison: ", div_num(x, y))
