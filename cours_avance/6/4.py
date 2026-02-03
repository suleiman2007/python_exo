n = int(input())
result = []
p = 0
while p != n:
    if len(result) < 3:
        result.append(1)
    else:
        result.append(sum(result[len(result)-3:]))
    p += 1
print(*result)
