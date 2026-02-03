from random import randint

def input_bet():
    while True:
        n = int(input('Введите выбраную ствыку: '))
        if n in bet:
            return n
        else:
            print('Вы можете выбрать только предложенную ставку')

def is_valid_num():
    while True:
        n = int(input('Угадай число '))
        if 1 <= n <= selec_possible_number:
            return n
        else:
            print('А может быть все-таки введем целое число от 1 до', selec_possible_number, '?')

a = 5
# основная программа
def game(selec_attempts):
    global player_balance, bot_balance
    while selec_attempts != 0:
        num = is_valid_num()
        if num > random_n:
            print('Ваше число больше загаданного, попробуйте еще разок')
            selec_attempts -= 1
            print('Осторожно у вас осталось', selec_attempts, 'попытак')
        elif num < random_n:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            selec_attempts -= 1
            print('Осторожно у вас осталось', selec_attempts, 'попытак')
        else:
            print('Вы угадали, поздравляем!')
            player_balance -= selec_bet
            bot_balance += selec_bet
            print('Теперь вашь баланс равен',player_balance)
            print('Баланс противника равен', bot_balance)
            break
    if selec_attempts == 0: 
        print('Жаль но вы проиграли')
        player_balance -= selec_bet
        bot_balance += selec_bet
        print('Теперь вашь баланс равен', player_balance)
        print('Баланс противника равен', bot_balance)

# переигровка
def yes_or_no():
    while True:
        s = input('Хотите поиграть еще?(Да или Нет) ')
        if s.lower() == 'да' or s.lower() ==  'нет':
            return s.lower()
        else:
            print('Да или Нет третего не дано,')

def repley():
    repence = yes_or_no()
    if repence == 'да':
        return True
    else:
        return False

# переменые
bet = [100, 250, 500, 750, 1000]
attempts = [7, 8, 9, 10, 11]
possible_number = [100, 250, 400, 700, 1100]

def start_game():
    global selec_bet, selec_attempts, selec_possible_number, random_n
    selec_bet = input_bet()
    selec_attempts = int(attempts[bet.index(selec_bet)])
    selec_possible_number = int(possible_number[bet.index(selec_bet)])
    random_n = randint(1, selec_possible_number)

player_balance = 1500
bot_balance = 2000

# основная программа
print('Добро пожаловать')
print('Сдесь ты должен угадать числа загадоное твоим обонентом! \n Угадаешь: выйграешь денег \n Проиграешь: потеряешь')
print('Ваш текуший баланс: 1500')
print('Баланс вашего обонента: 2000')
print('Твоя цель обонкротить обонента и не стать самаму')
print('Правила токавы: \n Выбираешь сумму на которую хочешь поставить (100, 250, 500, 750, 1000)')
print('Смотря по ставке количество возможных чисел и попытак возростет:')
print('100 = возможные числа 1 - 100 ,попытки = 7 ','250 = возможные числа 1 - 250 ,попытки = 8', '500 возможные числа = 1 - 400 ,попытки = 9', '750 = возможные числа 1 - 700 ,попытки = 10', '1000 = возможные числа 1 - 1100 ,попытки = 11', sep = '\n')

while player_balance != 0 or bot_balance != 0:
    start_game()
    game(selec_attempts)
    if repley():
        print('Отлично!')
        print('Вашь баланс равен', player_balance)
        print('Баланс противника равен', bot_balance)
    else:
        print('Жаль, ну тогда до новых встречь')
        break

if player_balance > 0 and bot_balance <= 0:
    print('Молодец ты обонкротил противника')
    print('Приходи еще стобой было интерестно играть!')
elif bot_balance > 0 and player_balance <= 0:
    print('Хахахахах ЛАШАРА')
