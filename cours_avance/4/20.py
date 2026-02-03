def chanked(s, n):
    résultat = []
    for i in range(0, len(s), n):
        résultat.append(s[i:i+n])
    return résultat

s = input().split()
n = int(input())

print(chanked(s,n))