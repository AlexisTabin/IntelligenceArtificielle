from moteur_id3.noeud_de_decision import NoeudDeDecision
from task_3.regle_avec_variables import RegleAvecVariables as Regle


def rule_generation(arbre):
    """ Idée pour générer toutes les règles de l'arbre de décision :
    A partir de l'arbre final, il faut parcourir chaque branche une fois, jusqu'à la feuille
    L'idée est d'appeler le depth first search algorithm avec comme but un noeud qui n'est pas dans l'arbre.
    De cette manière, l'algorithme va avoir le comportement souhaité et ne s'arrêtera qu'une fois la totalité de l'arbre
    exploré.

    Autre Idée :
    Se baser sur la manière dont on print l'arbre récursivement pour implémenter les règles (semble bieeeeeeeeen plus simple)
     """

    """ Pour le moment, les conditions et la conclusion de chaque règle sont juste des strings, on pourrait en faire de
    vraies règles """
    regles = []

    def rule_generation_helper(arbre: NoeudDeDecision, regle: Regle):
        """ Représentation sous forme de string de l'arbre de décision duquel\
            le noeud courant est la racine.
        """
        if arbre.terminal():
            regle.conclusion = 'Alors {}'.format(arbre.classe().upper())
            regles.append(regle)
        else:
            for valeur, enfant in arbre.enfants.items():
                regle.conditions += 'Si {} = {}: '.format(arbre.attribut, valeur.upper())
                rule_generation_helper(enfant, regle)

    regle = Regle('', '')
    rule_generation_helper(arbre, regle)

    return regles
