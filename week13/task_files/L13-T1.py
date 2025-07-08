# L13-T1: Sum of numbers #1
def sum_of_list_recursive(numbers):
    if len(numbers) == 0:
        return 0  # Base case: empty list
    return numbers[0] + sum_of_list_recursive(numbers[1:])  # Recursive case

# Test for L13-T1
numbers = [1, 2, 3, 4, 5]
print("Sum of list:", sum_of_list_recursive(numbers))
