def produit(lst_n):
    for i in range(len(lst_n)):
        for j in range(i+1 , len(lst_n)):
            if lst_n[i] * lst_n[j] == multip_product:
                return 'ДА'
    return 'НЕТ'


n = int(input())
lst_num = []
for i in range(n):
    lst_num.append(int(input()))

multip_product = int(input())

print(produit(lst_num))