# L04-T4: Extensions of repeat structures

lower = int(input("Enter the lower limit of the range:\n"))
upper = int(input("Enter the upper limit of the range:\n"))
found = False  # set initial value to False for found

# range() function does not include the upper bound, so have to do (upper+1)
for num in range(lower, upper + 1):
    if num % 5 != 0:
        print(f"{num} is NOT divisible by 5, rejecting.")
        continue  # Move to the next number if NOT divisible by 5

    if num % 7 != 0:
        print(f"{num} is NOT divisible by 7, rejecting.")
    else:
        print(f"The number {num} is divisible by 5 and 7.")
        found = True
        print("Stopping the search.")
        break  # Stop the search when found

# After the loop, check if no suitable number was found
if not found:
    print("No suitable value was found in the range.")
