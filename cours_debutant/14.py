# объявление функции
def is_magic(date):
    date = date.split('.')
    day = int(date[0])
    month = int(date[1])
    year = date[2]
    if day * month == int(year[2:]):
        return True
    else:
        return False

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))