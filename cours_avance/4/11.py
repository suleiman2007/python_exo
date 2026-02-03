n, m = map(int, input().split())
matrix = [[str(i * m + j) for j in range(1, m + 1)] for i in range(n)]
[print(*matrix[i - 1][::-1]) if i % 2 == 0 else print(*matrix[i - 1]) for i in range(1, n + 1)]
