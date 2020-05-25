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
