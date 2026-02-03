# объявление функции
def is_palindrome(text):
    s = ''
    for i in list(text):
        if ord(i) >= 65:
            s += i.lower()
    if s == s[::-1]:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))