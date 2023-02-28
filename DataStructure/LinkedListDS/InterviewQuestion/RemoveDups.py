# Question 1 - Remove Dups : Write a code to remove duplicates from an unsorted linked list.


from generateRandomLinkedList import LinkedList


def remove_duplicate(ll):
    if ll.head is None:
        return
    else:
        currentNode = ll.head
        visited = set([currentNode.value])
        while currentNode.next:
            if currentNode.next.value in visited:
                currentNode.next = currentNode.next.next
            else:
                visited.add(currentNode.next.value)
                currentNode = currentNode.next
        return ll


# remove duplicate without temporary variable (visited = set([currentNode.value]))
def remove_duplicate1(ll):
    if ll.head is None:
        return
    currentNode = ll.head
    while currentNode:
        runner = currentNode
        while runner.next:
            if runner.next.value == currentNode.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        currentNode = currentNode.next
    return ll.head


print("Before")
customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
print("After")
# with temp buffer visited = set([currentNode.value])
remove_duplicate(customLL)
# without temp buffer visited = set([currentNode.value])
print(customLL)
remove_duplicate1(customLL)
print(customLL)
