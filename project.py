import random
from typing import List

from moteur_id3.id3 import ID3
from task_1.csc_reader import csv_reader
from task_2.test_precision import test_precision
from task_3.rule_generation import generateur_de_regles, derive_faits_depuis_fichier, justification
from task_4.abduction import abuction


class ResultValues:

    def __init__(self):
        # Do computations here

        # Task 1
        file_task1 = 'data/train_bin.csv'
        donnees_train = csv_reader(file_task1)
        id3 = ID3()
        self.arbre = id3.construit_arbre(donnees_train)

        # Task 2
        file_task2 = 'data/test_public_bin.csv'
        self.precision = test_precision(file_task2, self.arbre)

        # Task 3
        self.regles = generateur_de_regles(self.arbre)
        self.faits_initiaux = derive_faits_depuis_fichier(donnees_train)

        # Task 4

        # Task 5
        self.arbre_advance = None

        #self.print_tasks()
        self.print_task_3()

    def get_results(self):
        return [self.arbre, self.faits_initiaux, self.regles, self.arbre_advance]

    def print_task_1(self):
        print('-----TASK 1-----')
        print('Arbre de décision:')
        print(self.arbre)

    def print_task_2(self):
        print('-----TASK 2-----')
        print()
        print('Precision des diagnostics:')
        print(self.precision)
        print()

    def print_task_3(self):
        # Task 3
        print('-----TASK 3-----')
        print()
        rdm_patient_index = random.randint(0, len(self.faits_initiaux) - 1)
        rdm_patient = self.faits_initiaux[rdm_patient_index]
        print(justification(rdm_patient, self.regles))
        print()

    def print_task_4(self):
        # Task 4
        print('-----TASK 4-----')
        print()
        random_patient: List[str] = random.choice(self.faits_initiaux)
        abuction(random_patient, self.regles)

    def print_tasks(self):
        self.print_task_1()
        self.print_task_2()
        self.print_task_3()
        self.print_task_4()


result = ResultValues()
