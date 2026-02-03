def convert_to_python_case(text):
    index_start, index_end = 0, 1
    repence = ''
    while index_end != len(text):
        if ord(text[index_end]) > 64 and ord(text[index_end]) < 91:
            repence += text[index_start:index_end] + '_'
            index_start = index_end
            index_end += 2
        else:
            index_end += 1
    if index_start != index_end:
        repence += text[index_start:]
    return repence.lower()
            


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))