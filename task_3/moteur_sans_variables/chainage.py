
class Chainage:
    """ Le squelette d'un moteur d'inférence.

        Cette classe n'est pas censée être instanciée directement. Elle doit\ 
        être sous-classée par des classes filles qui implémentent la méthode\ 
        ``chaine``.

        :cvar self.trace: représente l'ordre dans lequel les propositions ont\
        été déduites et dans lequel les règles ont été appliquées (à utiliser\
        pour débugger votre code).
        :cvar self.solutions: doit contenir les solutions du chaînage.
    """

    __indentation = 4 * ' '

    def __init__(self, connaissances):
        """ Initialise le moteur d'inférence sans variables.
        
            :param connaissances: la base de connaissances.
        """

        self.trace = []
        self.solutions = []
        self.connaissances = connaissances

    def reinitialise(self):
        """ Réinitialise le moteur. 

            La trace et les solutions sont à nouveau vides après l'appel à\
            cette méthode.
        """

        self.trace = []
        self.solutions = []

    def chaine(self):
        """ Effectue le chaînage. 

            Si des solutions sont trouvées, elles sont placées dans\
            ``self.solutions`` et également retournées.

            :return: les solutions.
        """

        # Nous retournons un ensemble vide dans ce cas.
        return self.solutions

    def affiche_trace(self):
        """ Affiche la trace d'un chaînage après l'appel à ``chaine``.

            :param str indent: l'identation souhaitée au début de chaque ligne\
            (quatre espaces par défaut).
        """

        print('Grâce à cette règle : ')
        print()
        print(self.trace[0])

        self.affiche_solutions()

    def affiche_solutions(self, indent=None):
        """ Affiche les solutions d'un chaînage après l'appel à ``chaine``.

            :param str indent: l'identation souhaitée au début de chaque ligne\
            (quatre espaces par défaut).
        """

        if indent is None:
            indent = Chainage.__indentation

        n = len(self.solutions)
        if n > 0:
            print('On en déduit : ')

            print_sol = '('
            for i in range(n - 2):
                print_sol += '{}, '.format(self.solutions[i])
            print_sol += '{}) => (classe = {})'.format(self.solutions[n-2], self.solutions[n-1])
            print(print_sol)

        else:
            print('Aucun fait trouvé.')