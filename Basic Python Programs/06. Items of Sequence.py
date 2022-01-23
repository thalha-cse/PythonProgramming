txt = input("Enter the sentence:- ")
words = [word.upper() for word in txt.split()]
words.sort()
print(words)
for word in words:
    print(word)
