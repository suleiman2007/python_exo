n = int(input()) 
matrix = [list(map(int, input().split())) for i in range(n)]
maximum = matrix[0][-1]
for i in range(n):
    for j in range(n):
        if i <= j and i >= n - 1 - j or i >= j and i >= n - 1 - j:
            if matrix[i][j] > maximum:
                maximum = matrix[i][j]

print(maximum)