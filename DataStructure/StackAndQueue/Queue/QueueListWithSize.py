class Queue:
    def __init__(self, maxsize):
        self.item = []
        self.maxsize = maxsize

    def __str__(self):
        values = [str(x) for x in self.item]
        return ' '.join(values)

    def isEmpty(self):
        if not self.item:
            return True
        else:
            return False

    def isFull(self):
        if len(self.item) > self.maxsize:
            return True
        else:
            return False

    def enqueue(self, values):
        if self.isFull():
            print("Space not left")
        else:
            self.item.append(values)

    def dequeue(self):
        if self.isEmpty():
            print("No element present")
        else:
            self.item.pop(0)

    def peek(self):
        if self.isEmpty():
            return "No element present"
        else:
            return self.item[0]

    def delete(self):
        self.item = None


customQueue = Queue(5)
print(customQueue.isEmpty())
print(customQueue.isFull())
customQueue.enqueue(5)
customQueue.enqueue(6)
customQueue.enqueue(8)
customQueue.enqueue(5)
customQueue.enqueue(3)
customQueue.enqueue(3)
print(customQueue)
print("Dequeue")
customQueue.dequeue()
customQueue.dequeue()
print(customQueue)
print("Peek")
print(customQueue.peek())
print("Deleted Queue")
customQueue.delete()
# print(customQueue)
