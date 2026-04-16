matrix = []

for i in range(3):
    matrix.append([])
    for j in range(3):
        matrix[i].append(int(input("Enter a number: ")))

transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("ORIGINAL MATRIX")
print(matrix)

print("TRANSPOSE MATRIX")
print(transpose)

