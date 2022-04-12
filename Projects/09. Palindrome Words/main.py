# This project is extracting palindrome words from the sentences/paragraphs or any article
# First of all removing punctuation from the sentence/paragraph/articles after that checking whether words or palindrome or not
# If the words are palindrome print it...

def palindrome(sentence):
    # Below line contains punctuation
    for i in (".,<>[]{}'():;/*-+_*!@#$%^"):
        sentence = sentence.replace(i, "")
    palindrome = []
    # Splitting the words from the sentence
    words = sentence.split(" ")
    for word in words:
        word = word.lower()
        # Checking the words are palindrome or not
        if word == word[::-1]:
            palindrome.append(word)
    return palindrome
sentence = input("Enter the sentence:- ")
print(palindrome(sentence))
