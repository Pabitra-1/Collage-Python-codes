class Stack:
    list = []
    def push(num):
        list.append(num)
    def pop():
        list.pop()
    def peak():
        return list[-1]

Stack stack = Stack()