n, m = map(int, input().split())
matrix = [[0 for j in range(m)] for i in range(n)]
upper = [0, [0, m - 2]]
rigth = [[0, n - 2], m - 1]
lower = [n - 1, [1, m - 1]]
left = [[1, m - 1], 0]
cnt = 1
i = 0
j = 0

while cnt != n * m + 1:
    if upper[0] == i and upper[1][0] <= j <= upper[1][1]:
        matrix[i][j] += cnt
        cnt += 1
        j += 1
    elif rigth[0][0] <= i <= rigth[0][1] and j == rigth[1]:
        matrix[i][j] += cnt
        cnt += 1
        i += 1
    elif i == lower[0] and lower[1][0] <= j <= lower[1][1]:
        matrix[i][j] += cnt
        cnt += 1
        j -= 1
    else:
        if i - 1 == j:
            matrix[i][j] += cnt
            cnt += 1
            j += 1
            upper[0] += 1
            upper[1][0] += 1
            upper[1][1] -= 1
            rigth[0][0] += 1
            rigth[0][1] -= 1
            rigth[1] -= 1
            lower[0] -= 1
            lower[1][0] += 1
            lower[1][1] -= 1
            left[0][0] += 1
            left[0][1] -= 1
            left[1] += 1
        else:
            matrix[i][j] += cnt
            cnt += 1
            i -= 1

[print(*i) for i in matrix]