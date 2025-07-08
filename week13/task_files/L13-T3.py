# L13-T3: Fibonacci numbers
def fibonacci(n):
    if n == 0:
        return 0  # Base case
    elif n == 1:
        return 1  # Base case
    return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case

# Test
n = 12  # Calculate Fibonacci(12)
print(f"Fibonacci({n}):", fibonacci(n))


import time
n = 12
start_time = time.time()
print(f"Fibonacci({n}) using recursion:", fibonacci(n))
print(f"Time taken (recursion): {time.time() - start_time:.4f} seconds")
