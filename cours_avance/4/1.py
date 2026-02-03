n = int(input())
lst = [list(map(int, input().split())) for i in range(n)]
moyenne = [sum(i) / len(i) for i in lst]

for i in range(n):
    cnt = 0
    for j in range(n):
        if lst[i][j] > moyenne[i]:
            cnt += 1
    print(cnt)