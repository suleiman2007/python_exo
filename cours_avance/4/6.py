n, m = map(int, input().split())
matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = j * n + i + 1

for i in matrix:
    print(*i)