class RegleSansVariables:
    """ Représentation d'une règle d'inférence pour le chaînage sans\
        variables. 
    """

    def __init__(self, conditions, conclusion):
        """ Construit une règle étant donné une liste de conditions et une\
            conclusion.
            
            :param list conditions: une collection de propositions (sans\
            variables) nécessaires pour déclencher la règle.
            :param conclusion: la proposition (sans variables) résultant du\
            déclenchement de la règle.
        """

        self.conditions = conditions
        self.conclusion = conclusion

    def depend_de(self, fait):
        """ Vérifie si un fait est pertinent pour déclencher la règle.
            
            :param fait: un fait qui doit faire partie des conditions de\
            déclenchement.
            :return: ``True`` si le fait passé en paramètre fait partie des\
            conditions de déclenchement.
        """
        return fait in self.conditions

    def satisfaite_par(self, faits):
        """ Vérifie si un ensemble de faits est suffisant pour prouver la\
            conclusion.
            
            :param list faits: une liste de faits.
            :return: ``True`` si les faits passés en paramètres suffisent à\
            déclencher la règle.
        """

        """ J'ai inversé la valeur de retour (self.conditions.issubset(faits) 
        par ce qu'il y a ci-dessous, parce que dans nos règles issues de notre arbre,
        il se peut qu'il y ait des conditions qui ne puissent être satisfaites en même temps
        (comme age = 2 et age = 3) 
        """
        return set(faits).issubset(self.conditions)

    def __repr__(self):
        """ Représentation d'une règle sous forme de string. """
        result = ''
        for key, value in self.conditions.items():
            result += ' {} = {},'.format(key, value)
        return '({}) => {}\n'.format(result[:-1],
                                     str(self.conclusion))
