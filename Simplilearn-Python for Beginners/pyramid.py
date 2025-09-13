# left align pyramid
n = int(input('Enter a number for pyramid: '))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end='')
    print()
    
    
    
# make a matrix
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"Enter the element at position [{i}][{j}]: "))
        row.append(value)
    matrix.append(row)

print("Your matrix is:")
print(matrix)