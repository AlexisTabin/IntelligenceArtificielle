import random

from moteur_id3.id3 import ID3
from task_1.arbre_statistiques import Statistiques
from task_1.csc_reader import csv_reader
from task_2.test_precision import test_precision
from task_3.rule_generation import generateur_de_regles, derive_faits_depuis_fichier, justification
from task_4.abduction import nb_patients_sauvables, diagnostic_et_prescription
from task_5.id3_continous import ID3_continous



class ResultValues:

    def __init__(self):
        # Do computations here

        # Task 1
        self.file_task1 = 'data/train_bin.csv'
        donnees_train = csv_reader(self.file_task1)
        self.id3 = ID3()
        self.arbre = self.id3.construit_arbre(donnees_train)


        # Task 2
        self.file_task2 = 'data/test_public_bin.csv'
        self.precision = test_precision(self.file_task2, self.arbre)

        # Task 3
        self.regles = generateur_de_regles(self.arbre)
        self.faits_initiaux = derive_faits_depuis_fichier(donnees_train)

        # Task 4


        #Task 5
        """
        self.file_continous_train = 'data/train_continuous.csv'
        donnees_continous = csv_reader(self.file_continous_train)
        self.file_continous_test = 'data/test_public_continuous.csv'
        self.id3_continous = ID3_continous()
        self.arbre_continous = self.id3_continous.construit_arbre(donnees_continous)
        self.precision_continous = test_precision(self.file_continous_test, self.arbre_continous)
        """



        self.arbre_advance = None

        self.print_task_1()

    def get_results(self):
        return [self.arbre, self.faits_initiaux, self.regles, self.arbre_advance]

    def print_task_1(self):
        print('-----TASK 1-----')
        print('Arbre de décision:')
        print(self.arbre)
        print('-----Statistiques-------')
        Statistiques.arbre_statistiques(self, self.arbre)

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
        if rdm_patient['diagnostic'] == 1:
           diagnostic, presription, _ = diagnostic_et_prescription(rdm_patient, self.regles)
           print(presription)

    def print_task_4(self):
        """!!! On doit utiliser les patients des données test cette fois"""
        # Task 4
        print('-----TASK 4-----')
        donnees_test = csv_reader(self.file_task2)
        faits_test = derive_faits_depuis_fichier(donnees_test)
        print()
        total, fichus, sauvables, saufs = nb_patients_sauvables(faits_test, self.regles)
        print("Sur un nombre total de {} patients,".format(total))
        print("le nb de personnes pouvant être guerries en changeant 1 ou 2 attribut est : {}".format(sauvables))
        print("il y a {} personnes qui ne sont pas malades ".format(saufs))
        print("et {}heureusement {} personnes fichues".format("mal" if (fichus != 0) else '', fichus))

    def print_task_5(self):
        print('-----TASK 5------')
        print(self.arbre_continous)
        print()
        print('Précision: '), print(self.precision_continous)


    def print_tasks(self):
        #self.print_task_1()
        #self.print_task_2()
        #self.print_task_3()
        #self.print_task_4()
        self.print_task_5()


result = ResultValues()
