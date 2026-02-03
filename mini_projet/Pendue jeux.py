import random

word_list = ['programmation', 'arthur', 'jamais', 'musique', 'melancolie', 'etude', 'téléphone', 'amour', 'intellectuel', 'canne', 'mouchoir', 
'transport', 'clavier', 'ecouteur', 'alphabet', 'pendue', 'compte', 'raison', 'compliment', 'question', 'moment', 'conversation', 'feuille', 
'mot', 'tranquillite', 'confortabilité', 'main', 'pluit', 'maison', 'livre', 'file', 'chargeur', 'pyramide', 'imprimante', 'foot', 'oxygene', 
'orthogonal', 'voiture', 'barbe', 'alphabet', 'intergouvernementalisation','cheveux','oeil','veste','anticonstitutionnellement','lit','coussin',
'ordinateur', 'hasard', 'neige', 'exclamation', 'effondrement', 'cordialement', 'president', 'langue', 'essai', 'virgule', 'cicatrice', 'terre',
'proposition', 'jupiter', 'torse', 'imposteur', 'arobase', 'ophiophobie', 'fer', 'coucher', 'projet', 'latitude', 'serpent', 'lunette', 'serpent',
'education','aristocrate']

# функция получения случайного слова из списка слов
def get_word():
    word = random.choice(word_list)
    return word.upper()

# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                ''',
                '''
                   --------
                   |      
                   |      
                   |    
                   |      
                   |     
                   -------
                ''',
                '''
                   |      
                   |      
                   |    
                   |      
                   |     
                   -------
                ''',
                '''
                   -------
                ''',
                '''
                
                ''']
    return stages[tries]

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 10

    print('Jouons au pendue')
    print(display_hangman(tries))
    print(word_completion)
    print()

    while not guessed and tries > 0:
        guess = input('Saisissez une lettre ou un mot entier: ').upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('Vous avez déjà saisie cette lettre', guess)
            elif guess not in word:
                print("la lettre", guess, "n'est pas dans le mot")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print('Bien joué, la lettre ', guess, 'est dans le mot!')
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i in range(len(word)) if word[i] == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = ''.join(word_as_list)
                if '_' not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print('Vous avez saisie ce mot', guess)
            elif guess != word:
                print("Non ce n'est pas ce mot.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print('Saisissez une lettre ou un mot')
        print(display_hangman(tries))
        print(word_completion)
        print()
    if guessed:
        print('Vous avez trouvez le mot, Bien joué !!!')
    else:
        print('Vous avez perdu. Le mot que vous deviez deviner était : ' + word + '. Peut-être une autre fois !')

again = 'oui'

while again.lower() == 'oui':
    word = get_word()
    play(word)
    again = input('voulez-vous joué encore ? (saisisez oui ou non):')