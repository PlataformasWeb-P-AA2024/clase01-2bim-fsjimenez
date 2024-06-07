from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Provincia, Canton, Parroquia, Establecimiento
from config import DATABASE_URI

# Crear el motor y la sesión
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

# Consultas para probar los métodos
provincias = session.query(Provincia).all()
for provincia in provincias:
    print(f'Provincia: {provincia.nombre}, Número de docentes: {provincia.obtener_numero_docentes()}')

cantones = session.query(Canton).all()
for canton in cantones:
    print(f'Cantón: {canton.nombre}, Número de estudiantes: {canton.obtener_numero_estudiantes()}')

parroquias = session.query(Parroquia).all()
for parroquia in parroquias:
    print(f'Parroquia: {parroquia.nombre}, Número de establecimientos: {parroquia.obtener_numero_establecimientos()}, Tipos de jornada: {parroquia.obtener_tipos_jornada()}')


provincias = session.query(Provincia).all()

for provincia in provincias:
    print(f'Provincia: {provincia.nombre}')
    parroquias = provincia.obtener_lista_parroquias()
    print('Parroquias:')
    for parroquia in parroquias:
        print(f'- {parroquia}')
    print()