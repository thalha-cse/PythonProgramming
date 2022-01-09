# This project is about by taking multiple inputs using While loop in python
# If user wants to input data/string/any other things multiple times this is for them.....

# while True means infinte loop, it will run until it gets fails
while True:
    reply = input("Enter Text:- ")
    if reply=="stop":
        break
    print(reply)
