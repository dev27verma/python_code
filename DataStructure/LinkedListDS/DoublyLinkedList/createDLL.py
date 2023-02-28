class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class DLinkedList:
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

    # creation of Linked list
    def createDLL(self, value):
        newNode = Node(value)
        newNode.prev = None
        newNode.next = None
        self.head = newNode
        self.tail = newNode


doublyLL = DLinkedList()
doublyLL.createDLL(6)
print([node.value for node in doublyLL])
