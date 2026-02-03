from random import sample

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters =  'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '#$%&*+-=?@^_'
chars = ''

print('Добро пожаловать в генекатор поролей')

counter_pass= int(input('Сколько паролей вам нужно? '))
length_pass = int(input('Сколько символов должно быть в одном пароле? '))
digits_pass = input('Нужно ли чтобы в нем садержались цифры? ')
lower_lett_pass = input('Нужно ли чтобы в нем садержались прописные буквы? ')
upper_lett_pass = input('Нужно ли чтобы в нем садержались заглавные буквы? ')
punctuation_pass = input('Нужно ли чтобы в нем садержались знаки припинания(#$%&*+-=?@^_)? ')

if digits_pass.lower() == "да":
    chars += digits
if lower_lett_pass.lower() == 'да':
    chars += lowercase_letters
if upper_lett_pass.lower() == 'да':
    chars += uppercase_letters
if punctuation_pass.lower() == 'да':
    chars += punctuation

for i in range(counter_pass):
    print(*sample(chars, length_pass), sep = '')
