import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# 1. Carrega as variáveis de segurança do arquivo .env
load_dotenv()

# 2. Busca as credenciais mascaradas
usuario = os.getenv('DB_USER')
senha = os.getenv('DB_PASS')
host = os.getenv('DB_HOST')
porta = os.getenv('DB_PORT')
banco_de_dados = os.getenv('DB_NAME')

# 3. Carregar o dataset do nosso "Data Lake" (arquivo local)
print("Lendo o arquivo CSV do Data Lake...")
df_outflow = pd.read_csv('dataset_outflow_celulose.csv')

# 4. Configurar a conexão segura com o MySQL (Data Warehouse)
string_conexao = f"mysql+pymysql://{usuario}:{senha}@{host}:{porta}/{banco_de_dados}"

print("Conectando ao MySQL Server de forma segura...")
engine = create_engine(string_conexao)

# 5. Enviar os dados para o banco
print("Enviando dados para a tabela 'tb_outflow_bruto'...")
df_outflow.to_sql(name='tb_outflow_bruto', con=engine, if_exists='replace', index=False)

print("Carga finalizada com sucesso!")