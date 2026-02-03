n, m = map(int, input().split())
cnt = 1

for i in range(n):
    for j in range(m):
        print(str(cnt).ljust(3), end='')
        cnt += 1
    print()
