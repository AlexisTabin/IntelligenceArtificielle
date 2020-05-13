from functions import csv_reader
from functions import test_precision
from moteur_id3.id3 import ID3
from task_3.rule_generation import rule_generation


class ResultValues:

    def __init__(self):
        # Do computations here

        # Task 1
        # self.arbre = None
        file_task1 = 'train_bin.csv'
        donnees_train = csv_reader(file_task1)

        id3 = ID3()
        arbre = id3.construit_arbre(donnees_train)
        print('-----TASK 1-----')
        print('Arbre de décision:')
        print(arbre)
        print()

        regles = rule_generation(arbre)
        print(regles)
        # Task 2
        file_task2 = 'test_public_bin.csv'
        precision = test_precision(file_task2, arbre)

        print('-----TASK 2-----')
        print('Precision des diagnostics:')
        print(precision)

        # Task 3
        self.faits_initiaux = None
        self.regles = None
        # Task 5
        self.arbre_advance = None

    def get_results(self):
        return [self.arbre, self.faits_initiaux, self.regles, self.arbre_advance]


result = ResultValues()
