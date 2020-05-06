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
            categories[0] = 'age' #premiere categorie ne marchait pas tres bien
            
        else:
            #remplissage des colonnes de donnees
            patient = []
            patient.append('patient'+str(line_count - 1))
            patient.append({})
            
            for i in range(0,len(categories)):
                patient[1][categories[i]] = row[i]
            donnees.append(patient)
            
        line_count += 1






