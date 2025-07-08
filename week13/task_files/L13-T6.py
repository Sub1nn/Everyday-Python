import time
import copy
import os

# Function to read words from the file and return them as a list
def read_words(file_name):
    try:
        with open(file_name, 'r') as file:
            words = file.readlines()  # Read all lines from the file
        print(f"Successfully read {len(words)} words from the file.")  
        return [word.strip() for word in words]  # Remove any trailing newlines
    except FileNotFoundError:
        print(f"Error: The file {file_name} was not found.")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []

# Quicksort implementation
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Insertion Sort implementation
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Measure time for sorting methods
def measure_times(file_name):
    words = read_words(file_name)  # Read words from the file
    
    # Check if the list is empty (file reading failed)
    if not words:
        print("No words read from the file. Exiting program.")
        return

    # Create three deep copies of the list
    list1 = copy.deepcopy(words)
    list2 = copy.deepcopy(words)
    list3 = copy.deepcopy(words)

    # Measure time taken by sorted()
    start_time = time.time()
    sorted(list1)  # Sorting using the built-in sorted() function
    time_sorted = time.time() - start_time
    print(f"Sorted() completed in {time_sorted:.6f} seconds.")  

    # Measure time taken by quicksort()
    start_time = time.time()
    quicksort(list2)  # Sorting using quicksort()
    time_quicksort = time.time() - start_time
    print(f"Quicksort() completed in {time_quicksort:.6f} seconds.")  

    # Measure time taken by insertionSort()
    start_time = time.time()
    insertionSort(list3)  # Sorting using insertionSort()
    time_insertion_sort = time.time() - start_time
    print(f"InsertionSort() completed in {time_insertion_sort:.6f} seconds.")  

    # Output the results
    print(f"Time taken by sorted(): {time_sorted:.6f} seconds")
    print(f"Time taken by quicksort(): {time_quicksort:.6f} seconds")
    print(f"Time taken by insertionSort(): {time_insertion_sort:.6f} seconds")


file_name = 'pseudo_words.txt'  
print("Current working directory:", os.getcwd())  # Print current directory to verify location
measure_times(file_name)
