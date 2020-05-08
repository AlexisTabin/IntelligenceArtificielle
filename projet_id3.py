from moteur_id3.noeud_de_decision import NoeudDeDecision
from moteur_id3.id3 import ID3
import csv

#TASK 1

def csv_reader(file):

    """
        :param string file: le fichier cvs que l'on veut lire
        :param list categories: la liste des noms de categorie
        :param list donnees: les données d'apprentissage\
        ``[classe, {attribut -> valeur}, ...]``
    """
    
    categories = []
    donnees = []
    
    with open (file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        line_count = 0
                    #rows_total = sum(1 for row in csv_reader)
                    #print(f'there are {rows_total} lines')
        
        for row in csv_reader:
                
            if line_count == 0: #nom des catégories
                categories = row
                categories[0] = 'age'             
            else:
                #remplissage des colonnes de donnees
                target = []
                target.append(row[-1]) #classe: valeur de 'target'
                target.append({}) #attributs + valeurs
                
                for i in range(0,len(categories)):
                    target[1][categories[i]] = row[i]
                donnees.append(target)
                
            line_count += 1
        return donnees

file_task1 = 'train_bin.csv'
donnees_train = csv_reader(file_task1)


id3 = ID3()
arbre = id3.construit_arbre(donnees_train)
print('Arbre de décision :')
print(arbre)
print()






#TASK 2


##def test_precision(file):
##
##    #recuperation des donnees du test
##    donnees_test = csv_reader(file_task2)
##
##    #construction de l'arbre 
##    id3 = ID3()
##    arbre = id3.construit_arbre(donnees_train)
##
##    predictions_justes = 0
##    predictions_fausses = 0
##
##    #verification de la preciction
##    #for donnee in donnees_test:
##
##        #on enleve target de la donnee:
####        sans_solution = donnee[1]
####        solution = sans_solution["target"]
####        del sans_solution["target"]
####        
####        full_prediction = arbre.classifie(donnee[1])
####        print(full_prediction)
##        
##                
##    print('Exemplification :')
##    #full_prediction =
##    print(arbre.classifie({
##        'age': '3',
##        'sex': '1',
##        'cp': '1',
##        'trestbps': '2',
##        'chol': '1',
##        'fbs': '1',
##        'restecg': '0',
##        'thalach': '3',
##        'exang': '0',
##        'oldpeak': '1',
##        'slope': '2',
##        'ca': '0',
##        'thal': '2'}))
##    
##    
##    
##
##    precision = predictions_justes #/(predictions_justes+predictions_fausses)*100
##    
##    return precision
##
##file_task2 = 'test_public_bin.csv'
##
##precision = test_precision(file_task2)
##
#id3 = ID3()
#arbre = id3.construit_arbre(donnees_train)
#print('Arbre de décision :')
#print(arbre)
#print()



