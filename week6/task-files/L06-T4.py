# L06-T4: Matrix (Matrix is a list of lists [[1,2], [3,4], [5,6]])

def create_matrix(rows, cols):
    # Initialize an empty list to hold the matrix
    matrix = []
    for i in range(1, rows + 1):
        while True: # prompt the user for input until they provide a valid row.
            row_input = input(f"Give row {i}:\n").split() # split input into list
            # validate number of elements in the row
            if len(row_input) == cols:
                # Convert input strings to integers and add to the matrix
                matrix.append([int(element) for element in row_input])
                break # exit the loop if invalid input
            else:
                print("Error: Invalid number of elements in the row. Please try again.")
    return matrix

def print_matrix(matrix):
    for row in matrix:
        # print each row Joining elements with tabs and enclosed with '|'
        print('|' + '\t'.join(map(str, row)) + '|')

def main():
    rows = int(input("Enter the number of rows:\n"))
    cols = int(input("Enter the number of columns:\n"))
    # Create the matrix based on user input
    matrix = create_matrix(rows, cols)
    print_matrix(matrix)
    
# Run the main function to execute the program
main()
