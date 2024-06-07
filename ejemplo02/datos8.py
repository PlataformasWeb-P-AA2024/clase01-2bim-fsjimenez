from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Establecimiento, Provincia, Parroquia, Canton
from config import DATABASE_URI

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()


result = session.query(Establecimiento).filter(Establecimiento.nombre.like('%UNIDOS%')).all()


for establecimiento, provincia in result:
    print(f'Establecimiento: {establecimiento.nombre}, Provincia: {establecimiento.parroquia.canton.provincia.nombre}')
