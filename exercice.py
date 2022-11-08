#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
from Exercices_GitHub.chapitre_06_1_malamao.exercice import frequence
import math
import turtle as t
import re

# TODO: Définissez vos fonction ici
def volume_masse_ellipsoide(a = 1, b = 1, c = 1, p = 1):
    volume = 4 / 3* math.pi *a*b*c
    masse = p * volume
    return (volume, masse)

def branche(longeur, epaisseur, angle):
    if longeur > 0 and epaisseur > 0:
        t.pensize(epaisseur)
        t.forward(longeur)
        t.right(angle)
        branche(longeur - 10, epaisseur - 1, angle - 5)
        t.left(angle * 2)
        branche(longeur - 10, epaisseur - 1, angle - 5)
        t.right(angle)
        t.backward(longeur)

def arbre():
    t.setheading(90)
    t.color("orange")
    branche(70, 7, 35)
    t.done()

def valide(saisie):
    if bool(re.match(r'^[atgc]+$', saisie)) == True:
        return True
    else:
        return False

def saisir(type):
    saisie = str(input(f"Entrez une {type} d'ADN avec des combinaisons de seulement a, t, g ou c:\n"))
    if valide(saisie):
        return saisie
    else:
        print(f"Cette {type} n'est pas valide")
        return saisir(type)


def proportion(chaine, sequence):
    propo = chaine.count(sequence) / len(chaine)

    return propo

def ADN():
    chaine = saisir("chaîne")
    sequence = saisir("séquence")


    propo = proportion(chaine, sequence)
    print("Il y a {0:.2f} % de {1}.".format(propo*100, sequence))

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(volume_masse_ellipsoide(3, 4, 5, 87))
    print("La lettre ayant la plus haute fréquence est: ", (lambda phrase: frequence(phrase)[0][1])(phrase = "big big test bb"))
    #arbre()
    ADN()
    pass
