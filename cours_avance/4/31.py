n, m = map(int, input().split())
matrix = []

for i in range(n):
    tmp = []
    for j in range(m):
        if i % 2 == 0 and j % 2 == 0 or i % 2 != 0 and j % 2 != 0:
            tmp.append('.')
        else:
            tmp.append('*')
    matrix.append(tmp)

for i in matrix:
    print(*i)