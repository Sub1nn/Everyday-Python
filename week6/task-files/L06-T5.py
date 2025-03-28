# L06-T5: Matrix 2

def create_matrix(rows, cols):
    # Initialize an empty list to hold the matrix
    matrix = []
    for i in range(1, rows + 1):
        while True: # prompt the user for input until they provide a valid row.
            row_input = input(f"Give row {i}:\n").split()
            # validate number of elements in the row
            if len(row_input) == cols:
                # Convert input strings to integers and add to the matrix
                matrix.append([int(element) for element in row_input])
                break
            else:
                print("Error: Invalid number of elements in the row. Please try again.")
    return matrix

def print_matrix(matrix):
    for row in matrix:
        # print each row Joining elements with tabs and enclosed with '|'
        print('|' + '\t'.join(map(str, row)) + '|')
        
# Get the number of rows and columns from the original matrix
def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Initialize a new matrix initially with zeros to store transposed matrix
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j] # Swap the indices to create transposed matrix
    
    return transposed

def main():
    rows = int(input("Enter the number of rows:\n"))
    cols = int(input("Enter the number of columns:\n"))

    # create matrix by calling the function create_matrix()
    matrix = create_matrix(rows, cols)
    
    print("The original matrix:")
    print_matrix(matrix)

    # create the transposed matrix
    transposed_matrix = transpose(matrix)
    
    print("Its transpose:")
    print_matrix(transposed_matrix)


main()
