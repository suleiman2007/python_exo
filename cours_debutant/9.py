# объявление функции
def draw_triangle(fill, base):
    for i in range(1, base // 2 + 2):
        print(fill * i)
        p = i
    p -= 1
    while p > 0:
        print(fill * p)
        p -= 1

# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)