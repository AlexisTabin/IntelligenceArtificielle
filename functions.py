from moteur_id3.noeud_de_decision import NoeudDeDecision
from moteur_id3.id3 import ID3
import csv


def csv_reader(file):
    """
        :param string file: le fichier cvs que l'on veut lire
        :param list categories: la liste des noms de categorie
        :param list donnees: les données d'apprentissage\
        ``[classe, {attribut -> valeur}, ...]``
    """

    categories = []
    donnees = []

    with open(file) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        # rows_total = sum(1 for row in csv_reader)
        # print(f'there are {rows_total} lines')

        for row in reader:

            if line_count == 0:  # nom des catégories
                categories = row
                categories[0] = 'age'
            else:
                # remplissage des colonnes de donnees
                target = [row[-1], {}]

                for i in range(len(categories) - 1):
                    target[1][categories[i]] = row[i]
                donnees.append(target)

            line_count += 1
        return donnees


def test_precision(file, arbre):
    # recuperation des donnees du test
    donnees_test = csv_reader(file)

    diagnostic_juste = 0
    nb_diagnostics = len(donnees_test)
    if nb_diagnostics == 0:
        return 0

    # verification du diagnostic p/r à l'arbre déjà établi
    for donnee in donnees_test:

        symptomes = donnee[1]
        solution = donnee[0]

        diagnostic = arbre.classifie(symptomes)

        # prediction correcte:
        if diagnostic[-1] == solution:
            diagnostic_juste += 1

    return diagnostic_juste / nb_diagnostics * 100
