from csv_reader import donnees
from csv_reader import categories
from moteur_id3.noeud_de_decision import NoeudDeDecision
from moteur_id3.id3 import ID3

print(donnees)
id3 = ID3()
arbre = id3.construit_arbre(donnees)
print('Arbre de décision :')
print(arbre)
print()

print('Exemplification :')

