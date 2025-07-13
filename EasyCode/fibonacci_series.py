def fibonacci_series(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib


# Main program
try:
    n = int(input("Enter the number of terms for the Fibonacci series: "))
    result = fibonacci_series(n)

    print("\nFibonacci series:")
    print(", ".join(map(str, result)))

    total = sum(result)
    print(f"\nSum of the series: {total}")

except ValueError:
    print("⚠️ Please enter a valid integer.")
