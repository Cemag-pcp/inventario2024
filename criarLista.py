from app import create_app
from app.management.gerar_lista_inventario import generate_inventory_lists

app = create_app()

with app.app_context():
    generate_inventory_lists()