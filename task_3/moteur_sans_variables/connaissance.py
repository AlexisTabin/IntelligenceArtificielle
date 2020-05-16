
class BaseConnaissances:
    """ Une base de connaissances destinée à contenir les faits et les\ 
        règles d'un système de chaînage avant.
    """

    def __init__(self):
        """ Construit une base de connaissances. """

        self.faits = []
        self.regles = []


    def ajoute_un_fait(self, fait):
        """ Ajoute un fait dans la base de connaissances. 

            :param fait: un fait.
        """

        self.faits.append(fait)

    def ajoute_faits(self, faits):
        """ Ajoute une liste de faits dans la base de connaissances.

            :param list faits: une liste de faits.
        """
        
        self.faits.extend(faits)
            
    def ajoute_une_regle(self, regle):
        """ Ajoute une règle dans la base de connaissances.

            Une règle est décrite par une liste (ou un tuple) de deux\
            éléments : un dictionnaire de conditions et une conclusion.

            Les conditions et la conclusion doivent être des propositions.

            :param regle: une règle.
        """
        self.regles.append(regle)

    def ajoute_regles(self, regles):
        """ Ajoute des règles dans la base de connaissances.

            L'argument est une liste de règles, chacune composée d'une\
            liste de conditions et d'une conséquence.

            :param list regles: une liste de descriptions de règles.
        """

        for regle in regles:
            self.ajoute_une_regle(regle)