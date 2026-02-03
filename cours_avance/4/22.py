n = int(input())
lst = []
som = 0
for i in range(n):
    lst.append(input().split())

for i in range(n):
    som += int(lst[i][i])

print(som)