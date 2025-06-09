from ..database.db_connector import Base

class BaseModel(Base):
    __abstract__ = True