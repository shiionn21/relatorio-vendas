import argparse
import logging
from coleta import carregar_dados
from limpeza import limpar_dados
from analise import analisar
from relatorio import gerar_relatorio

# Configura o log: mostra na tela E grava no arquivo relatorio.log
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("relatorio.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)


def main():
    parser = argparse.ArgumentParser(description="Gera um relatório de vendas a partir de planilhas.")
    parser.add_argument("--entrada", default="entrada", help="Pasta com os arquivos de venda")
    parser.add_argument("--saida", default="saida/relatorio.xlsx", help="Caminho do relatório gerado")
    args = parser.parse_args()

    try:
        logging.info("Iniciando geração do relatório...")
        dados = carregar_dados(args.entrada)
        limpos = limpar_dados(dados)
        logging.info("Dados limpos: %d linhas válidas (de %d)", len(limpos), len(dados))

        resultado = analisar(limpos)
        logging.info("Faturamento total: R$ %.2f", resultado["faturamento_total"])

        gerar_relatorio(resultado, args.saida)
        logging.info("Concluído! Relatório em: %s", args.saida)

    except FileNotFoundError as e:
        logging.error("Arquivo/pasta não encontrado: %s", e)
    except Exception as e:
        logging.exception("Erro inesperado: %s", e)


if __name__ == "__main__":
    main()