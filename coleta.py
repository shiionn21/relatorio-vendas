import logging
import pandas as pd
from pathlib import Path


def carregar_dados(pasta_entrada="entrada"):
    """Lê todos os CSV e Excel da pasta de entrada e junta num só DataFrame."""
    pasta = Path(pasta_entrada)
    arquivos = list(pasta.glob("*.csv")) + list(pasta.glob("*.xlsx"))

    if not arquivos:
        raise FileNotFoundError(f"Nenhum arquivo encontrado em '{pasta_entrada}'")

    tabelas = []
    for arquivo in arquivos:
        try:
            if arquivo.suffix == ".csv":
                df = pd.read_csv(arquivo)
            else:
                df = pd.read_excel(arquivo)
            df["arquivo_origem"] = arquivo.name
            tabelas.append(df)
            logging.info("Lido: %s (%d linhas)", arquivo.name, len(df))
        except Exception as e:
            logging.warning("Falhou ao ler %s: %s (ignorado)", arquivo.name, e)

    if not tabelas:
        raise ValueError("Nenhum arquivo pôde ser lido.")

    return pd.concat(tabelas, ignore_index=True)