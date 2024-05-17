from sqlalchemy import create_engine

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite

from configuracion import engine
# engine es la conexion a la base de datos

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String
# es la superclase que esta heredando de otra
#la clase saludo cuando haga el proceso va a recoger todas las clases pero en la base de datos se llamen saludo y
#el atributo debe tener una estructura __tablemname__ y luego se creen las otras variables
# el tipo de taributo y dato se extrae del sqlalchemy
class Saludo(Base):
    __tablename__ = 'saludos' 

    id = Column(Integer, primary_key=True)
    mensaje = Column(String(200))
    tipo = Column(String(200))


"""
class Saludo2(Base):
    __tablename__ = 'saludo2'
    id = Column(Integer, primary_key=True)
    mensaje = Column(String(200))
    tipo = Column(String(200))
    origen = Column(String(200))
"""

Base.metadata.create_all(engine)
