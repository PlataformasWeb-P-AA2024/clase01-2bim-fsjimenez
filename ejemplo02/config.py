DATABASE_URI = 'mysql+pymysql://root:Felipe_94!@localhost/final1bimnuevo'



# genera_establecimiento.py (y otros scripts similares)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv
import pymysql
from crear_tablas import Establecimiento, Parroquia
from config import DATABASE_URI

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

# Resto del código...
