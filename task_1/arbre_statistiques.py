from statistics import mean

from moteur_id3 import noeud_de_decision as noeud_de_decision


class Statistiques:

    def __init__(self, arbre : noeud_de_decision):
        self.feuille = 0
        self.level = 0
        self.longueurs = []
        self.enfants = []
        self.arbre = arbre

    def arbre_statistiques(self):
        def compteur_de_feuille(arbre: noeud_de_decision):
            if arbre.terminal():
                self.feuille += 1
            else:
                for valeur, enfant in arbre.enfants.items():
                    compteur_de_feuille(enfant)

        compteur_de_feuille(self.arbre)
        print("Nb de feuillles : {}".format(self.feuille))

        def maximum_longueur_branche(arbre: noeud_de_decision, level=0):
            if arbre.terminal():
                self.longueurs.append(level)
            else:
                for valeur, enfant in arbre.enfants.items():
                    maximum_longueur_branche(enfant, level + 1)

        maximum_longueur_branche(self.arbre)
        print("Max : {}".format(max(self.longueurs)))
        print("Avg : {}".format(round(mean(self.longueurs), 2)))

        def nombre_enfants(arbre: noeud_de_decision):
            if not arbre.terminal():
                self.enfants.append(len(arbre.enfants))
                for valeur, enfant in arbre.enfants.items():
                    nombre_enfants(enfant)

        nombre_enfants(self.arbre)
        print("Nb d'enfants : {}".format(sum(self.enfants)))
