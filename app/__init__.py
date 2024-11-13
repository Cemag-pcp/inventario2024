# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Importa o Flask-Migrate

db = SQLAlchemy()
migrate = Migrate()  # Inicializa o Migrate sem uma aplicação ainda

def create_app(config_class='config.Config'):
    main = Flask(__name__)
    main.config.from_object(config_class)
    
    db.init_app(main)
    migrate.init_app(main, db)  # Conecta o Migrate ao app e ao db
    
    with main.app_context():
        from . import views

    return main
