def chifrer(text):
    tt = list(text + '.')
    chiffre = []
    tmp = []
    mot = []
    signe = []
    while len(chiffre) - 1 != len(text):
        for i in tt:
            if i.isalpha():
                mot += i  
            else:
                signe += i
                for y in mot:
                    tmp = ord(y) + len(mot)
                    if chr(tmp).isalpha():
                        chiffre += chr(tmp)
                    elif 90 < tmp < 97 or tmp > 122:
                        chiffre += chr(tmp - 26)
                chiffre += signe
                mot = []
                signe = []
    return ''.join(chiffre[:len(chiffre)-1])
                
text_pr_chif = input()
print(chifrer(text_pr_chif))