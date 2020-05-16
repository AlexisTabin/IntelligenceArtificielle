from moteur_id3.id3 import ID3
from task_1.csc_reader import csv_reader
from task_2.test_precision import test_precision
from task_3.rule_generation import rule_generation, derive_faits_from_file, justification
import random


class ResultValues:

    def __init__(self):
        # Do computations here

        # Task 1
        file_task1 = 'data/train_bin.csv'
        donnees_train = csv_reader(file_task1)

        id3 = ID3()
        self.arbre = id3.construit_arbre(donnees_train)
        print('-----TASK 1-----')
        print('Arbre de décision:')
        print(self.arbre)

        # Task 2
        file_task2 = 'data/test_public_bin.csv'
        precision = test_precision(file_task2, self.arbre)

        print('-----TASK 2-----')
        print()
        print('Precision des diagnostics:')
        print(precision)
        print()

        # Task 3
        print('-----TASK 3-----')
        print()
        self.regles = rule_generation(self.arbre)
        self.faits_initiaux = derive_faits_from_file(donnees_train)
        justification(random.choice(self.faits_initiaux), self.regles)
        print()

        # Task 5
        self.arbre_advance = None

    def get_results(self):
        return [self.arbre, self.faits_initiaux, self.regles, self.arbre_advance]


result = ResultValues()
