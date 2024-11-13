from app import create_app, db

app = create_app()

with app.app_context():
    db.create_all()  # Cria todas as tabelas no banco de dados, caso ainda não existam

if __name__ == '__main__':
    app.run(debug=True)
