from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Establecimiento, Parroquia
from config import DATABASE_URI

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

# Verificación de datos en la Parroquia
parroquias = session.query(Parroquia).filter(Parroquia.codigo.in_(['20151', '20153'])).all()
print(f'Parroquias encontradas: {len(parroquias)}')
for parroquia in parroquias:
    print(f'Parroquia: {parroquia.codigo} - {parroquia.nombre}')

# Consulta de Establecimientos en las parroquias especificadas
result = session.query(Establecimiento).join(Parroquia).filter(Parroquia.codigo.in_(['20151', '20153'])).all()
print(f'Establecimientos encontrados: {len(result)}')
for establecimiento in result:
    print(f'Establecimiento: {establecimiento.nombre}')
