import csv

# Verificar los encabezados del archivo CSV
with open('data/datos.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    headers = reader.fieldnames
    print("Encabezados del CSV:", headers)
