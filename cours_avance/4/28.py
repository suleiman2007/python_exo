from math import floor, sqrt
n1, m1 = map(int, input().split())
a1 = [list(map(int, input().split())) for i in range(n1)]
input()
n2, m2 = map(int, input().split())
b1 = [list(map(int, input().split())) for i in range(n2)]

matrix_result = [[0 for i in range(m2)] for i in range(n1)]

for x in range(n1):
    for y in range(n1):
        for i in range(m1):
            matrix_result[x][y] += a1[x][i] * b1[i][y]

[print(*i) for i in matrix_result]