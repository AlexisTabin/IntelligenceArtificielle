from typing import List

from task_3.regle_sans_variables import RegleSansVariables as Regle

"""
Première idée pour la tâche 4 : On trie les règles et on ne prend que celles qui mènent vers une diagnostic positif.
Pour le patient que l'on cherche à diagnostiquer, on commence par enlever les critères age et sexe.
On enlève aussi ces critères pour chaque règle.
Ensuite, pour chaque règle dont la conclusion est 0 (pas malade), on regarde combien de critères du patient ne sont pas satisfait par la règle :
Si c'est > 2, on abandonne la règle pour ce patient.
Si c'est 0, le patient n'est pas affecté par cette règle.
Si c'est 1 ou 2, on garde la règle
A la fin, on se retrouve avec pour chaque patient, une règle associée,
qui nécéssite soit 0, 1 ou 2 changement pour que le patient soit diagnostiqué guerri

"""


def diagnostic_et_prescription(patient: dict, regles: List[Regle]):
    """Trouve par abduction si un patient et soignable ou non et comment le soigner
    @return diagnostic, prescription, code
    code = 1 si le patient est soignable, sert à compter le nb de personnes soignables
    """
    regle, problemes = trouve_regles_possibles(patient, regles)
    diagnostic = "nb problemes : {} => ".format(problemes)
    if problemes == 0:
        diagnostic += "Le patient n'est pas malade :)"
        return diagnostic, None, 0
    elif problemes > 2:
        diagnostic += "Le patient n'est pas soignable :("
        return diagnostic, None, 0
    else:
        diagnostic += "On peut soigner le patient"
        prescritpion = soigner_patient(patient, regle)
        return diagnostic, prescritpion, 1


def trouve_regles_possibles(patient: dict, regles: List[Regle]):
    """
    @param patient : un patient
    @param regles : Une liste de règle
    @return la règle la plus proche du patient
    et le nombre d'attribut du patient à changer pour qu'elle soit satisfaite
    """
    patient.pop('age', None)
    patient.pop('sex', None)
    regles_triees = [regle for regle in regles if regle.conclusion == 0]
    for regle in regles_triees:
        regle.conditions.pop('age', None)
        regle.conditions.pop('sex', None)

    # J'ai mis 10 ici, mais n'importe quel nb > 3 jouerait
    meilleure_regle = None, 10
    for regle in regles_triees:
        counter = 0
        for key, value in regle.conditions.items():
            if patient[key] != value:
                counter += 1
        if counter < meilleure_regle[1]:
            meilleure_regle = regle, counter
    return meilleure_regle


def soigner_patient(patient, regle):
    """
    @param patient : un patient
    @param regle : une règle
    @return string : prescription de quels attributs changer chez le patient
    pour que la règle s'applique
    """
    prescription = 'En changeant '
    for key, value in regle.conditions.items():
        if patient[key] != value:
            prescription += '{} = {} par {} et'.format(key, patient[key], value)
    prescription = prescription[:-3] + ', on guérit le patient'
    return prescription


def nb_patients_sauvables(patients: List[dict], regles: List[Regle]):
    """
    @param patients : Une liste de patients
    @param regles : Une liste de règle
    @return total : le nombre total de patients pouvant être guerris
    """
    total = 0
    for patient in patients:
        _, _, code = diagnostic_et_prescription(patient, regles)
        total += code
    return total
