# 🚢 Torre de Controle Logístico: Outflow e Prontidão Portuária

Este projeto é uma solução ponta a ponta (End-to-End) de Engenharia e Análise de Dados focada em resolver um dos maiores desafios do setor de Supply Chain e exportação: o sincronismo entre o escoamento da fábrica e a infraestrutura do porto.

## 🎯 O Problema de Negócio
No setor de papel e celulose, o maior gargalo logístico e risco financeiro não está no espaço da fábrica, mas sim no **Porto**. O armazenamento portuário tem espaço estrito e é extremamente caro. Além disso, se um navio atracar e a carga não estiver pronta para o embarque, a empresa paga multas diárias altíssimas chamadas *Demurrage* (sobre-estadia).

O objetivo deste projeto foi criar um pipeline de dados e um painel tático de monitoramento preventivo. A ferramenta permite que a torre de controle tome ações rápidas para garantir que os lotes do navio sejam atingidos a tempo, sem sobrecarregar a capacidade máxima do armazém do porto.

## 🛠️ Arquitetura e Tecnologias Utilizadas
* **Python (Pandas, NumPy):** Geração de *mock data* simulando 90 dias de movimentação logística contínua e cadência de produção.
* **MySQL Server:** Atuando como Data Warehouse. Criação de uma camada semântica com Views parametrizadas, modelagem **Star Schema** e tratamentos de calendário direto na fonte.
* **DevSecOps:** Uso de variáveis de ambiente (`.env` e `python-dotenv`) para mascaramento seguro de credenciais de banco de dados no script de ingestão.
* **Power BI & DAX:** Conexão direta com o banco relacional, cálculos de inteligência de tempo e modelagem de Dashboard com interface corporativa (Light Theme).

## 📊 Principais Indicadores Desenvolvidos (DAX Avançado)
1. **Prontidão de Navio (Ship Readiness):** Lógica matemática de ciclo contínuo (utilizando a função `MOD` para resto de divisão). Isola o saldo exato do lote do próximo navio (ex: 40.000 tons) sem distorcer o histórico de longo prazo, travando o KPI entre 0 e 100%.
2. **Risco de Lotação do Porto (Dias de Autonomia):** Cruzamento dinâmico entre o estoque real no porto (Total que chegou via trem/caminhão menos os navios que já zarparam) e a velocidade atual de chegada da carga. Se o porto estiver prestes a lotar, o indicador entra em alerta crítico (Zero dias).
3. **Média Diária de Escoamento:** Monitoramento da velocidade (cadência) por modal logístico (Ferroviário vs. Rodoviário).

## 💡 Telas do Dashboard
*<img width="1307" height="732" alt="Torre de Controle" src="https://github.com/user-attachments/assets/c77bba4e-d3ce-42a0-9e49-eeea432d9f9a" />*

---
**Nota:** Os dados utilizados neste projeto são mock-data (fictícios) gerados via Python estritamente para demonstração de portfólio, preservando a lógica matemática e o comportamento de uma operação real de exportação de celulose.
