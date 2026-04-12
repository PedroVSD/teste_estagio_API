from pydantic import BaseModel, ConfigDict

class ConsultaCashBack(BaseModel):
    cliente: str
    valor_compra: float

class HistoricoResponse(BaseModel):
    cliente: str
    valor_compra: float
    cash_back: float

    model_config = ConfigDict(from_attributes=True)