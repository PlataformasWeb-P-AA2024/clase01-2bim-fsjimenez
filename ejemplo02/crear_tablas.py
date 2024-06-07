from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Provincia(Base):
    __tablename__ = 'provincia'

    id = Column(Integer, primary_key=True)
    codigo = Column(String(50))
    nombre = Column(String(250))
    cantones = relationship("Canton", back_populates="provincia")

    def obtener_numero_docentes(self):
        return sum(canton.obtener_numero_estudiantes() for canton in self.cantones)
    
    def obtener_lista_parroquias(self):
        cadena = ""
        for c in self.cantones:
            for p in c.parroquias:
                cadena = "%s%s\n" % (cadena, p.nombre)
        return cadena

class Canton(Base):
    __tablename__ = 'canton'

    id = Column(Integer, primary_key=True)
    codigo = Column(String(50))
    nombre = Column(String(250))
    provincia_id = Column(Integer, ForeignKey('provincia.id'))
    provincia = relationship("Provincia", back_populates="cantones")
    parroquias = relationship("Parroquia", back_populates="canton")

    def obtener_numero_estudiantes(self):
        return sum(parroquia.obtener_numero_establecimientos() for parroquia in self.parroquias)

class Parroquia(Base):
    __tablename__ = 'parroquia'

    id = Column(Integer, primary_key=True)
    codigo = Column(String(50))
    nombre = Column(String(250))
    canton_id = Column(Integer, ForeignKey('canton.id'))
    canton = relationship("Canton", back_populates="parroquias")
    establecimientos = relationship("Establecimiento", back_populates="parroquia")

    def obtener_numero_establecimientos(self):
        return len(self.establecimientos)

    def obtener_tipos_jornada(self):
        return set(establecimiento.jornada for establecimiento in self.establecimientos)

class Establecimiento(Base):
    __tablename__ = 'establecimiento'

    id = Column(Integer, primary_key=True)
    codigo_amie = Column(String(50))
    nombre = Column(String(250))
    parroquia_id = Column(Integer, ForeignKey('parroquia.id'))
    parroquia = relationship("Parroquia", back_populates="establecimientos")
    numero_profesores = Column(Integer)
    codigo_distrito = Column(String(50))
    numero_estudiantes = Column(Integer)
    jornada = Column(String(50))
    sostenimiento = Column(String(50))
    tipo_educacion = Column(String(50))
    regimen_escolar = Column(String(50))


# Conexión a la base de datos
engine = create_engine("mysql+pymysql://root:Felipe_94!@localhost/final1bimnuevo")

# Crear todas las tablas
Base.metadata.create_all(engine)
