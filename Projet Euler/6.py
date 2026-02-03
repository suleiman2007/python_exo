def le_carré_de_la_somme():
    cnt = 0
    for i in range(101):
        cnt += i
    return cnt ** 2
def la_somme_des_carrés():
    cnt = []
    for i in range(1, 101):
        cnt.append(i**2)
    return sum(cnt)

print(le_carré_de_la_somme() - la_somme_des_carrés())