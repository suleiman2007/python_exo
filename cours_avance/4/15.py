n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
largest = matrix[0][0]


for i in range(n):
    for j in range(n):
        if i >= j and i <= n - 1 - j and matrix[i][j] > largest:
            largest = matrix[i][j]
        elif i <= j and i >= n - 1 - j and matrix[i][j] > largest:
            largest = matrix[i][j]

print(largest)