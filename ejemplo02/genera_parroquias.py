from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv
import pymysql
from crear_tablas import Parroquia, Canton
from config import DATABASE_URI

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

with open('data/datos.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='|')
    parroquias = {}
    for row in reader:
        codigo_canton = row['Código División Política Administrativa  Cantón']
        canton = session.query(Canton).filter_by(codigo=codigo_canton).first()
        if canton:
            codigo_parroquia = row['Código División Política Administrativa  Parroquia']
            nombre_parroquia = row['Parroquia']
            if codigo_parroquia not in parroquias:
                parroquia = Parroquia(codigo=codigo_parroquia, nombre=nombre_parroquia, canton=canton)
                session.add(parroquia)
                parroquias[codigo_parroquia] = parroquia

session.commit()
