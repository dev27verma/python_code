class Node:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None


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
        newNode.next = newNode
        newNode.prev = newNode

    def insertDCLL(self, value, location):
        if self.head is None:
            print("Linked List does not found")
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode

    def deleteDCLL(self, location):
        if self.head is None:
            print("Linked List not found")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head



doublyCircularLinkedList = DCLinkedList()
doublyCircularLinkedList.createDCLL(5)
doublyCircularLinkedList.insertDCLL(1, 0)
doublyCircularLinkedList.insertDCLL(0, 0)
doublyCircularLinkedList.insertDCLL(7, 1)
doublyCircularLinkedList.insertDCLL(5, 2)
doublyCircularLinkedList.insertDCLL(1, 3)
doublyCircularLinkedList.insertDCLL(0, 4)
doublyCircularLinkedList.insertDCLL(7, 5)
doublyCircularLinkedList.insertDCLL(5, 3)
doublyCircularLinkedList.insertDCLL(1, 0)
doublyCircularLinkedList.insertDCLL(4, 5)
doublyCircularLinkedList.insertDCLL(3, -1)
print([node.value for node in doublyCircularLinkedList])
print(doublyCircularLinkedList.searchDCLL(3))