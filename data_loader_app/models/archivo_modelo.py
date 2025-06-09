from sqlalchemy import Column, Integer, String, Float
from .base_model import BaseModel

class ArchivoCSV(BaseModel):
    __tablename__ = 'archivo_csv'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    valor = Column(Float)

class ArchivoJSON(BaseModel):
    __tablename__ = 'archivo_json'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    descripcion = Column(String, nullable=False)
    cantidad = Column(Integer)