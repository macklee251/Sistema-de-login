from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker

CONN = "sqlite:///sistema_de_login.db"

engine = create_engine(CONN, echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Pessoa(Base):
    __tablename__ = "Pessoa"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    email = Column(String(100))
    senha = Column(String(100))

    def __repr__(self):
        return f"Nome: {self.nome}, Email: {self.email}, Senha: {self.senha}"
        
Base.metadata.create_all(engine)