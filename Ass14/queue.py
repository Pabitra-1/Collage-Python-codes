class Queue:

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
