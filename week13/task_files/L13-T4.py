# L13-T4: Complexity issues
# Running Fibonacci with higher values of n

def fibonacci(n):
    if n == 0:
        return 0  # Base case
    elif n == 1:
        return 1  # Base case
    return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case

def test_fibonacci_complexity():
    import time
    for n in [30, 35, 40]:
        start_time = time.time()
        print(f"Fibonacci({n}):", fibonacci(n))
        print(f"Time taken for Fibonacci({n}): {time.time() - start_time:.4f} seconds")

test_fibonacci_complexity()


# The recursive approach takes a long time to compute for bigger values of n because of redundancy.
