import pandas as pd


def analisar(df):
    """Recebe o DataFrame limpo e devolve um dicionário com as métricas."""
    df = df.copy()

    # Coluna nova: valor total de cada venda (quantidade x preço)
    df["valor_total"] = df["quantidade"] * df["preco_unitario"]

    # Faturamento total geral
    faturamento_total = df["valor_total"].sum()

    # Faturamento por mês
    df["mes"] = df["data"].dt.to_period("M").astype(str)
    por_mes = df.groupby("mes")["valor_total"].sum().reset_index()

    # Top 5 produtos por faturamento
    top_produtos = (
        df.groupby("produto")["valor_total"].sum()
        .sort_values(ascending=False).head(5).reset_index()
    )

    # Top 5 clientes
    top_clientes = (
        df.groupby("cliente")["valor_total"].sum()
        .sort_values(ascending=False).head(5).reset_index()
    )

    # Faturamento por vendedor
    por_vendedor = (
        df.groupby("vendedor")["valor_total"].sum()
        .sort_values(ascending=False).reset_index()
    )

    return {
        "dados": df,
        "faturamento_total": faturamento_total,
        "por_mes": por_mes,
        "top_produtos": top_produtos,
        "top_clientes": top_clientes,
        "por_vendedor": por_vendedor,
    }