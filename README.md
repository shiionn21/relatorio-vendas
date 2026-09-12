# 📊 Gerador de Relatórios de Vendas

Automação em Python que lê várias planilhas de vendas (bagunçadas), limpa e consolida os dados, e gera um **relatório Excel profissional com gráficos** — tudo com um comando. Projeto de portfólio focado em processamento de dados e boas práticas.

---

## 📋 Sobre o projeto

Dados de vendas do mundo real chegam sujos: arquivos separados por mês, datas em formatos diferentes, preços como `R$ 19,90` e `49.90` misturados, linhas duplicadas e campos vazios. Este projeto resolve isso de ponta a ponta, seguindo um **pipeline** em camadas:

1. **Coleta** — lê todos os CSV/Excel de uma pasta e junta num só conjunto.
2. **Limpeza** — remove duplicatas, padroniza datas e preços, trata campos vazios.
3. **Análise** — calcula faturamento total, por mês, top produtos, top clientes e por vendedor.
4. **Relatório** — gera uma planilha Excel com abas e gráficos, pronta para enviar.

O código é dividido em módulos (`coleta`, `limpeza`, `analise`, `relatorio`), com interface de linha de comando, logging e testes automatizados.

---

## 🛠️ Tecnologias

- **Python 3**
- **pandas** — manipulação e análise de dados
- **openpyxl** — geração de Excel com gráficos
- **pytest** — testes automatizados
- **argparse / logging** — CLI e registro de execução

---

## 🚀 Como rodar

```bash
# 1. Clonar
git clone https://github.com/shiionn21/relatorio-vendas.git
cd relatorio-vendas

# 2. Ambiente virtual
python -m venv venv
.\venv\Scripts\activate        # Windows
# source venv/bin/activate     # Linux/Mac

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Rodar (usa a pasta 'entrada/' por padrão)
python main.py
```

O relatório é gerado em `saida/relatorio.xlsx`.

### Opções de linha de comando

```bash
python main.py --entrada dados/ --saida saida/relatorio_q1.xlsx
```

| Opção       | Descrição                          | Padrão                |
|-------------|------------------------------------|-----------------------|
| `--entrada` | Pasta com os arquivos de venda     | `entrada`             |
| `--saida`   | Caminho do relatório gerado        | `saida/relatorio.xlsx`|

---

## 🧪 Testes

```bash
pytest
```

Cobrem a lógica de limpeza (conversão de preços, remoção de duplicatas, tratamento de vazios) e o cálculo de faturamento.

---

## 📁 Estrutura

```
relatorio-vendas/
├── entrada/          # planilhas de venda (entrada)
├── saida/            # relatório gerado
├── coleta.py         # lê e junta os arquivos
├── limpeza.py        # trata e padroniza os dados
├── analise.py        # calcula as métricas
├── relatorio.py      # gera o Excel com gráficos
├── main.py           # ponto de entrada (CLI + logging)
├── test_limpeza.py   # testes da limpeza
├── test_analise.py   # testes da análise
└── requirements.txt
```

---

## 📈 Exemplo de saída

O relatório gerado contém 5 abas (Resumo, Por mês, Top produtos, Top clientes, Por vendedor) e gráficos de faturamento mensal e ranking de produtos.

---

## 🗺️ Próximos passos (roadmap)

- [ ] Exportar também uma versão em **PDF** do relatório.
- [ ] **Dashboard** interativo (Streamlit) em vez de só Excel.
- [ ] Agendamento para rodar **automaticamente** toda semana.
- [ ] Ler direto de um **banco de dados** além de arquivos.

---

## 👤 Autor

**Anderson Souza** — Estudante de Análise e Desenvolvimento de Sistemas.

- GitHub: [@shiionn21](https://github.com/shiionn21)
