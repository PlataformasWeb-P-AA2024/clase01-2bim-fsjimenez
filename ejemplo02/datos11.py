from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Establecimiento
from config import DATABASE_URI

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

result = session.query(Establecimiento).filter(Establecimiento.codigo_distrito == '09D12').order_by(Establecimiento.sostenimiento).all()
for establecimiento in result:
    print(establecimiento.nombre)
