def condition():
    intervale = [i for i in range(1, n**2 + 1)]
    tmp = [j for i in matrix for j in i]
    for i in intervale:
        if i not in tmp:
            return False
    return True 

def ligne():
    for i in matrix:
        tmp = sum(i)
        if somme_principale != tmp:
            return False
    return True

def colone():
    tmp = 0
    for mot in range(n):
            tmp =+ sum([matrix[i][mot] for i in range(n)])
    if tmp != somme_principale:
        return False
    return True

def diagonale_principale():
    tmp = sum([matrix[i][i] for i in range(n)])
    if tmp != somme_principale:
        return False
    return True

def diogonale_seсondaire():
    for i in range(n):
        for j in range(n):
            tmp = 0
            if i == n - 1 - j:
                tmp += matrix[i][j]
    if somme_principale != tmp:
        return False
    return True
n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
somme_principale = sum(matrix[0])

if condition():
    if ligne() and colone() and diagonale_principale() and diogonale_seсondaire:
        print('YES')
    else:
        print('NO')
else:
    print('NO')