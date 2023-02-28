class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = [str(x) for x in self.list]
        return ' '.join(values)

    # isEmpty()
    def isEmpty(self):
        if not self.list:
            return True
        else:
            return False

    # push
    def push(self, value):
        self.list.append(value)

    # pop
    def pop(self):
        if self.isEmpty():
            return "There is no element on stack"
        else:
            return self.list.pop()

    # peek
    def peek(self):
        if self.isEmpty():
            return "There is no element on stack"
        else:
            return self.list[len(self.list) - 1]

    # delete
    def delete(self):
        self.list = None


customStack = Stack()
print(customStack.isEmpty())
print("After Push")
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
customStack.push(5)
print(customStack)
print("After Pop")
customStack.pop()
customStack.pop()
print(customStack)
print("Peek")
print(customStack.peek())
customStack.delete()
# after delete stack will not found so it will return error
# print(customStack)
