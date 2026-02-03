n, m = map(int, input().split())
[print(*[(i  + j) % m + 1 for j in range(m)]) for i in range(n)]