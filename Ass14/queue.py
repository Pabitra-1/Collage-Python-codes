class Queue:
<<<<<<< HEAD

    def __init__(self) :
        self.list = []
    def enqueue(self,num) :
        self.list.append(num)
    def dequeue(self) :
        return self.list.pop(0)
    def peak(self) :
        return print(self.list[0])
    def display(self) :
        return print(self.list)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.display()
queue.dequeue()
queue.display()
queue.peak()
=======
    def __init__(self):
        self.list = []

    def enqueue(self, num):
        self.list.append(num)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.list.pop(0)

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.list[0]

    def is_empty(self):
        return len(self.list) == 0

    def display(self):
        print(self.list)


queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.peek())       # 1
print(queue.dequeue())    # 1
print(queue.dequeue())    # 2

queue.display()           # [3]
>>>>>>> 09ee3d56bc0b5b257b522171c461b85f3e7e2310
