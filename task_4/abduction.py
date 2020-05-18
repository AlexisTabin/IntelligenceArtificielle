from typing import List

from task_3.regle_sans_variables import RegleSansVariables as Regle

"""
Première idée pour la tâche 4 : On trie les règles et on ne prend que celles qui mènent vers une diagnostic positif.
Pour le patient que l'on cherche à diagnostiquer, on commence par enlever les critères age et sexe.
Ensuite, pour chaque règle dont la conclusion est 0 (pas malade), on regarde combien de critères du patient ne sont pas satisfait par la règle :
Si c'est > 2, on abandonne la règle pour ce patient.
Si c'est 0, le patient n'est pas affecté par cette règle.
Si c'est 1 ou 2, on garde la règle
A la fin, on se retrouve avec pour chaque patient, une règle associée,
qui nécéssite soit 0, 1 ou 2 changement pour que le patient soit diagnostiqué guerri

"""


def abuction(patient: dict, regles: List[Regle]):
    regle, problemes = trouve_regles_possibles(patient, regles)
    print("nb problems : {}".format(problemes))
    if problemes == 0:
        print("Le patient n'est pas malade :)")
    elif problemes > 2:
        print("Le patient n'est pas soignable :(")
    else:
        print("On peut soigner le patient")


def trouve_regles_possibles(patient: dict, regles: List[Regle]):
    regles_triees = [regle for regle in regles if regle.conclusion == 0]
    meilleure_regle = None, 10
    for regle in regles_triees:
        counter = 0
        for key, value in regle.conditions.items():
            if patient[key] != value:
                counter += 1
        if counter < meilleure_regle[1]:
            meilleure_regle = regle, counter
    return meilleure_regle
