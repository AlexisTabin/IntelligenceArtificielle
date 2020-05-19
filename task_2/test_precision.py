from task_1.csc_reader import csv_reader


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
