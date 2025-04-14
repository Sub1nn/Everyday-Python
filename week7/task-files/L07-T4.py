input_file = input("Give the name of the CSV file:\n")

file = open(input_file, 'r')

for row in file:
    column = row.strip().split(',')
    if len(column)>1:
        print(column[1].strip())

file.close()
