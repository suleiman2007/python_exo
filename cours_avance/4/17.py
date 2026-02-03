n = int(input())
m = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
m1, m2 = [int(i) for i in input().split()]

for i in range(n):
    matrix[i][m1], matrix[i][m2] = matrix[i][m2], matrix[i][m1]

for i in matrix:
    print(*i)