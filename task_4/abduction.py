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

Attention :
Pour le moment, une règle peut avoir plusieurs fois le même critère (ex. : age = 2, age = 3, age = 5)
ce qui veut dire qu'un patient avec age = 4 éliminerait cette règle : ça ne devrait pas être le cas !!

Pour éviter cela : Modifier la manière dont les règles sont stockées pour stocker les conditions sous la forme 
de dictionnaire (regle = { "age" : [2,3,5], "sex" : 1, "cp" = [0,1] } )
"""
def abuction(patient : List[str], regles : List[Regle]):
    print("abduction")


