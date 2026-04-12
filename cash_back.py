# Primeiro calcular o cashback base e depois o cashback VIP
# O cashback é só aplicado no final da compra
# vip tem 10% de bonus sobre o base que é 5%
# Compras acima de 500 reais o cashback dobra, ou seja cashback final * 2



def cash_back(preco_original_final: float, cliente: str) -> float:
    cash_back_base = preco_original_final * 0.05

    if cliente == 'VIP':
        cash_back_atual = cash_back_base * 1.10
    else:
        cash_back_atual = cash_back_base

    if preco_original_final > 500.00:
        cash_back_final = cash_back_atual * 2
    else:
        cash_back_final = cash_back_atual

    return round(cash_back_final, 2)


print(cash_back(480, 'VIP'))
print(cash_back(540, 'VIP'))
print(cash_back(480, 'Normal'))
print(cash_back(540, 'Normal'))
