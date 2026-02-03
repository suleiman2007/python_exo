from datetime import datetime

first_now = datetime.now()

result = set()
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        if str(i * j) == str(i * j)[::-1]:
            result.add(i * j)
print(max(result))
second_after = datetime.now()
print(second_after - first_now)

first_now = datetime.now()
r = 0
for i in range(100, 999):
    for j in range(100, 999):
        tmp = i * j
        r = tmp if str(tmp) == str(tmp)[::-1] and tmp > r else r
        

print(r)

second_after = datetime.now()
print(second_after - first_now)