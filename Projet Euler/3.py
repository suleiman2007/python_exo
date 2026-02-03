n =  600851475143
count = 1
while n != 1:
    count += 1
    if n % count == 0:
        n /= count
    

print(count)
print(n % count == 0)