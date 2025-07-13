def shortest_diagonal_path_sum(grid):
    rows = len(grid)
    cols = len(grid[0])

    # DP table to hold min path sums
    dp = [[float('inf')] * cols for _ in range(rows)]
    parent = [[None] * cols for _ in range(rows)]  # To reconstruct path
    dp[0][0] = grid[0][0]

    for i in range(rows):
        for j in range(cols):
            for dx, dy in [(1, 0), (0, 1), (1, 1)]:  # Down, Right, Diagonal
                ni, nj = i + dx, j + dy
                if ni < rows and nj < cols:
                    new_cost = dp[i][j] + grid[ni][nj]
                    if new_cost < dp[ni][nj]:
                        dp[ni][nj] = new_cost
                        parent[ni][nj] = (i, j)

    # Backtrack to find the path
    path = []
    i, j = rows - 1, cols - 1
    while True:
        path.append((i, j))
        if parent[i][j] is None:
            break
        i, j = parent[i][j]
    path.reverse()

    # Extract values along the path
    path_values = [grid[i][j] for i, j in path]
    total = dp[rows - 1][cols - 1]

    return total, path_values


def get_input_grid():
    print("Enter the grid row by row (space-separated integers). Type 'done' to finish:")
    grid = []
    expected_length = None

    while True:
        row = input("> ")
        if row.strip().lower() == 'done':
            break
        try:
            numbers = list(map(int, row.strip().split()))
            if expected_length is None:
                expected_length = len(numbers)
            elif len(numbers) != expected_length:
                print(f"⚠️ Row must have {expected_length} numbers. Try again.")
                continue
            grid.append(numbers)
        except ValueError:
            print("⚠️ Invalid input. Please enter integers only.")
    return grid


# Main Program
grid = get_input_grid()

if grid:
    print("\nGrid entered:")
    for row in grid:
        print(row)

    total, path_values = shortest_diagonal_path_sum(grid)
    expression = " + ".join(map(str, path_values))
    print(f"\nShortest diagonal path: {expression} = {total}")
else:
    print("No grid was entered.")