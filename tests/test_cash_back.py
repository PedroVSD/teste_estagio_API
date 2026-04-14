from cash_back import calcular_cash_back

def test_cliente_normal_compra_pequena():
    resultado = calcular_cash_back(valor_compra=100.0, cliente="Normal")
    assert resultado == 5.0

def test_cliente_vip_compra_pequena():
    resultado = calcular_cash_back(valor_compra=100.0, cliente="Vip")
    assert resultado == 5.5

def test_cliente_normal_compra_grande():
    resultado = calcular_cash_back(valor_compra=600.0, cliente="Normal")
    assert resultado == 60.0

def test_cliente_vip_compra_grande():
    resultado = calcular_cash_back(valor_compra=600.0, cliente="Vip")
    assert resultado == 66.0
