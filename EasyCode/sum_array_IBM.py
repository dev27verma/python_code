def getMaxSum(arr):
    n = len(arr)
    if n <= 2:
        return sum(arr)

    prefix_max = [0] * n
    suffix_max = [0] * n

    prefix_max[0] = arr[0]
    for i in range(1, n):
        prefix_max[i] = max(prefix_max[i - 1], arr[i])

    suffix_max[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        suffix_max[i] = max(suffix_max[i + 1], arr[i])

    total_sum = arr[0] + arr[n - 1]

    for i in range(1, n - 1):
        fill = min(prefix_max[i - 1], suffix_max[i + 1])
        total_sum += max(arr[i], fill)

    return total_sum


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    print(getMaxSum(arr))
