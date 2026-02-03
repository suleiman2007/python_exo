# объявление функции
def draw_box():
    print('*' * 10)
    for i in range(1, 13):
        print('*' + 8 * ' ' + '*')
    print('*' * 10)

# основная программа
draw_box()  # вызов функции