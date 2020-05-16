from typing import List

from task_3.moteur_sans_variables.regle_sans_variables import RegleSansVariables as Regle
"""
Première idée pour la tâche 4 : On trie les règles et on ne prend que celles qui mènent vers une diagnostic positif.
Pour le patient que l'on cherche à diagnostiquer, on commence par enlever les critères age et sexe.
Ensuite, pour chaque règle positive, on regarde combien de critères du patient ne sont pas satisfait par la règle :
Si c'est > 2, on abandonne la règle pour ce patient.
Si c'est 0, le patient n'est pas malade.
Si c'est 1, on regarde si la règle contient une autre valeur pour ce critère, si ce n'est pas le cas, on abandonne la règle.
Si c'est 2, Pour chacun des 2 critères, on regarde si la règle contient une autre valeur pour ce critère, Si poour l'un des deux,
        ça n'est pas le cas => on abandonne la règle
A la fin, on se retrouve avec pour chaque patient, une règle associée,
qui nécéssite soit 0, 1 ou 2 changement pour que le patient soit diagnostiqué guerri
"""
def abuction(patient : List[str], regles : List[Regle]):
    print("abduction")


    print(regles)