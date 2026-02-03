# объявление функции
def print_digit_sum(num):
    num = list(map(int, num))
    print(sum(num))
    
# считываем данные
n = input()

# вызываем функцию
print_digit_sum(n)