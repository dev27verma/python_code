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

    def createCLL(self, value):
        newNode = Node(value)
        newNode.next = newNode
        self.head = newNode
        self.tail = newNode

    def insertCLL(self, value, location):
        if self.head is None:
            return "head reference is None"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    def traversalLL(self):
        if self.head is None:
            print("Linked List does not exist")
        else:
            curNode = self.head
            while curNode:
                print(curNode.value, end=' ')
                curNode = curNode.next
                if curNode == self.tail.next:
                    break


circularLL = CLinkedList()
circularLL.createCLL(5)
circularLL.insertCLL(1, 0)
circularLL.insertCLL(0, 0)
circularLL.insertCLL(7, 1)
circularLL.insertCLL(5, 2)
circularLL.insertCLL(1, 3)
circularLL.insertCLL(0, 4)
circularLL.insertCLL(7, 5)
circularLL.insertCLL(5, 3)
circularLL.insertCLL(1, 0)
circularLL.insertCLL(4, 5)
circularLL.insertCLL(3, -1)

print([node.value for node in circularLL])
circularLL.traversalLL()