n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
matrix_transposed = []
for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append(matrix[j][i])
    matrix_transposed.append(tmp)
[print(*i) for i in matrix_transposed]