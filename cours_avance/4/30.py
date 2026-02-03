location_input = input()
table1 = [7, 6, 5, 4, 3, 2, 1, 0]
table2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
x1 = table1.index(int(location_input[1]) - 1)
y1 = table2.index(location_input[0])
matrix = [['.' for j in range(8)] for i in range(8)]

for i in range(8):
    for j in range(8):
        if abs(x1 - i) * abs(y1 - j) == 2:
            matrix[i][j] = '*'

matrix[x1][y1] = 'N'

[print(*i) for i in matrix]