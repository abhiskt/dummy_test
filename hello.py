def fibonacci(n):
    """
    Calculates the nth Fibonacci number using recursion.
    The sequence starts: 0, 1, 1, 2, 3, 5, 8... (0-based index)
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage:
num_terms = 7
print(f"Fibonacci sequence up to {num_terms} terms:")
for i in range(num_terms):
    print(fibonacci(i), end=" ")
