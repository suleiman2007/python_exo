n = int(input())
p = 0
triongle_paskal = [1]
tmp = triongle_paskal
while p != n:
    print(*triongle_paskal)
    tmp = triongle_paskal
    tmp.insert(0, 0)
    tmp.insert(len(triongle_paskal), 0)
    triongle_paskal = [0, 0]
    for i in range(len(tmp) - 1):
        triongle_paskal.insert(len(triongle_paskal) - 1, tmp[i] +  tmp[i + 1])
    del triongle_paskal[0]
    del triongle_paskal[-1]
    p += 1
