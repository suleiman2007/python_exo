def PivautGausse(sisteme):    
    coef_1 = 0
    coef_2 = 0
    for ligne_base in range(len(sisteme) - 1):
        for ligne_change in range(ligne_base+1, len(sisteme)):
            coef_1 = sisteme[ligne_base][ligne_base]
            coef_2 = sisteme[ligne_change][ligne_base]
            for element in range(len(sisteme[ligne_base])):
                sisteme[ligne_change][element] = sisteme[ligne_change][element] * coef_1 - sisteme[ligne_base][element] * coef_2

    inconnues = [1 for i in range(len(sisteme))]
    sisteme = sisteme[::-1]

    for index_ligne in range(len(sisteme)):
        for mult in range(len(inconnues)):
            sisteme[index_ligne][mult] *= inconnues[mult]
        index_diviseur = len(sisteme) - 1 - index_ligne
        for element in range(len(sisteme)):
            if element == index_diviseur:
                continue
            if sisteme[index_ligne][element] >= 0:
                sisteme[index_ligne][-1] -= abs(sisteme[index_ligne][element])
            else:
                sisteme[index_ligne][-1] += abs(sisteme[index_ligne][element])
        inconnues[index_diviseur] = int(sisteme[index_ligne][-1] / sisteme[index_ligne][index_diviseur])

    [print(f'inconnues{i + 1} : {inconnues[i]}') for i in range(len(inconnues))]

n_inconnu = int(input("Combien il y a d'inconnues "))
sisteme_input = []
for i in range(1, n_inconnu+1):
    sisteme_input.append(list(map(int, input('Ecrivez les coefficients et le resultat juste aprés separant avec les vergulles ').split())))

PivautGausse(sisteme_input)
