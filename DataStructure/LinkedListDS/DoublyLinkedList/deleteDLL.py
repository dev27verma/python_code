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
                nextNode.prev = newNode

    # delete element from LL
    def deleteDLL(self, location):
        if self.head is None:
            print("Linked List does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                curNode = self.head
                index = 0
                while index < location - 1:
                    curNode = curNode.next
                    index += 1
                curNode.next = curNode.next.next
                curNode.next.prev = curNode

    # delete entire Linked List
    def deleteEntireDLL(self):
        if self.head is None:
            print("Linked List does not exist")
        else:
            currNode = self.head
            index = 0
            while currNode is not None:
                currNode.prev = None
                currNode = currNode.next
            self.head = None
            self.tail = None


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
# deletion function
doublyLL.deleteDLL(0)
print([node.value for node in doublyLL])
doublyLL.deleteDLL(-1)
print([node.value for node in doublyLL])
doublyLL.deleteDLL(4)
print([node.value for node in doublyLL])
doublyLL.deleteEntireDLL()
print([node.value for node in doublyLL])
