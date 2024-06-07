from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv
import pymysql
from crear_tablas import Canton, Provincia
from config import DATABASE_URI

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

with open('data/datos.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='|')
    cantones = {}
    for row in reader:
        codigo_provincia = row['Código División Política Administrativa Provincia']
        provincia = session.query(Provincia).filter_by(codigo=codigo_provincia).first()
        if provincia:
            codigo_canton = row['Código División Política Administrativa  Cantón']
            nombre_canton = row['Cantón']
            if codigo_canton not in cantones:
                canton = Canton(codigo=codigo_canton, nombre=nombre_canton, provincia=provincia)
                session.add(canton)
                cantones[codigo_canton] = canton

session.commit()
