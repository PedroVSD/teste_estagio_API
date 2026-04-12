# Primeiro calcular o cashback base e depois o cashback VIP
# O cashback é só aplicado no final da compra
# vip tem 10% de bonus sobre o base que é 5%
# Compras acima de 500 reais o cashback dobra, ou seja cashback final * 2

#def desconto(preco: float, percentual_desconto: float) -> float:
    #reco_desconto = preco * percentual_desconto
    #preco_final = preco - preco_desconto
    #return preco_final

# Mudei a ordem: o cliente vem em segundo, e o cupom vai pro final valendo 0.0 por padrão
def calcular_cash_back(valor_compra: float, cliente: str) -> float:
    cash_back_base = valor_compra * 0.05

    if cliente.lower() == 'vip':
        cash_back_atual = cash_back_base * 1.10
    else:
        cash_back_atual = cash_back_base

    if valor_compra > 500.00:
        cash_back_final = cash_back_atual * 2
    else:
        cash_back_final = cash_back_atual

    # Retorna o valor arredondado com 2 casas decimais
    return round(cash_back_final, 2)

# --- Testes Unitários ---
# Obs: Ajustei o nome da função no print para bater com o nome da função (calcular_cash_back)
# print(calcular_cash_back(600, 0.2, 'VIP'))    # Esperado: 26.4
# print(calcular_cash_back(600, 0.1, 'VIP'))    # Esperado: 59.4
# print(calcular_cash_back(600, 0.2, 'Normal')) # Esperado: 24.0
# print(calcular_cash_back(600, 0.1, 'Normal')) # Esperado: 54.0

#print(calcular_cash_back(600, 'vip'))

#print(cash_back(600, 0.2, 'VIP'))
#print(cash_back(600, 0.1, 'VIP'))
#print(cash_back(600, 0.2, 'Normal'))
#print(cash_back(600, 0.1, 'Normal'))

#print(cash_back(600, 0.15, 'VIP'))

#26.4
#59.4
#24.0
#54.0
