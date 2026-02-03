s = input().split()
lst = []
tmp = []

for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        tmp.append(s[i])
    elif tmp == 0:
        lst.append(s[i])
    else:
        tmp.append(s[i])
        lst.append(tmp)
        tmp = []
if len(lst) == 0:
    lst.append(tmp)
elif tmp:
    lst.append(tmp)

if s[-1] == s[-2]:
    lst[-1].append(s[-1])
else:
    lst.append([s[-1]])

print(lst)