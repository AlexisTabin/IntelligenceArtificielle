class RegleSansVariables:
    """ Représentation d'une règle d'inférence pour le chaînage sans\
        variables. 
    """

    def __init__(self, conditions, conclusion):
        """ Construit une règle étant donné un dictionnaire de conditions et une\
            conclusion.
            
            :param dict conditions: une collection de propositions (sans\
            variables) nécessaires pour déclencher la règle.
            :param conclusion: la proposition (sans variables) résultant du\
            déclenchement de la règle.
        """

        self.conditions = conditions
        self.conclusion = conclusion

    def __repr__(self):
        """ Représentation d'une règle sous forme de string. """
        result = ''
        for key, value in self.conditions.items():
            result += ' {} = {},'.format(key, value)
        return '({}) => {}\n'.format(result[:-1],
                                     str(self.conclusion))
