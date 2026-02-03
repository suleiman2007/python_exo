import copy
n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
b = copy.deepcopy(a)
matrix_result = [[0 for i in range(n)] for i in range(n)]
m = int(input())

for p in range(m - 1):
    for x in range(n):
        for y in range(n):
            for i in range(n):
                matrix_result[x][y] += b[x][i] * a[i][y]
    b = copy.deepcopy(matrix_result)
    matrix_result = [[0 for i in range(n)] for i in range(n)]


[print(*i) for i in b]
