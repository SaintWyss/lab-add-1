from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('sqlite:///data_loader_app/archivos.db', echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base()

def init_db():
    from ..models.archivo_modelo import ArchivoCSV, ArchivoJSON
    Base.metadata.create_all(engine)