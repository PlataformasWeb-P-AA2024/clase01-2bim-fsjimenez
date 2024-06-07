from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Establecimiento, Parroquia
from config import DATABASE_URI

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

result = session.query(Parroquia).join(Establecimiento).filter(Establecimiento.jornada.in_(['Matutina', 'Vesperina', 'Nocturna'])).all()
for parroquia in result:
    print(parroquia.nombre)
