n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
upper_quarter = 0
right_quarter = 0
lower_quarter = 0
left_quarter = 0

for i in range(n):
    for j in range(n):
        if i < j and i < n - 1 - j:
            upper_quarter += matrix[i][j]
        elif i < j and i > n - 1 - j:
            right_quarter += matrix[i][j]
        elif i > j and i > n - 1 - j:
            lower_quarter += matrix[i][j]
        elif i > j and i < n - 1 - j:
            left_quarter += matrix[i][j]

print(upper_quarter)
print(right_quarter)
print(lower_quarter)
print(left_quarter)