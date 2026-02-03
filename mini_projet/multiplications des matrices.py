m1 = [[2, 1, 6], [3, 5, 2], [4, 3, 8]]
m2 = [[7, 2, 1], [4, 5, 3], [6, 8, 9]]

liste = [list() for i in range(len(m1))]


for index_ligne in range(len(m1)):
    for index_colone in range(len(m1)):
        tmp = 0
        for index_element in range(len(m1)):
            tmp += m1[index_ligne][index_element] * m2[index_element][index_colone]
        liste[index_ligne].append(tmp)

[print(*i) for i in liste]