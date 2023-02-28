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
            node = node.next

    # insertion of Linked list
    def insertDLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            newNode.prev = None
            newNode.next = None
        else:
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == -1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                newNode.prev = tempNode
                newNode.next = nextNode
                tempNode.next = newNode
                nextNode.prev =  newNode

    # Search Function
    def search(self, value):
        if self.head is None:
            print("Linked List not present")
        else:
            tempNode = self.head
            while tempNode is not None:
                if tempNode.value == value:
                    return "Value found in Linked List"
                tempNode = tempNode.next
            return "Value not found in Linked List"


doublyLL = DLinkedList()
doublyLL.insertDLL(1, 0)
doublyLL.insertDLL(0, 0)
doublyLL.insertDLL(7, 1)
doublyLL.insertDLL(5, 2)
doublyLL.insertDLL(1, 3)
doublyLL.insertDLL(0, 4)
doublyLL.insertDLL(7, 5)
doublyLL.insertDLL(5, 3)
doublyLL.insertDLL(1, 0)
doublyLL.insertDLL(4, 5)
doublyLL.insertDLL(3, -1)

print([node.value for node in doublyLL])
# search
print(doublyLL.search(7))