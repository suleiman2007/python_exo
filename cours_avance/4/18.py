n = int(input())

for i in range(n):
    tmp = []
    for j in range(n):
        if i < n - 1 - j:
            tmp.append(0)
        elif i > n - 1 - j:
            tmp.append(2)
        else:
            tmp.append(1)
    print(*tmp)