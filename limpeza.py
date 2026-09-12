import pandas as pd


def _para_numero(valor):
    """Converte '49.90', 'R$ 19,90' ou '1.234,56' em número (float)."""
    texto = str(valor).replace("R$", "").strip()
    if "," in texto:  # formato brasileiro: vírgula é decimal
        texto = texto.replace(".", "").replace(",", ".")
    return float(texto)

def _para_data(valor):
    """Lê datas '2026-02-05' (ISO) e '03/02/2026' (BR) corretamente."""
    texto = str(valor).strip()
    if "/" in texto:
        return pd.to_datetime(texto, format="%d/%m/%Y")  # dia/mês/ano
    return pd.to_datetime(texto, format="%Y-%m-%d")       # ano-mês-dia

def limpar_dados(df):
    """Recebe o DataFrame bruto e devolve limpo e padronizado."""
    df = df.copy()

    # 1. Padroniza texto: tira espaços e ajusta maiúsculas
    df["produto"] = df["produto"].str.strip().str.title()
    df["categoria"] = df["categoria"].str.strip().str.capitalize()

    # 2. Preço vira número (trata R$ e vírgula)
    df["preco_unitario"] = df["preco_unitario"].apply(_para_numero)

    # 3. Datas de vários formatos viram um só (regra pelo separador)
    df["data"] = df["data"].apply(_para_data)

    # 4. Preenche campos de texto vazios
    df["cliente"] = df["cliente"].fillna("Não informado")
    df["vendedor"] = df["vendedor"].fillna("Não informado")

    # 5. Remove vendas sem quantidade e converte pra inteiro
    df = df.dropna(subset=["quantidade"])
    df["quantidade"] = df["quantidade"].astype(int)

    # 6. Remove linhas duplicadas (agora que tudo está padronizado)
    df = df.drop_duplicates()

    return df