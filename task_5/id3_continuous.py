from decimal import Decimal
from math import log

from .noeud_de_decision_continuous import NoeudDeDecisionContinuous


class ID3Continuous:
    """ Algorithme ID3, pour les données continues.

    """

    def construit_arbre(self, donnees):
        """ Construit un arbre de décision à partir des données d'apprentissage.

            :param list donnees: les données d'apprentissage\
            ``[classe, {attribut -> valeur}, ...]``.
            :return: une instance de NoeudDeDecision correspondant à la racine de\
            l'arbre de décision.
        """

        # Nous devons extraire les domaines de valeur des
        # attributs, puisqu'ils sont nécessaires pour
        # construire l'arbre.
        attributs = {}
        for donnee in donnees:
            for attribut, valeur in donnee[1].items():
                valeurs = attributs.get(attribut)
                if valeurs is None:
                    valeurs = set()
                    attributs[attribut] = valeurs
                valeurs.add((valeur))

        # Find the predominant class
        classes = set([row[0] for row in donnees])
        # print(classes)
        predominant_class_counter = -1
        for c in classes:
            # print([row[0] for row in donnees].count(c))
            if [row[0] for row in donnees].count(c) >= predominant_class_counter:
                predominant_class_counter = [row[0] for row in donnees].count(c)
                predominant_class = c
        # print(predominant_class)

        arbre = self.construit_arbre_recur(donnees, attributs, predominant_class)

        return arbre

    def construit_arbre_recur(self, donnees, attributs, predominant_class):
        """ Construit rédurcivement un arbre de décision à partir
            des données d'apprentissage et d'un dictionnaire liant
            les attributs à la liste de leurs valeurs possibles.

            :param list donnees: les données d'apprentissage\
            ``[classe, {attribut -> valeur}, ...]``.
            :param attributs: un dictionnaire qui associe chaque\
            attribut A à son domaine de valeurs a_j.
            :return: une instance de NoeudDeDecision correspondant à la racine de\
            l'arbre de décision.
        """

        def classe_unique(donnees):
            """ Vérifie que toutes les données appartiennent à la même classe. """

            if len(donnees) == 0:
                return True
            premiere_classe = donnees[0][0]
            for donnee in donnees:
                if donnee[0] != premiere_classe:
                    return False
            return True

        if donnees == []:
            return NoeudDeDecisionContinuous(None, [str(predominant_class), dict()], str(predominant_class))

        # Si toutes les données restantes font partie de la même classe,
        # on peut retourner un noeud terminal.
        elif classe_unique(donnees):
            return NoeudDeDecisionContinuous(None, donnees, str(predominant_class))


        else:
            # Sélectionne la combinaison attribut/valeur avec l'entropie (h_C_aj) minimale
            entropies = []

            for attribut in attributs:
                for valeur in attributs[attribut]:
                    h_C_aj = self.h_C_aj(donnees, attribut, valeur)
                    entropies = entropies + [[h_C_aj, attribut, valeur]]

            entropie_min = 2
            attribut_separation = None
            valeur_separation = None
            for entropie in entropies:
                # on veut un gain supérieur, mais pour une valeur qui n'est pas la borne inférieure
                # du domaine de valeurs de l'attribut sinon boucle infinie !
                if entropie[0] < entropie_min and entropie[2] != min(attributs[entropie[1]]):
                    entropie_min = entropie[0]
                    attribut_separation = entropie[1]
                    valeur_separation = entropie[2]

            partitions = self.partitionne(donnees, attribut_separation, valeur_separation)

            # Mise à jour des nouveaux attributs pour chaque noeud (meme code que dans
            # construit_arbre mais avec des listes à la place des sets (sinon arbre différent chaque fois)
            attributs_gauche = {}
            for donnee in partitions[0]:
                for attribut, valeur in donnee[1].items():
                    valeurs = attributs_gauche.get(attribut)
                    if valeurs is None:
                        valeurs = []
                        attributs_gauche[attribut] = valeurs
                    valeurs.append((valeur))

            attributs_droite = {}
            for donnee in partitions[1]:
                for attribut, valeur in donnee[1].items():
                    valeurs = attributs_droite.get(attribut)
                    if valeurs is None:
                        valeurs = []
                        attributs_droite[attribut] = valeurs
                    valeurs.append((valeur))

            # creation des 2 enfants
            enfants = {}
            enfants['less than '] = self.construit_arbre_recur(partitions[0],
                                                               attributs_gauche,
                                                               str(predominant_class))
            enfants['more than '] = self.construit_arbre_recur(partitions[1],
                                                               attributs_droite,
                                                               str(predominant_class))

            return NoeudDeDecisionContinuous(attribut_separation, donnees, str(predominant_class), enfants,
                                             valeur_separation)

    def partitionne(self, donnees, attribut, valeur):
        """ Partitionne les données sur les valeurs a_j de l'attribut A.

            :param list donnees: les données à partitioner.
            :param attribut: l'attribut A de partitionnement.
            :param list valeurs: les valeurs a_j de l'attribut A.
            :return: un dictionnaire qui associe à chaque valeur a_j de\
            l'attribut A une liste l_j contenant les données pour lesquelles A\
            vaut a_j.
        """

        gauche = []  # LESS THAN
        droite = []  # GREATER THAN OR EQUAL TO

        for donnee in donnees:
            if Decimal(donnee[1][attribut]) < Decimal(valeur):  # on met dans le noeud de gauche
                gauche.append(donnee)

            else:  # on met dans le noeud de droite
                droite.append(donnee)

        return [gauche, droite]

    def p_aj(self, donnees, attribut, valeur):
        """ p(a_j) - la probabilité que la valeur de l'attribut A soit a_j.

            :param list donnees: les données d'apprentissage.
            :param attribut: l'attribut A.
            :param valeur: la valeur a_j de l'attribut A.
            :return: p(a_j)
        """
        # Nombre de données.
        nombre_donnees = len(donnees)

        # Permet d'éviter les divisions par 0.
        if nombre_donnees == 0:
            return 0.0

        # Nombre d'occurrences de la valeur a_j parmi les données.
        nombre_aj = 0
        for donnee in donnees:
            if donnee[1][attribut] == valeur:
                nombre_aj += 1

        # p(a_j) = nombre d'occurrences de la valeur a_j parmi les données /
        #          nombre de données.
        return nombre_aj / nombre_donnees

    def p_ci_aj(self, donnees, attribut, valeur, classe):
        """ p(c_i|a_j) - la probabilité conditionnelle que la classe C soit c_i\
            étant donné que l'attribut A vaut a_j.

            :param list donnees: les données d'apprentissage.
            :param attribut: l'attribut A.
            :param valeur: la valeur a_j de l'attribut A.
            :param classe: la valeur c_i de la classe C.
            :return: p(c_i | a_j)
        """
        # Nombre d'occurrences de la valeur a_j parmi les données.
        donnees_aj = [donnee for donnee in donnees if donnee[1][attribut] == valeur]
        nombre_aj = len(donnees_aj)

        # Permet d'éviter les divisions par 0.
        if nombre_aj == 0:
            return 0

        # Nombre d'occurrences de la classe c_i parmi les données pour lesquelles
        # A vaut a_j.
        donnees_ci = [donnee for donnee in donnees_aj if donnee[0] == classe]
        nombre_ci = len(donnees_ci)

        # p(c_i|a_j) = nombre d'occurrences de la classe c_i parmi les données
        #              pour lesquelles A vaut a_j /
        #              nombre d'occurrences de la valeur a_j parmi les données.
        return nombre_ci / nombre_aj

    def h_C_aj(self, donnees, attribut, valeur):
        """ H(C|a_j) - l'entropie de la classe parmi les données pour lesquelles\
            l'attribut A vaut a_j.

            :param list donnees: les données d'apprentissage.
            :param attribut: l'attribut A.
            :param valeur: la valeur a_j de l'attribut A.
            :return: H(C|a_j)
        """
        # Les classes attestées dans les exemples.
        classes = list(set([donnee[0] for donnee in donnees]))

        # Calcule p(c_i|a_j) pour chaque classe c_i.
        p_ci_ajs = [self.p_ci_aj(donnees, attribut, valeur, classe)
                    for classe in classes]

        # Si p vaut 0 -> plog(p) vaut 0.
        return -sum([p_ci_aj * log(p_ci_aj, 2.0)
                     for p_ci_aj in p_ci_ajs
                     if p_ci_aj != 0])

    def h_C_A(self, donnees, attribut, valeurs):
        """ H(C|A) - l'entropie de la classe après avoir choisi de partitionner\
            les données suivant les valeurs de l'attribut A.

            :param list donnees: les données d'apprentissage.
            :param attribut: l'attribut A.
            :param list valeurs: les valeurs a_j de l'attribut A.
            :return: H(C|A)
        """
        # Calcule P(a_j) pour chaque valeur a_j de l'attribut A.
        p_ajs = [self.p_aj(donnees, attribut, valeur) for valeur in valeurs]

        # Calcule H_C_aj pour chaque valeur a_j de l'attribut A.
        h_c_ajs = [self.h_C_aj(donnees, attribut, valeur)
                   for valeur in valeurs]

        return sum([p_aj * h_c_aj for p_aj, h_c_aj in zip(p_ajs, h_c_ajs)])
