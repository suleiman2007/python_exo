from math import floor
n = int(input())
matrix = [['.' for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == j or j == floor(n / 2) or i == floor(n / 2) or i == n - 1 - j:
            matrix[i][j] = '*'

for i in matrix:
    print(*i, sep=' ')
