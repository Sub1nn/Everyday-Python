# L13-T2: Sum of numbers #2
def sum_of_digits_recursive(n):
    if n < 10:
        return n  # Base case: single digit
    return n % 10 + sum_of_digits_recursive(n // 10)  # Recursive case

# Test for L13-T2
n = 123
print("Sum of digits:", sum_of_digits_recursive(n))
