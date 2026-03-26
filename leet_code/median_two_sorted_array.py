def findMedian(arr1, arr2):
    merged = arr1 + arr2
    merged.sort()

    n = len(merged)

    # If odd
    if n % 2 == 1:
        return merged[n // 2]

    # If even
    else:
        return (merged[n // 2 - 1] + merged[n // 2]) / 2


# 🔹 Dynamic Input
n1 = int(input("Enter size of first array: "))
print("Enter elements of first sorted array:")
arr1 = list(map(int, input().split()))

n2 = int(input("Enter size of second array: "))
print("Enter elements of second sorted array:")
arr2 = list(map(int, input().split()))

# 🔹 Validate input size
if len(arr1) != n1 or len(arr2) != n2:
    print("Invalid input size!")
else:
    median = findMedian(arr1, arr2)
    print("\nMedian of two sorted arrays:", median)