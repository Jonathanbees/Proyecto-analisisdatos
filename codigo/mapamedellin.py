import pandas as pd
import numpy
import csv

with open('calles_de_medellin_con_acoso.csv') as csvfile:
    '''
    reader = csv.reader(csvfile, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        print(row)
    '''
    archivo = pd.read_csv(csvfile, delimiter=";")
    print(archivo)
