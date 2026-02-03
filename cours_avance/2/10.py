n = int(input())
cnt = []
for i in range(n):
    flag = True
    tmp = input()
    for j in 'anton':
        if j in tmp:
            tmp = tmp[tmp.find(j):]
        else:
            flag = False
            break
    if flag:
        cnt.append(i + 1)
print(*cnt)