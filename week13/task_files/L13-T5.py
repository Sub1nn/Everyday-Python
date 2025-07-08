# L13-T5: Improved version of Fibonacci
def fibonacci_linear(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Test for L13-T5
n = 12
print(f"Improved Fibonacci({n}):", fibonacci_linear(n))

import time
n = 40
start_time = time.time()
print(f"Fibonacci({n}) using linear approach:", fibonacci_linear(n))
print(f"Time taken (linear): {time.time() - start_time:.4f} seconds")
