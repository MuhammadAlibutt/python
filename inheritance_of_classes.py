# Python code​​​​​​‌‌​​‌‌​‌​​​​​​‌​‌​​‌‌‌‌​‌ below
# You will need this class for your solution. Do not edit it.
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


def reverse_string(my_string):

    s = Stack()
    for i in my_string:
        s.push(i)



    reversed_string = ""

    while s.size():
        reversed_string += s.pop()

    # Create a new stack

    # Iterate through my_string and push the characters onto the stack

    # Use a while loop with the exit condition that the stack is empty.
    # Within this loop, update reversed_string with characters popped off the stack.

    # Return the result
    return reversed_string





print(reverse_string('gninraeL nIdekniL htiw tol a nraeL'))
