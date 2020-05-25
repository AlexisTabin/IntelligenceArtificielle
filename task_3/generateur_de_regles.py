from moteur_id3.noeud_de_decision import NoeudDeDecision
from task_3.regle_sans_variables import RegleSansVariables as Regle


def generateur_de_regles(arbre):
    """ Idée pour générer toutes les règles de l'arbre de décision :
    A partir de l'arbre final, il faut parcourir chaque branche une fois, jusqu'à la feuille
    L'idée est d'appeler le depth first search algorithm avec comme but un noeud qui n'est pas dans l'arbre.
    De cette manière, l'algorithme va avoir le comportement souhaité et ne s'arrêtera qu'une fois la totalité de l'arbre
    exploré.
et
    Autre Idée :
    Se baser sur la manière dont on print l'arbre récursivement pour implémenter les règles (semble bieeeeeeeeen plus simple)
     """

    """ Les règles et les faits sont des dictionnaires, rendant leur comparaison plus facile"""
    regles = []

    def aide_generateur_de_regles(arbre: NoeudDeDecision, conditions: dict):
        """ Permet de générer les règles à partir d'un arbre
        """
        if arbre.terminal():
            regle = Regle(conditions, int(arbre.classe()))
            regles.append(regle)
        else:
            for valeur, enfant in arbre.enfants.items():
                copie = dict(conditions)
                copie[arbre.attribut] = int(valeur)
                aide_generateur_de_regles(enfant, copie)

    conditions = {}
    aide_generateur_de_regles(arbre, conditions)

    return regles


def derive_faits_depuis_fichier(fichier):
    """Permet de générer les faits à partir d'un fichier"""
    faits = []
    for donnee in fichier:
        fait = {}
        for k, v in donnee[1].items():
            fait[k] = int(v)
        fait['diagnostic'] = int(donnee[0])
        faits.append(fait)
    return faits


def justification(exemple, regles):
    "Renvoie un string j, la justification de l'exemple par la bonne règle"
    regle_valide = trouve_regle(exemple, regles)
    result = 'Grâce à cette règle : \n'
    result += regle_valide.__repr__()
    result += 'On en déduit : \n('
    for key, value in exemple.items():
        result += ' {} = {},'.format(key, value)
    return '{}) => {}\n'.format(result[:-1], str(regle_valide.conclusion))


def trouve_regle(fait, regles):
    """Permet de trouver la/les règle(s) parmi la liste de règles, qui justifie le fait"""
    for regle in regles:
        is_valid = True
        for key, value in regle.conditions.items():
            if fait[key] != value:
                is_valid = False
        if is_valid:
            return regle
