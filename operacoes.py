from sqlalchemy.orm import Session
import models, schemas

def criar_registro_historico(db: Session, consulta: schemas.ConsultaCashBack, ip_usuario: str, cashback_gerado: float):
    novo_registro = models.Historico(
        ip_usuario = ip_usuario,
        cliente = consulta.cliente,
        valor_compra = consulta.valor_compra,
        cash_back = cashback_gerado
    )

    db.add(novo_registro)
    db.commit()
    db.refresh(novo_registro)

    return novo_registro

def buscar_historico_por_ip(db: Session, ip_usuario: str):
    return db.query(models.Historico).filter(models.Historico.ip_usuario == ip_usuario).all()