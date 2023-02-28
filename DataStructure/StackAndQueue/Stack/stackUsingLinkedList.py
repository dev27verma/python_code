class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return ' -> '.join(values)

    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False

    def push(self, value):
        newNode = Node(value)
        newNode.next = self.LinkedList.head
        self.LinkedList.head = newNode

    def pop(self):
        if self.isEmpty():
            print("No element present in Linked List")
        else:
            self.LinkedList.head = self.LinkedList.head.next

    def peek(self):
        if self.isEmpty():
            return "No element present in Linked List"
        else:
            return self.LinkedList.head.value

    def delete(self):
        self.LinkedList.head = None


customStack = Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
customStack.push(5)
print(customStack)
print("POP")
customStack.pop()
print(customStack)
print("POP")
customStack.pop()
print(customStack)
print("Peek")
print(customStack.peek())
print("Deleted Stack")
print(customStack.delete())
print(customStack)