lst = [i for i in input().split()]
result = []
for i in range(0, len(lst) - 1, 2):
    x, y = lst[i + 1], lst[i]
    result.append(x)
    result.append(y)
if len(lst) % 2 != 0:
    result.extend(lst[-1])
print(*result)
