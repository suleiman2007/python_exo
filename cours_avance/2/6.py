timur = input()
ruslan = input()
lst = ["камень", "бумага", "ножницы", "Спок", "ящерица"]

if timur == ruslan:
    print('ничья')
elif (lst.index(timur) - lst.index(ruslan)) % 2 == 0:
    tmp = max(lst.index(timur), lst.index(ruslan))
    if tmp == timur.index(lst):
        print('Тимур')
    else:
        print('Руслан')
else:
    tmp = min(lst.index(timur), lst.index(ruslan))
    if tmp == timur.index(lst):
        print('Тимур')
    else:
        print('Руслан')