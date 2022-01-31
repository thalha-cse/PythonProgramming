# An acronym is a short form of a word created by long words or phrases such as NLP for natural language processing
# To write this project we need splitting method and indexing method.....


user_input = str(input("Enter a phrase:- "))
text = user_input.split()
a = ""
for i in text:
    a = a + str(i[0]).upper()
print(a)
