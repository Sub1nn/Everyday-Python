def main():
    # Define the matrix
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    while True:
        try:
            # Prompt for the row index
            row_index = int(input("Enter the row index:\n"))
            
            # Prompt for the column index
            col_index = int(input("Enter the column index:\n"))
            
            # Access the value in the matrix
            value = matrix[row_index][col_index]
            print(f"Value at position ({row_index}, {col_index}): {value}")
            break  # Exit the loop after successful access

        except IndexError:
            print("Error: Index out of bounds. Please enter valid row and column indices.")
            return None
        except ValueError:
            print("Error: Please enter valid integers for row and column indices.")
            return None

# Call the main function
if __name__ == "__main__":
    main()
