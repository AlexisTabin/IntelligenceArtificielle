import csv


#CREATION DE LA LISTE DE DONNEES

donnees = []
list_of_names = []

with open ('train_bin.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    line_count = 0
                #rows_total = sum(1 for row in csv_reader)
                #print(f'there are {rows_total} lines')
    
    for row in csv_reader:

        if line_count == 0: #nom des catégories
            list_of_names = row
            list_of_names[0] = 'age'
            
        else:
            #ajout du numero de patient / parcourt des lignes
            #donnees[line_count - 1].append(f'patient nb {line_count}')

            patient = []
            patient.append('patient')
            patient.append({}) #add a dictionary
            #parcourt les colonnes
            for i in range(0,len(list_of_names)):
                patient[1][list_of_names[i]] = row[i]
                  
            donnees.append(patient)
        line_count += 1



