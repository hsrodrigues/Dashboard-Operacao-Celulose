# 🚢 Torre de Controle Logístico: Outflow de Celulose

Este projeto é uma solução ponta a ponta (End-to-End) de Engenharia e Análise de Dados focada em resolver um dos maiores desafios do setor de Supply Chain e exportação: o descompasso entre a produção da fábrica e a prontidão portuária (Ship Readiness).

## 🎯 O Problema de Negócio
No setor de papel e celulose, o aluguel de um navio cargueiro é cobrado por dia. Se o navio atracar no porto e a carga não estiver pronta porque o fluxo de trens e caminhões atrasou, a empresa paga multas altíssimas de *Demurrage* (sobre-estadia). 

O objetivo deste projeto foi criar um pipeline de dados e um painel tático para monitorar o risco de lotação do armazém do fábrica e garantir que a meta em toneladas para liberar o próximo navio seja atingida dentro do prazo.

## 🛠️ Arquitetura e Tecnologias Utilizadas
* **Python (Pandas, NumPy):** Criação de dados sintéticos para simular 90 dias de produção contínua e movimentação logística.
* **MySQL Server:** Armazenamento dos dados brutos e construção de uma camada semântica com Views parametrizadas no modelo **Star Schema**.
* **Power BI & DAX:** Conexão direta com o banco relacional, cálculos de inteligência de tempo e modelagem de um Dashboard com interface moderna (Light Theme Corporativo).

## 📊 Principais Indicadores Desenvolvidos (DAX)
1. **Prontidão de Navio (Ship Readiness):** Lógica que isola lotes de 40.000 toneladas e exibe, em tempo real, a porcentagem de conclusão para o próximo embarque.
2. **Dias para Lotação (Risco de Armazém):** Medida de alerta preventivo (`LASTDATE` e inteligência de tempo) que cruza o saldo diário atual com a média de produção para prever um possível travamento logístico.
3. **Média Diária de Escoamento:** Monitoramento da cadência por modal (Ferroviário vs. Rodoviário).

## 💡 Telas do Dashboard
*<img width="1308" height="733" alt="Torre de Controle" src="https://github.com/user-attachments/assets/cafd5f0a-3b2a-4592-8208-f8549c46ec4e" />*

---
**Nota:** Os dados utilizados neste projeto são mock-data (fictícios) gerados via Python estritamente para demonstração de portfólio, preservando a lógica e o comportamento de uma operação real.
