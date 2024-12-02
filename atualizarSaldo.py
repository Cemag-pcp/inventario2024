from app import create_app
from app.management.atualizar_quantidade import atualizar_quantidades

app = create_app()

with app.app_context():
    # Uso do script
    arquivo_csv = r'excel_dados_inventario/MODELO BASE INVENTÁRIO 2024 - Almox Central.csv'
    atualizar_quantidades(arquivo_csv)