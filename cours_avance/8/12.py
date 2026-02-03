a,b,c = set(map(int, input().split())), set(map(int, input().split())), set(map(int, input().split()))
print(*sorted((a | b | c).difference(b,a), reverse=True))