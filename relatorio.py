from pathlib import Path
import pandas as pd
from openpyxl.chart import BarChart, LineChart, Reference


def gerar_relatorio(resultado, caminho_saida="saida/relatorio.xlsx"):
    """Gera uma planilha Excel com abas e gráficos a partir das métricas."""
    Path(caminho_saida).parent.mkdir(parents=True, exist_ok=True)

    with pd.ExcelWriter(caminho_saida, engine="openpyxl") as writer:
        # Cada métrica vira uma aba
        resumo = pd.DataFrame({
            "Métrica": ["Faturamento total"],
            "Valor (R$)": [resultado["faturamento_total"]],
        })
        resumo.to_excel(writer, sheet_name="Resumo", index=False)
        resultado["por_mes"].to_excel(writer, sheet_name="Por mês", index=False)
        resultado["top_produtos"].to_excel(writer, sheet_name="Top produtos", index=False)
        resultado["top_clientes"].to_excel(writer, sheet_name="Top clientes", index=False)
        resultado["por_vendedor"].to_excel(writer, sheet_name="Por vendedor", index=False)

        # --- Gráfico de linha: faturamento por mês ---
        ws = writer.sheets["Por mês"]
        grafico_mes = BarChart()
        grafico_mes.title = "Faturamento por mês"
        dados = Reference(ws, min_col=2, min_row=1, max_row=ws.max_row)
        categorias = Reference(ws, min_col=1, min_row=2, max_row=ws.max_row)
        grafico_mes.add_data(dados, titles_from_data=True)
        grafico_mes.set_categories(categorias)
        ws.add_chart(grafico_mes, "E2")

        # --- Gráfico de barras: top produtos ---
        ws = writer.sheets["Top produtos"]
        grafico_prod = BarChart()
        grafico_prod.title = "Top produtos"
        dados = Reference(ws, min_col=2, min_row=1, max_row=ws.max_row)
        categorias = Reference(ws, min_col=1, min_row=2, max_row=ws.max_row)
        grafico_prod.add_data(dados, titles_from_data=True)
        grafico_prod.set_categories(categorias)
        ws.add_chart(grafico_prod, "E2")

    print(f"Relatório gerado em: {caminho_saida}")