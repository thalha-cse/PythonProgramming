# This project is used object oriented programming.
# User if you know about oops it will help you to understand otherwise it won't

class stack:
    def __init__(self):
        self.item = []
    def is_empty(self):
        return self.item == []
    def push(self, item):
        self.item.append(item)
    def pop(self):
        return self.item.pop()
    def peek(self):
        l = len(self.item)-1
        return self.item[l]
    def size(self):
        return len(self.item)

stack = stack()
print(stack.is_empty())
for i in range(0, 10):
    stack.push(i)
print(stack.size())
print(stack.item)
name = (input("Enter your name:- "))
stack.push(name)
print(stack.item)
