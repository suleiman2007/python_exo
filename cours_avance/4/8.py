n = int(input())
[print(*[1 if (i <= j and i <= n - 1 - j) or (i >= j and i >= n - 1 - j) else 0 for j in range(n)]) for i in range(n)]