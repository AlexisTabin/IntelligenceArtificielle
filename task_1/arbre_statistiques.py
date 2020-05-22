from moteur_id3 import noeud_de_decision as NoeudDeDecision
from statistics import mean

class Statistiques:

    def arbre_statistiques(self, arbre: NoeudDeDecision):
        """Autre Idée :
        Se baser sur la manière dont on print l'arbre récursivement pour implémenter les règles (semble bieeeeeeeeen plus simple)
         """

        """ Les règles et les faits sont des dictionnaires, rendant leur comparaison plus facile"""
        self.feuille = 0
        self.level = 0

        def compteur_de_feuille(arbre: NoeudDeDecision):
            """ Permet de générer les règles à partir d'un arbre
            """
            if arbre.terminal():
                self.feuille += 1
            else:
                for valeur, enfant in arbre.enfants.items():
                    compteur_de_feuille(enfant)

        compteur_de_feuille(arbre)
        print("Nb de feuillles : {}".format(self.feuille))
        self.longueurs = []

        def maximum_longueur_branche(arbre: NoeudDeDecision, level=0):
            if arbre.terminal():
                self.longueurs.append(level)
            else:
                for valeur, enfant in arbre.enfants.items():
                    maximum_longueur_branche(enfant, level + 1)

        maximum_longueur_branche(arbre)
        print("Max : {}".format(max(self.longueurs)))
        print("Avg : {}".format(round(mean(self.longueurs), 2)))

        self.enfants = []

        def nombre_enfants(arbre: NoeudDeDecision):
            if not arbre.terminal():
                self.enfants.append(len(arbre.enfants))
                for valeur, enfant in arbre.enfants.items():
                    nombre_enfants(enfant)

        nombre_enfants(arbre)
        print("Nb d'enfants : {}".format(sum(self.enfants)))