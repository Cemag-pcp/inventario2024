from app import create_app, db
from app.management.planilha_almox_central import carregar_dados_csv,caminho_csv

app = create_app()

with app.app_context():
    db.create_all()  # Cria todas as tabelas no banco de dados, caso ainda não existam
    carregar_dados_csv(caminho_csv)