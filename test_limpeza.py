import pandas as pd
from limpeza import limpar_dados, _para_numero


def test_para_numero_formato_brasileiro():
    assert _para_numero("R$ 19,90") == 19.90


def test_para_numero_formato_com_ponto():
    assert _para_numero("49.90") == 49.90


def test_remove_duplicatas():
    df = pd.DataFrame({
        "data": ["2026-01-01", "2026-01-01"],
        "produto": ["Camiseta", "Camiseta"],
        "categoria": ["Vestuário", "Vestuário"],
        "quantidade": [1, 1],
        "preco_unitario": ["49.90", "49.90"],
        "cliente": ["Ana", "Ana"],
        "vendedor": ["Carlos", "Carlos"],
    })
    assert len(limpar_dados(df)) == 1


def test_remove_venda_sem_quantidade():
    df = pd.DataFrame({
        "data": ["2026-01-01"],
        "produto": ["Camiseta"],
        "categoria": ["Vestuário"],
        "quantidade": [None],
        "preco_unitario": ["49.90"],
        "cliente": ["Ana"],
        "vendedor": ["Carlos"],
    })
    assert len(limpar_dados(df)) == 0


def test_preenche_cliente_vazio():
    df = pd.DataFrame({
        "data": ["2026-01-01"],
        "produto": ["Camiseta"],
        "categoria": ["Vestuário"],
        "quantidade": [1],
        "preco_unitario": ["49.90"],
        "cliente": [None],
        "vendedor": ["Carlos"],
    })
    assert limpar_dados(df).iloc[0]["cliente"] == "Não informado"