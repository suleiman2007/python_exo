n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
matrix_transposed = []
mirror_matrix = []

for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append(matrix[j][i])
    matrix_transposed.append(tmp)

for i in matrix_transposed:
    i.reverse()
    mirror_matrix.append(i)

for row in mirror_matrix:
    print(*row)