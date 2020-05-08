from csv_reader import donnees
#from donnees_mini import donnees_mini
from csv_reader import categories
from moteur_id3.noeud_de_decision import NoeudDeDecision
from moteur_id3.id3 import ID3


id3 = ID3()
arbre = id3.construit_arbre(donnees)
print('Arbre de décision :')
print(arbre)
print()

print('Exemplification :')
print(arbre.classifie({
        'age': '3',
        'sex': '1',
        'cp': '1',
        'trestbps': '2',
        'chol': '1',
        'fbs': '1',
        'restecg': '0',
        'thalach': '3',
        'exang': '0',
        'oldpeak': '1',
        'slope': '2',
        'ca': '0',
        'thal': '2'}))
