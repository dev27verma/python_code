def maxProductPathOptimized(grid):
    m, n = len(grid), len(grid[0])

    max_dp = [0] * n
    min_dp = [0] * n

    parent = [[None] * n for _ in range(m)]

    max_dp[0] = min_dp[0] = grid[0][0]

    # First row
    for j in range(1, n):
        max_dp[j] = min_dp[j] = max_dp[j - 1] * grid[0][j]
        parent[0][j] = (0, j - 1)

    # Remaining rows
    for i in range(1, m):
        new_max = [0] * n
        new_min = [0] * n

        # First column
        new_max[0] = new_min[0] = max_dp[0] * grid[i][0]
        parent[i][0] = (i - 1, 0)

        for j in range(1, n):
            val = grid[i][j]

            candidates = [
                (max_dp[j] * val, (i - 1, j)),
                (min_dp[j] * val, (i - 1, j)),
                (new_max[j - 1] * val, (i, j - 1)),
                (new_min[j - 1] * val, (i, j - 1))
            ]

            max_val, max_parent = max(candidates, key=lambda x: x[0])
            min_val, _ = min(candidates, key=lambda x: x[0])

            new_max[j] = max_val
            new_min[j] = min_val
            parent[i][j] = max_parent

        max_dp = new_max
        min_dp = new_min

    # Path reconstruction
    path = []
    i, j = m - 1, n - 1
    while True:
        path.append(grid[i][j])
        if parent[i][j] is None:
            break
        i, j = parent[i][j]

    path.reverse()
    return max_dp[n - 1], path


# 🔹 Dynamic Input
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

grid = []
print("Enter matrix row by row (space-separated):")

for i in range(m):
    while True:
        row = list(map(int, input().split()))
        if len(row) == n:
            grid.append(row)
            break
        else:
            print(f"Please enter exactly {n} values.")

# 🔹 Run
result, path = maxProductPathOptimized(grid)

# 🔹 Output
print("\nMaximum Non-Negative Product:", result)
print("Path:", " → ".join(map(str, path)))