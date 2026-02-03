s = list(range(2, 2000001))
for i in s:
    if i:
        for j in range(i*2, 2000001, i):
            s[j - 2] = 0

print(sum(s))