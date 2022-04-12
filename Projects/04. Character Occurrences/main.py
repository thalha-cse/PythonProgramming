# This project is about Character occurrences in a string or in any other paragraphs etc...
# This project contains user defined function named as count_occurrences, for loop, if else statement and some variables

# "a" is formal parameter in below line
def count_occurrences(a):
    count = {}
    for i in a:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print(count)

sentence = input("Enter the string:- ")
# 'sentence' is used as actual parameter in below line
count_occurrences(sentence)
