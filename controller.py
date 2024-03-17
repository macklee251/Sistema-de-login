from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import hashlib
from model import Pessoa

def return_session():
    CONN = "sqlite:///sistema_de_login.db"
    engine = create_engine(CONN, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

class ControllerCadastro():
    @classmethod
    def cadastrar(cls, nome, email, senha):
        session = return_session()
        
        if len(nome) > 50 or len(nome) < 3:
            return 2
        if len(email) > 200:
            return 3
        if len(senha) > 100 or len(senha) < 6:
            return 4
        
        usuario = session.query(Pessoa).filter(Pessoa.email == email).all()
        if len(usuario) > 0:
            return 5
            
        try:
            senha = hashlib.sha256(senha.encode()).hexdigest()
            pessoa = Pessoa(nome=nome, email=email, senha=senha)
            session.add(pessoa)
            session.commit()
            session.close()
            return 1
        except:
            return 6
    
    
class ControllerLogin():
    @classmethod
    def login(cls, email, senha):
        session = return_session()
        senha = hashlib.sha256(senha.encode()).hexdigest()
        usuario_logado = session.query(Pessoa).filter(Pessoa.email == email, Pessoa.senha == senha).all()
        if usuario_logado:
            return {"logado": True, id: usuario_logado[0].id}
        else:
            return False
        
print(ControllerLogin.login("allison@gmail.com", "sousa13"))
    
session = return_session()    
x = session.query(Pessoa).all()
print(x)
        