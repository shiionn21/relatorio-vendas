import pandas as pd
from analise import analisar


def test_faturamento_total():
    df = pd.DataFrame({
        "data": pd.to_datetime(["2026-01-01", "2026-02-01"]),
        "produto": ["A", "B"],
        "categoria": ["X", "Y"],
        "quantidade": [2, 3],
        "preco_unitario": [10.0, 20.0],
        "cliente": ["Ana", "Bia"],
        "vendedor": ["Carlos", "Marina"],
    })
    resultado = analisar(df)
    # 2*10 + 3*20 = 80
    assert resultado["faturamento_total"] == 80.0