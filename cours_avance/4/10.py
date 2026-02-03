n, m = map(int, input().split())
matrix = [[None for j in range(m)]for i in range(n)]
cnt = 1
sum_index = 0
while cnt != (n * m + 1):
    for i in range(n):
        for j in range(m):
            if i + j == sum_index:
                matrix[i][j] = cnt 
                cnt += 1
                break
    sum_index += 1

[print(*i) for i in matrix]