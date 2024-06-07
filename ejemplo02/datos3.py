from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Establecimiento, Parroquia, Canton
from config import DATABASE_URI

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

result = session.query(Establecimiento).join(Parroquia).join(Canton).filter(Canton.nombre == 'GUAYAQUIL').all()
for establecimiento in result:
    print(establecimiento.nombre)
