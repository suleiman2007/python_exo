import Labyrinthe
import graph
import random
import sys

sys.setrecursionlimit(2000)

#Affichage du labyrinthe
def segment_horiz(y, x1, x2, c):
    for x in range(x1, x2):
        graph.plot(y, x, c)

def rectangle(y1, y2, x1, x2, c):
    for y in range(y1, y2):
        segment_horiz(y, x1, x2, c)

def dessiner_lab(h, l):
    graph.open_win(h, l, 10)
    for i in range(h):
        for j in range(l):
            rectangle(i, i+1, j, j+1, ['black', 'white', 'blue', 'red'][laby[i][j]])


#Recherche 
def indice(lst, n):
    for i in range(len(lst)):
        if lst[i] == n:
            return i

def coord(lst, n):
    for j in range(len(lst)):
        coord_y = indice(lst[j], n)
        if coord_y:
            return (j, coord_y)

def entree(lst):
    return coord(lst, 2)

def sortie(lst):
    return coord(lst, 3)

def taille_laby(lab):
    return (len(lab), len(lab[0]))

def voisins_laby_fin(lgn, col, nb_lignes, nb_colonnes):
    haut = (lgn - 1, col)
    bas = (lgn + 1, col)
    droite = (lgn, col + 1)
    gauche = (lgn, col - 1)
    result = []
    for i in [haut, bas, droite, gauche]:
        if 0 <= i[0] <= nb_lignes and 0 <= i[1] <= nb_colonnes:
            result.append(i)
    return result

def voisins_laby_acc(couple, lab):
    taille = taille_laby(lab)
    voisins = voisins_laby_fin(couple[0], couple[1], taille[0]-1, taille[1]-1)
    resultat = []
    for i in voisins:
        x, y = i
        if lab[x][y]:
            resultat.append(i)
    return resultat

def trouver_chemin(lgn, col, lab, parcours, srt):
    voisins = voisins_laby_acc((lgn, col), lab)
    if srt in parcours:
        return []
    for v in voisins:
        if v not in parcours:
            if v != srt:
                rectangle(v[0], v[0]+1, v[1], v[1]+1, 'green')
                graph.refresh()
            parcours.append(v)
            lst = trouver_chemin(v[0], v[1], lab, parcours, srt)
            if lst != None:
                return [v] + lst
            rectangle(v[0], v[0]+1, v[1], v[1]+1, 'gray')
            graph.refresh()
    return None

hauteur = 99
largeur = 101

laby = Labyrinthe.creer(largeur, hauteur)

dessiner_lab(hauteur, largeur)
etr = entree(laby)

print(trouver_chemin(*etr, laby, [etr], sortie(laby)))
graph.wait()
