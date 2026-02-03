résultat = [[]]
index = 1
s = input().split()
tmp = len(s)
for i in range(len(s)):
    for j in range(tmp):
        résultat.append(s[j:index + j])
    index += 1
    tmp -= 1
print(résultat)