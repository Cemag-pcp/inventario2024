from app import create_app, db
from app.management.planilha_dados_inventario import carregar_varios_csv,caminhos_csv

app = create_app()

with app.app_context():
    db.create_all()  # Cria todas as tabelas no banco de dados, caso ainda não existam
    carregar_varios_csv(caminhos_csv)