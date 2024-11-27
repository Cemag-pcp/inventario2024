import os
from dotenv import load_dotenv

# Carregar as variáveis do arquivo .env (se existir)
load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

# Obter as variáveis de ambiente
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('DB_NAME', 'dbname')
DB_USER = os.getenv('DB_USER', 'username')
DB_PASS = os.getenv('DB_PASS', 'password')

class Config:
    # Configuração do banco de dados PostgreSQL
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_SCHEMA = 'inventario_2024'  # Definindo o schema do banco de dados
