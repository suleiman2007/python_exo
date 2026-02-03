def SAC(n):
    num_SAC = ''
    while len(n) >= 4:
        num_SAC = ',' + ''.join(n[-3::1]) + num_SAC
        n = n[:-3:1]
    num_SAC = ''.join(n) + num_SAC
    return num_SAC

num = list(input())

print(SAC(num))