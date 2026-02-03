# объявление функции
def draw_triangle():
    triangal = [' ', ' ', ' ', ' ', ' ', ' ', ' ', '*']
    print(*triangal, sep = '')
    for i in range(7):
        triangal.remove(' ')
        for i in range(2):
            triangal.append('*')
        print(*triangal, sep = '')

# основная программа
draw_triangle()  # вызов функции