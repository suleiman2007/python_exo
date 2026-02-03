n = int(input())
p = 0
triongle_paskal = [0, 1, 0]
while p != n:
    tmp = triongle_paskal
    triongle_paskal = []
    for i in range(len(tmp) - 1):
        triongle_paskal.append(tmp[i] +  tmp[i + 1])
    triongle_paskal.insert(0, 0)
    triongle_paskal.insert(len(triongle_paskal), 0)
    p += 1

del triongle_paskal[0]
del triongle_paskal[-1]
print(triongle_paskal)
