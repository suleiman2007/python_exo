def flavil(n, k):
    r = 0
    for i in range(1, n + 1):
        r = (r + k) % i
    return r + 1

num, shag = int(input()), int(input())
print(flavil(num, shag))