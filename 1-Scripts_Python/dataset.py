import pandas as pd
import numpy as np
from datetime import timedelta, date

# Configurações do dataset
dias = 90
data_inicial = date(2026, 1, 1)
datas = [data_inicial + timedelta(days=i) for i in range(dias)]

# Simulando produção e escoamento em toneladas
np.random.seed(200)
producao_diaria = np.random.normal(loc=5500, scale=300, size=dias).round(2) # Toneladas produzidas
escoamento_ferrovia = np.random.normal(loc=3000, scale=500, size=dias).round(2) # Toneladas escoadas
escoamento_rodovia = np.random.normal(loc=2000, scale=400, size=dias).round(2)

# Criando o DataFrame
df_outflow = pd.DataFrame({
    'Data': datas,
    'Producao_Fábrica_Ton': producao_diaria,
    'Outflow_Ferrovia_Ton': escoamento_ferrovia,
    'Outflow_Rodovia_Ton': escoamento_rodovia
})

# Calculando o estoque projetado no armazém da fábrica
df_outflow['Total_Escoado_Ton'] = df_outflow['Outflow_Ferrovia_Ton'] + df_outflow['Outflow_Rodovia_Ton']
df_outflow['Variacao_Estoque_Ton'] = df_outflow['Producao_Fábrica_Ton'] - df_outflow['Total_Escoado_Ton']
df_outflow['Saldo_Armazem_Ton'] = df_outflow['Variacao_Estoque_Ton'].cumsum() + 10000 # Começando com 10k tons de estoque

df_outflow.to_csv('dataset_outflow_celulose.csv', index=False)
print("Dataset gerado com sucesso!")