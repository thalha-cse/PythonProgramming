# This project is fizz buzz algorithm, this project is some what like if-else statement
# FizzBuzz Algorithm is refer to any number this is multiple of 3 and 5. 
# if the integer (x) is divisible by 3 the output must be replaced by "Fizz"
# if the integer (x) is divisible by 5 the output must be replaced by "Buzz"
# if the integer (x) is divisible by 3 and 5 the output must be replaced by "FizzBuzz"

n = int(input("Enter a number:- "))
# For loop is used in the below line
for i in range(1, n):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
