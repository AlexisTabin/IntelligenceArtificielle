from sys import argv
from typing import List

from moteur_id3.noeud_de_decision import NoeudDeDecision
from task_3.moteur_sans_variables.chainage_avant_sans_variables import ChainageAvantSansVariables
from task_3.moteur_sans_variables.connaissance import BaseConnaissances
from task_3.moteur_sans_variables.regle_sans_variables import RegleSansVariables as Regle


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

    def rule_generation_helper(arbre: NoeudDeDecision, conditions: List[str]):
        """ Représentation sous forme de string de l'arbre de décision duquel\
            le noeud courant est la racine.
        """
        if arbre.terminal():
            regle = Regle(conditions, arbre.classe())
            regles.append(regle)
        else:
            for valeur, enfant in arbre.enfants.items():
                conditions.append(create_condition_from_nb(arbre.attribut, valeur.upper()))
                rule_generation_helper(enfant, list(conditions))

    conditions = []
    rule_generation_helper(arbre, conditions)

    return regles


def derive_faits_from_file(file):
    faits = []
    for don in file:
        fait = []
        for k, v in don[1].items():
            fait.append(create_condition_from_nb(k, v))
        faits.append(fait)
    return faits


def create_condition_from_nb(a, b):
    return '{} = {}'.format(a, b)


def justification(exemple, regles):
    bc = BaseConnaissances()
    bc.ajoute_faits(exemple)
    bc.ajoute_regles(regles)

    moteur = ChainageAvantSansVariables(bc)
    moteur.chaine()

   # if len(argv) > 1 and argv[1].lower() == 'trace':
        # Utile durant le déboggage.
    moteur.affiche_trace()
