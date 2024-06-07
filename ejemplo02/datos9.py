from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Establecimiento, Parroquia
from config import DATABASE_URI

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

result = session.query(Establecimiento).join(Parroquia).filter(Establecimiento.numero_profesores > 40, Establecimiento.tipo_educacion.like('%Educación regular%')).order_by(Parroquia.nombre).all()
for establecimiento in result:
    print(establecimiento.nombre)
