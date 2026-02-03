n, flag = int(input()), True
matrix = [list(map(int, input().split())) for i in range(n)]
for i in matrix:
    if flag:
        for j in i:
            if 0 > j or j > n or i.count(j) > 0:
                flag = False
                break
    else:
        print('NO')
        break
for i in range(n):
    if flag:
        colone = []
        for j in range(n):
            if 0 > matrix[j][i] or matrix[j][i] > n or matrix[j][i] not in colone:
                flag = False
                break
            else:
                colone.append(matrix[j][i])
    else:
        print('NO')

if flag:
    print('YES')