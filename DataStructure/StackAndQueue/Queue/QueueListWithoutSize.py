class Queue:
    def __init__(self):
        self.item = []

    def __str__(self):
        values = [str(x) for x in self.item]
        return ' '.join(values)

    def isEmpty(self):
        if not self.item:
            return True
        else:
            return False

    def enqueue(self, value):
        self.item.append(value)

    def dequeue(self):
        if self.isEmpty():
            print("No element present in dequeue")
        else:
            self.item.pop(0)

    def peek(self):
        if self.isEmpty():
            return "No element present in dequeue"
        else:
            return self.item[0]

    def delete(self):
        self.item = None


customQueue = Queue()
print(customQueue.isEmpty())
print('Enqueue')
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(5)
customQueue.enqueue(5)
print(customQueue)
print(customQueue.isEmpty())
print("Dequeue")
customQueue.dequeue()
print(customQueue)
print("Dequeue")
customQueue.dequeue()
print(customQueue)
print("Peek")
print(customQueue.peek())
print("Deleted Queue")
customQueue.delete()
# print(customQueue)