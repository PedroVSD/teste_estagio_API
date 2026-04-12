from sqlalchemy import Column, Integer, String, Float
from database import Base

class Historico(Base):
    __tablename__ = "historico_consultas"

    id = Column(Integer, primary_key=True, index=True)
    ip_usuario = Column(String, index=True)
    cliente = Column(String)
    valor_compra = Column(Float)
    cash_back = Column(Float)