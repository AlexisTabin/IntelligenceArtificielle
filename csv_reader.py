import csv

#CREATION DE LA LISTE DE DONNEES
donnees = []
categories = []

with open ('train_bin.csv') as csv_file:
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
            
            for i in range(0,len(categories) - 1):
                target[1][categories[i]] = row[i]
            donnees.append(target)
            
        line_count += 1


