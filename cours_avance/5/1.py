s = input().split()
n = int(input())
res = []
for i in range(n):
    res.append(s[i::n])
print(res)