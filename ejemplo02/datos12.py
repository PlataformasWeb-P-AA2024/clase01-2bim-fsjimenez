from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Establecimiento
from config import DATABASE_URI

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

result = session.query(Establecimiento).filter(Establecimiento.numero_profesores > 100, Establecimiento.regimen_escolar == 'SIERRA').order_by(Establecimiento.numero_estudiantes).all()
for establecimiento in result:
    print(establecimiento.nombre)
