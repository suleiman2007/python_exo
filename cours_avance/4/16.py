n = int(input())
m = int(input())
lst = [list(map(int, input().split())) for i in range(n)]
index_largest = [0, 0]
largest = lst[0][0]

for i in range(n):
    for j in range(m):
        if lst[i][j] > largest:
            largest = lst[i][j]
            index_largest = [i, j]

print(*index_largest)