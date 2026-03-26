def maxArea(height):
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        h = min(height[left], height[right])
        width = right - left
        area = h * width

        max_water = max(max_water, area)

        # Move smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


# 🔹 Dynamic Input
n = int(input("Enter number of elements: "))
print("Enter heights:")
height = list(map(int, input().split()))

if len(height) != n:
    print("Invalid input!")
else:
    result = maxArea(height)
    print("\nMaximum Water:", result)