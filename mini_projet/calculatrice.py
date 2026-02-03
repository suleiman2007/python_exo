from math import sqrt
def addition(a, b):
    return a + b
def soustraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b
def reste(a, b):
    return a // b
def quotient(a, b):
    return a % b
def racine_carée(x):
    return sqrt(x)

print('Bonjour vous êtes à la calcultrice moderne')
print("Pour utiliser cette calculatrice vous devez écrire l'un des mots suivant:")
print('''"addition" : addition de deux nombres
         "soustraction" : soustraction de deux nombres
         "multiplication" : multiplication de deux nombres
         "division" : division de deux nombres
         "quotient" : quotient de la division euclidienne de deux nombres
         "reste" : reste de la division euclidienne de deux nombres
         "racine carée" : racine carée d'un nombre ''')
choix = input("Qu'est-ce que vous voulez que je fasse comme calcule :")

if choix == 'addition':
    print(addition(int(input('Saisissez un nombre pour la valeur a :')), int(input('Saisissez un nombre pour la valeur b :'))))
elif choix == 'soustraction':
    print(soustraction(int(input('Saisissez un nombre pour la valeur a :')), int(input('Saisissez un nombre pour la valeur b :'))))
elif choix == 'multiplication':
    print(multiplication(int(input('Saisissez un nombre pour la valeur a :')), int(input('Saisissez un nombre pour la valeur b :'))))
elif choix == 'division':
    print(division(int(input('Saisissez un nombre pour la valeur a :')), int(input('Saisissez un nombre pour la valeur b :'))))
elif choix == 'quotient':
    print(quotient(int(input('Saisissez un nombre pour la valeur a :')), int(input('Saisissez un nombre pour la valeur b :'))))
elif choix == 'reste':
    print(reste(int(input('Saisissez un nombre pour la valeur a :')), int(input('Saisissez un nombre pour la valeur b :'))))
elif choix == 'racine carée':
    print(racine_carée(int(input('Saisissez un nombre pour la valeur a : '))))
else:
    print("Vous avez mal saise votre choix de calcule")