from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Establecimiento, Parroquia, Canton
from config import DATABASE_URI

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

result = session.query(Canton).join(Parroquia).join(Establecimiento).filter(Establecimiento.numero_profesores == 0, Establecimiento.numero_estudiantes == 210).all()
for canton in result:
    print(canton.nombre)
