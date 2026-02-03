n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
matrix.reverse()

for rov in matrix:
    print(*rov)