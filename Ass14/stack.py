class Stack:
    def __init__(self):
        self.list = []

    def push(self, num):
        self.list.append(num)

    def pop(self):
        return self.list.pop()

    def peek(self):
        return self.list[-1]


stack = Stack()

stack.push(1)
stack.push(2)

print(stack.peek())