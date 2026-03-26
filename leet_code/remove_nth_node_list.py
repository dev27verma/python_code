class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head

    fast = slow = dummy

    # Move fast n+1 steps
    for _ in range(n + 1):
        fast = fast.next

    # Move both
    while fast:
        fast = fast.next
        slow = slow.next

    # Delete node
    slow.next = slow.next.next

    return dummy.next


# 🔹 Create Linked List from input
def createList(arr):
    head = ListNode(arr[0])
    curr = head
    for num in arr[1:]:
        curr.next = ListNode(num)
        curr = curr.next
    return head


# 🔹 Print Linked List
def printList(head):
    while head:
        print(head.val, end=" → ")
        head = head.next
    print("None")


# 🔹 Dynamic Input
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

remove_n = int(input("Enter n (node to remove from end): "))

if len(arr) != n:
    print("Invalid input!")
else:
    head = createList(arr)

    print("\nOriginal List:")
    printList(head)

    head = removeNthFromEnd(head, remove_n)

    print("Updated List:")
    printList(head)