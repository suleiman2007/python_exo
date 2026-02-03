from random import randint

def input_bet():
    while True:
        n = int(input('Entrez votre tarif choisi : '))
        if n in bet:
            return n
        else:
            print("Vous ne pouvez sélectionner que l'enchère suggérée")

def is_valid_num():
    while True:
        n = int(input('Devinez le nombre '))
        if 1 <= n <= selec_possible_number:
            return n
        else:
            print('Peut-être que vous allez entrer un nombre entier de 1 à', selec_possible_number, '?')

a = 5
# основная программа
def game(selec_attempts):
    global player_balance, bot_balance
    while selec_attempts != 0:
        num = is_valid_num()
        if num > random_n:
            print("Votre numéro est plus grand qu'il faut, essayez encore")
            selec_attempts -= 1
            print('Mais attention il vous reste', selec_attempts, 'tentative')
        elif num < random_n:
            print("Votre numéro est plus petit qu'il faut, essayez encore")
            selec_attempts -= 1
            print('Mais attention il vous reste', selec_attempts, 'tentative')
        else:
            print("Vous avez deviné, bien joué !")
            player_balance += selec_bet
            bot_balance -= selec_bet
            print('Votre solde est maintenant de ',player_balance)
            print("Le solde de l'adversaire est de", bot_balance)
            break
    if selec_attempts == 0: 
        print('Malheureusement vous avez perdu')
        player_balance -= selec_bet
        bot_balance += selec_bet
        print('Votre solde est maintenant de', player_balance)
        print("Le solde de l'adversaire est de", bot_balance)
        print('le nombre que vous deviez deviner est ', random_n)

# переигровка
def yes_or_no():
    if player_balance > 0 and bot_balance > 0:
        while True:
            s = input('Voulez-vous jouer encore plus? ("Oui" ou "Non") ')
            if s.lower() == 'oui' or s.lower() ==  'non':
                return s.lower()
            else:
                print("Oui ou Non il n'y a pas d'autre options")
    elif player_balance > 0 and bot_balance <= 0:
        print('Bravo tu as mis ton adversaire en faillite')
        print("Viens encore jouer c'étais intéressant de jouer avec toi!")
    elif bot_balance > 0 and player_balance <= 0:
        print("HAHAHAHA Le con t'as même plus d'argent")

def repley():
    repence = yes_or_no()
    if repence == 'oui':
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
print('Bonjour')
print("Dans ce jeux tu dois deviner le chiffre qui étais choisi par votre adversaire ! \n Si vous devinez: vous allez gagner de l'argent \n si vous perdez: vous allez en perdre")
print('Votre solde actuel: 1500')
print("Le solde d'adversaire: 2000")
print('Votre but est de mettre votre adversaire en faillite')
print('Les règles: \n Choisissez le montant que vous voulez miser (100, 250, 500, 750, 1000)')
print('En fonction de la mise, le nombre des nombres possible et de tentatives possibles augmentera:')
print('100 = les nombres possibles sont entre 1 - 100 tentatives possibles = 7 ','250 = les nombres possibles sont entre 1 - 250 ,tentatives possibles = 8', '500 les nombres possible sont entre = 1 - 400 ,tentatives possibles = 9', '750 = les nombres possible sont entre 1 - 700 ,tentatives possibles = 10', '1000 = les nombres possible sont entre 1 - 1100 ,tentatives possibles = 11', sep = '\n')

while player_balance != 0 or bot_balance != 0:
    start_game()
    game(selec_attempts)
    if repley():
        print('Super')
        print('votre solde est de', player_balance)
        print("Le solde d'adversaier est de", bot_balance)
    else:
        print('Alors a bien tôt')
        break


