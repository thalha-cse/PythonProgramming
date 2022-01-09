# This project count the character occurrences in the string which user gives
# This project contains 
# 1. User defines function 2. for loop 3. if else statement and some more variables.....

# a is the formal parameters in the below line
def count_occurrences(a):
    count = {}
    for i in a:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print(count)
    
sentence = input("Enter the string:- ")
# sentence is the actual parameter in the below line
count_occurrences(sentence)
