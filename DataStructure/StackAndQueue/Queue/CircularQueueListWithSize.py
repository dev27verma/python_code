class Queue:
    def __init__(self, maxsize):
        self.list = maxsize * [None]
        self.maxsize = maxsize
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.list]
        return ' '.join(values)

    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxsize:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def enqueue(self, value):
        if self.isFull():
            print("No space Left")
        else:
            if self.top + 1 == self.maxsize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.list[self.top] = value

    def dequeue(self):
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            firstElement = self.list[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxsize:
                self.start = 0
            else:
                self.start += 1
            self.list[start] = None
            return firstElement

    def peek(self):
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            return self.list[self.top]

    def delete(self):
        self.list = self.maxsize * [None]
        self.start = -1
        self.top = -1


circular_queue = Queue(5)
print(circular_queue)
print(f"Is queue Full: {circular_queue.isFull()}")
print(f"Is queue Empty: {circular_queue.isEmpty()}")
print("Enqueue")
circular_queue.enqueue(1)
circular_queue.enqueue(2)
circular_queue.enqueue(3)
circular_queue.enqueue(4)
circular_queue.enqueue(5)
print(circular_queue)
print("Dequeue")
circular_queue.dequeue()
circular_queue.dequeue()
print(circular_queue)
print(f"Is queue Full: {circular_queue.isFull()}")
print(f"Is queue Empty: {circular_queue.isEmpty()}")
print("Enqueue")
circular_queue.enqueue(7)
print(circular_queue)
print(f"Peek value: {circular_queue.peek()}")
print("Deleted")
circular_queue.delete()
print(circular_queue)