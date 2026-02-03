def is_correct_bracket(text):
    if text.count('(') != text.count(')'):
        return False
    flag = True
    text = list(text)
    for i in range(len(text) // 2):
        for i in range(text.index('('), len(text)):
            if text[i] == ')':
                flag = True 
                text.remove('(')
                text.pop(i - 1)
                break
            else:
                flag = False
        if flag == False:
            return False
    if len(text) == 0:
        return True

        

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))