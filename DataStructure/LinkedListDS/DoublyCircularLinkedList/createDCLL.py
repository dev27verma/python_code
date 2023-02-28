class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class DCLinkedList:
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

    def createDCLL(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode


doublyCircularLL = DCLinkedList()
doublyCircularLL.createDCLL(6)
print([node.value for node in doublyCircularLL])
