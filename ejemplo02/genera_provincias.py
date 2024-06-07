from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv
import pymysql
from crear_tablas import Provincia
from config import DATABASE_URI

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

with open('data/datos.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='|')
    provincias = {}
    for row in reader:
        codigo_provincia = row['Código División Política Administrativa Provincia']
        nombre_provincia = row['Provincia']
        if codigo_provincia not in provincias:
            provincia = Provincia(codigo=codigo_provincia, nombre=nombre_provincia)
            session.add(provincia)
            provincias[codigo_provincia] = provincia

session.commit()
