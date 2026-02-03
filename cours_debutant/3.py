from math import *
def quick_merge(num):
    list1, list2 = '', ''
    for i in range(ceil(num / 2)):
        list1 += input()
        list1 += ' '
    for i in range(floor(num / 2)):
        list2 += input()
        list2 += ' '

    result = []
    p1, p2 = 0, 0
    list1 = list1.split()
    list2 = list2.split()

    while p1 < len(list1) and p2 < len(list2):
        if int(list1[p1]) <= int(list2[p2]):
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):
        result += list1[p1:]
    if p2 < len(list2):
        result += list2[p2:]
    
    print(*result)

n = int(input())

quick_merge(n)