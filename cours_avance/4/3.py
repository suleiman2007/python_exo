lst = []
n = int(input())
m = int(input())
for i in range(n):
    tmp = []
    for j in range(m):
        tmp.append(input())
    lst.append(tmp)

for i in range(n):
    for j in range(m):
        print(lst[i][j], end=' ')
    print()