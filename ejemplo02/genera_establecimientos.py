from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv
import pymysql
from crear_tablas import Establecimiento, Parroquia
from config import DATABASE_URI

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

with open('data/datos.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='|')
    for row in reader:
        codigo_parroquia = row['Código División Política Administrativa  Parroquia']
        parroquia = session.query(Parroquia).filter_by(codigo=codigo_parroquia).first()
        if parroquia:
            establecimiento = Establecimiento(
                codigo_amie=row['Código AMIE'],
                nombre=row['Nombre de la Institución Educativa'],
                parroquia=parroquia,
                numero_profesores=row['Número de docentes'],
                codigo_distrito=row['Código de Distrito'],
                jornada=row['Jornada'],
                sostenimiento=row['Sostenimiento'],
                tipo_educacion=row['Tipo de Educación'],
                regimen_escolar=row['Régimen Escolar']
            )
            session.add(establecimiento)

session.commit()
