### 5)	(30	points):	
La	discrétisation	des	valeurs	d'attribut	à	l'avance	peut	entraîner	une	perte	de	
performances	de	votre	arbre	de	décision.	Au	lieu	de	cela,	vous	pouvez	essayer	une	
division	plus	sophistiquée	des	valeurs	d'attribut,	basée	sur	les	notions	de	
minimisation	d'entropie	(ou	de	maximisation	du	gain	d'informations)	présentées	dans	
la	classe	du	27	Avril.
Pour	ce	faire,	vous	devez	modifier	l'algorithme	ID3	à	partir	des	exercices	du	27	Avril	
(id3.py	et	noeud_de_decision.py).
	
 L'algorithme	doit	prendre	en	entrée	un	ensemble	de	
données	avec	des	valeurs	d'attribut	continues:
http://lia.epfl.ch/CS330_project_2020/train_continuous.csv
À	chaque	itération	de	l'algorithme,	un	nœud	est	divisé	en	nœuds	enfants	en	fonction	
non	seulement	de	l'attribut,	mais	de	la	combinaison	de	(attribut,	valeur	d'attribut)	qui	
minimise	l'entropie	(ou,	de	manière	équivalente,	maximise	le	gain	d'informations).	

Par	exemple,	l'algorithme	peut	diviser	un	nœud	en	fonction	de	l'attribut	"âge"	et	de	la	
valeur	"37"	de	telle	sorte	que	tous	les	participants	de	moins	de	37	ans	iraient	sur	
l'enfant	de	gauche,	tandis	que	les	plus	âgés	sur	l’enfant	de	droite.	

Ne	considérez	que	
les	arbres	de	classification	binaires,	c'est-à-dire	que	chaque	nœud	non	feuille	doit	
avoir	deux	enfants.	L'algorithme	continue	sa	récursion	sur	chaque	sous-ensemble,	
mais	en	considérant	TOUS	les	attributs	(c.-à-d.,	dans	une	itération	ultérieure,	
l'algorithme	peut	choisir	de	se	diviser	à	nouveau	en	fonction	de	l'attribut	"âge",	mais	
cette	fois	sur	la	valeur	20	de	sorte	que	tous	les	participants	qui	sont	plus	jeunes	de	20	
ans	iraient	sur	l'enfant	de	gauche,	tandis	que	ceux	qui	ont	entre	20	et	36	ans	iraient	
sur	l'enfant	de	droite).
	
Utiliser	le	jeu	de	données	de	test	suivant : http://lia.epfl.ch/CD330_project_2020/test_public_continuous.csv

Évaluez	la	précision	des	prédictions	obtenues	grâce	à	l'arbre	de	décision.	Votre	
précision	s'est-elle	améliorée	par	rapport	à	l'arbre	de	décision	de	la	question	(1)?