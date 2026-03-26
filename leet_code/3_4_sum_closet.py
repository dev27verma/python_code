def threeSum(nums):
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

    return result


def fourSum(nums, target):
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left, right = j + 1, n - 1

            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]

                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < target:
                    left += 1
                else:
                    right -= 1

    return result


def threeSumClosest(nums, target):
    nums.sort()
    closest = float('inf')

    for i in range(len(nums)):
        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if abs(target - total) < abs(target - closest):
                closest = total

            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return total

    return closest


# 🔁 Continuous Menu
while True:
    print("\n--- Sum Problems Menu ---")
    print("1. 3Sum")
    print("2. 4Sum")
    print("3. 3Sum Closest")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        n = int(input("Enter number of elements: "))
        nums = list(map(int, input("Enter numbers: ").split()))

        if len(nums) != n:
            print("Invalid input!")
        else:
            print("Triplets:", threeSum(nums))

    elif choice == '2':
        n = int(input("Enter number of elements: "))
        nums = list(map(int, input("Enter numbers: ").split()))
        target = int(input("Enter target: "))

        if len(nums) != n:
            print("Invalid input!")
        else:
            print("Quadruplets:", fourSum(nums, target))

    elif choice == '3':
        n = int(input("Enter number of elements: "))
        nums = list(map(int, input("Enter numbers: ").split()))
        target = int(input("Enter target: "))

        if len(nums) != n:
            print("Invalid input!")
        else:
            print("Closest Sum:", threeSumClosest(nums, target))

    elif choice == '4':
        print("Exiting...")
        break

    else:
        print("Invalid choice! Try again.")