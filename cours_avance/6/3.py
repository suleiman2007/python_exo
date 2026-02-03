n = int(input())
eleves_total = [tuple(map(str, input().split())) for i in range(n)]
[print(*i) for i in eleves_total]
print()
[print(*i) for i in eleves_total if int(i[1]) >= 4]