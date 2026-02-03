n1 , n2 = 1, 2
result = 0
while n1 + n2 <= 4000000:
    n1, n2 = n2, n1 + n2
    if n2 % 2 == 0:
        result += n2

print(result)
