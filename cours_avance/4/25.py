n = int(input())
m = int(input())
mult = []
for a in range(n):
    tmp = []
    for b in range(m):
        tmp.append('0')
    mult.append(tmp)

for i in range(n):
    for j in range(m):
        mult[i][j] = i * j
        print(str(mult[i][j]).ljust(3), end = '')
    print()