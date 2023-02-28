class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class CLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    def createLL(self, value):
        newNode = Node(value)
        newNode.next = newNode
        self.head = newNode
        self.tail = newNode


circularLL = CLinkedList()
circularLL.createLL(5)
print([node.value for node in circularLL])
