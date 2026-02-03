def fonction():
    p = 1
    while True:
        flag = True
        for i in [2, 3, 5, 7, 11, 13, 17, 19]:
            if p % i != 0:
                flag = False
                break
        if flag:
            return p
        p += 1

print(fonction())