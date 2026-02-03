def chiffrer():
    chiffre = ''
    txt = input('Ведите текст каторый вы хотите зашифровать(на Русском или Англиском) \n')
    k = int(input('На сколько символов должен передвигаться изначальный символ? '))
    if ord(txt[0].lower()) in en_alphabet:
        for i in range(len(txt)):
            if ord(txt[i].lower()) in en_alphabet:
                tmp = ord(txt[i].lower()) + k
                if tmp in en_alphabet:
                    if txt[i] == txt[i].upper():
                        chiffre += chr(tmp).upper()
                    else:
                        chiffre += chr(tmp)
                else: 
                    if txt[i] == txt[i].upper():
                        chiffre += chr(tmp - 26).upper()
                    else:
                        chiffre += chr(tmp - 26)
            else:
                chiffre += txt[i]
    elif ord(txt[0].lower()) in ru_alphabet:
        for i in range(len(txt)):
            if ord(txt[i].lower()) in ru_alphabet:
                tmp = ord(txt[i].lower()) + k
                if tmp in ru_alphabet:
                    if txt[i] == txt[i].upper():
                        chiffre += chr(tmp).upper()
                    else:
                        chiffre += chr(tmp)
                else:
                    if txt[i] == txt[i].upper():
                        chiffre += chr(tmp - 32).upper()
                    else:
                        chiffre += chr(tmp - 32)
            else:
                chiffre += txt[i]
    return chiffre

def dechiffrer():
    dechiffre = ''
    txt =  input('Ведите текст каторый вы хотите расшифровать(на Русском или Англиском')
    k = int(input('На сколько символов был передвежон изначальный символ? '))
    if ord(txt[0].lower()) in en_alphabet:
        for i in range(len(txt)):
            if ord(txt[i].lower()) in en_alphabet:
                tmp = ord(txt[i].lower()) - k
                if tmp in en_alphabet:
                    if txt[i] == txt[i].upper():
                        dechiffre += chr(tmp).upper()
                    else:
                        dechiffre += chr(tmp)
                else:
                    if txt[i] == txt[i].upper():
                        dechiffre += chr(tmp + 26).upper()
                    else:
                        dechiffre += chr(tmp + 26)
            else:
                dechiffre += txt[i]
        return dechiffre
    elif ord(txt[0].lower()) in ru_alphabet:
        for i in range(len(txt)):
            if ord(txt[i].lower()) in ru_alphabet:
                tmp = ord(txt[i].lower()) - k
                if tmp in ru_alphabet:
                    if txt[i] == txt[i].upper():
                        dechiffre += chr(tmp).upper()
                    else:
                        dechiffre += chr(tmp)
                else:
                    if txt[i] == txt[i].upper():
                        dechiffre += chr(tmp + 32).upper()
                    else:
                        dechiffre += chr(tmp + 32)
            else:
                dechiffre += txt[i]
        return dechiffre
    
en_alphabet = [j for j in range(97, 123)]
ru_alphabet = [i for i in range(1072, 1104)]

chiffrer_or_dechiffrer = input('Вам нужно "з" (зашифровать) текст или "р" (расшифровать) его? ')

if chiffrer_or_dechiffrer == 'з':
    print(chiffrer())
elif chiffrer_or_dechiffrer == 'р':
    print(dechiffrer())
 