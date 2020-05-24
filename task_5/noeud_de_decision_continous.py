from decimal import Decimal

class NoeudDeDecision_continous:
    """ Un noeud dans un arbre de décision avancé, qui aura toujours 2 enfants.
    """

    def __init__(self, attribut, donnees, p_class, enfants=None, valeur_separation = None):
        """
            :param attribut: l'attribut de partitionnement du noeud (``None`` si\
            le noeud est un noeud terminal).
            :param list donnees: la liste des données qui tombent dans la\
            sous-classification du noeud.
            :param enfants: un dictionnaire associant un fils (sous-noeud) à\
            chaque valeur (less than/more than) de l'attribut du noeud (``None`` si le\
            noeud est terminal).
            :param valeur_separation: la valeur qui a engendré les 2 sous-noeuds
        """

        self.attribut = attribut
        self.donnees = donnees
        self.enfants = enfants
        self.p_class = p_class
        self.valeur_separation = valeur_separation

    def terminal(self):
        """ Vérifie si le noeud courant est terminal. """

        return self.enfants is None

    def classe(self):
        """ Si le noeud est terminal, retourne la classe des données qui\
            tombent dans la sous-classification (dans ce cas, toutes les\
            données font partie de la même classe.
        """

        if self.terminal():
            return self.donnees[0][0]

    def classifie(self, donnee):
        """ Classifie une donnée à l'aide de l'arbre de décision duquel le noeud\
            courant est la racine.

            :param donnee: la donnée à classifier.
            :return: la classe de la donnée selon le noeud de décision courant.
        """

        rep = ''
        if self.terminal():
            rep += 'Alors {}'.format(self.classe().upper())

        else:
            enfant_less = self.enfants['less than ']
            enfant_more = self.enfants['more than ']

            # on met cette donnee à gauche si la valeur de l'attribut est < que valeur_separation:
            if (donnee[self.attribut]) < self.valeur_separation:
                rep += 'Si {} < {}, '.format(self.attribut, self.valeur_separation)

                try:
                    rep += enfant_less.classifie(donnee)
                except:
                    rep += self.p_class

            # sinon on met dans le noeud de droite (valeur >= que valeur_separation)
            else:
                rep += 'Si {} >= {}, '.format(self.attribut, self.valeur_separation)

                try:
                    rep += enfant_more.classifie(donnee)
                except:
                    rep += self.p_class

        return rep

    def repr_arbre(self, level=0):
        """ Représentation sous forme de string de l'arbre de décision duquel\
            le noeud courant est la racine.
        """

        rep = ''
        if self.terminal():
            rep += '---' * level
            rep += 'Alors {}\n'.format(self.classe().upper())
            rep += '---' * level
            rep += 'Décision basée sur les données:\n'
            for donnee in self.donnees:
                rep += '---' * level
                rep += str(donnee) + '\n'

        else:
            enfant_less = self.enfants['less than ']
            enfant_more = self.enfants['more than ']

            # gauche, <:
            rep += '---' * level
            rep += 'Si {} < {} : \n'.format(self.attribut, self.valeur_separation)
            rep += enfant_less.repr_arbre(level + 1)

            # droite, >=:
            rep += '---' * level
            rep += 'Si {} >= {} : \n'.format(self.attribut, self.valeur_separation)
            rep += enfant_more.repr_arbre(level + 1)

        return rep

    def __repr__(self):
        """ Représentation sous forme de string de l'arbre de décision duquel\
            le noeud courant est la racine. 
        """

        return str(self.repr_arbre(level=0))