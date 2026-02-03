from math import sqrt

def calcule_x0(a, b):
    return (-b) / (2*a)

def calcule_x1_x2(delta, a, b):
    return (-b - sqrt(delta)) / (2*a), (-b + sqrt(delta)) / (2*a)

a = float(input('Donnez la valeur de a '))
b = float(input('Donnez la valeur de b '))
c = float(input('Donnez la valeur de c '))
delta = (b)**2 - 4*(a)*(c)


print(delta)

if delta > 0:
    print(*calcule_x1_x2(delta, a, b))
elif delta == 0:
    print(calcule_x0(a, b))
else:
    print('Pas de solutions dans R')