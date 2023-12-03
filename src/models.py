import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
Base = declarative_base()



class Usuario(Base):
    __tablename__ = 'usuarios'
    email = Column(Integer, primary_key=True)
    usuario = Column(String(250), ForeignKey('naves_favoritas'),ForeignKey('personas_favoritas'),ForeignKey('planetas_favoritas'))
    password = Column(String(250), nullable=False)


class Naves(Base):
    __tablename__ = 'naves'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    modelo = Column(String(250), nullable=False)
    clase_de_nave = Column(String(250), nullable=False)
    costo_en_creditos = Column(String(250), nullable=False)
    longitud = Column(String(250), nullable=False)
    capacidad_de_pasajeros = Column(Integer, nullable=False)
    MGLT = Column(String(250), nullable=False)
    capacidad_de_carga = Column(Integer, nullable=False)
    provisiones = Column(Integer, nullable=False)
    hypermotor = Column(String(250), nullable=False)
class Personas(Base):
    __tablename__ = 'personas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    genero =Column(String(250), nullable=False)
    especie =Column(String(250), nullable=False)
    height =Column(String(250), nullable=False)
    mass=Column(String(250), nullable=False)
    skin_color =Column(String(250), nullable=False)
    eye_color =Column(String(250), nullable=False)
    birth_year =Column(String(250), nullable=False)
    hair_color =Column(String(250), nullable=False)
class Planetas(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    terreno =Column(String(250), nullable=False)
    poblacion =Column(String(250), nullable=False)
    diametro =Column(String(250), nullable=False)
    rotation_period =Column(String(250), nullable=False)
    orbital_period =Column(String(250), nullable=False)
    gravity =Column(String(250), nullable=False)
    climate =Column(String(250), nullable=False)
    surface_water =Column(String(250), nullable=False)


class Naves_favoritas(Base):
    __tablename__ = 'naves_favoritas'
    id = Column(Integer, primary_key=True)
    nave_id = Column(Integer, ForeignKey('naves.id'))
    usuario_id =Column(Integer, ForeignKey('naves.id'))
class Personas_favoritas(Base):
    __tablename__ = 'personas_favoritas'
    id = Column(Integer, primary_key=True)
    nave_id = Column(Integer, ForeignKey('personas.id'))
    usuario_id =Column(Integer, ForeignKey('personas.id'))
class Planetas_favoritas(Base):
    __tablename__ = 'planetas_favoritas'
    id = Column(Integer, primary_key=True)
    nave_id = Column(Integer, ForeignKey('planetas.id'))
    usuario_id =Column(Integer, ForeignKey('planetas.id'))

 
    


    def to_dict(self):
        return {}
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

