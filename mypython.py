import csv

# open file for reading
with open('shortdata.csv') as csvDataFile:

    # read file as csv file 
    csvReader = csv.reader(csvDataFile)

    # for every row, print the row
    for row in csvReader:
        print(row)







firstname = 'yasmin'
Lastname = 'Aden'
subject = 'Politics'
print('hello '+firstname + ' ' + Lastname  +' Welcome to SOAS I am studying ' + subject)
