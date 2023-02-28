class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SlinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def createLL(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        newNode.next = None


singlyLL = SlinkedList()
singlyLL.createLL(5)
print([node.value for node in singlyLL])
