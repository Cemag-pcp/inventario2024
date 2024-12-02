import os
from app import db, create_app
import pandas as pd
from app.models import Peca, Local

# Configuração de variáveis de ambiente
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')


def atualizar_quantidades(csv_file):
    connection = db.engine.connect()
    trans = connection.begin()  # Iniciar transação
    try:
        df = pd.read_csv(csv_file,dtype={'CÓDIGO': str})
    
        for index, row in df.iterrows():
            setor = row['SETOR']
            almoxarifado = row['ALMOXARIFADO']
            codigo = row['CODIGO']
            quantidade = row['QTD']

            quantidade = str(quantidade).replace(',', '.')
            quantidade = float(quantidade)
            
            # Obter o almoxarifado correspondente
            local = db.session.query(Local).filter_by(nome=setor, almoxarifado=almoxarifado).first()
            
            if local:
                # Encontrar a peça correspondente
                peca = db.session.query(Peca).filter_by(codigo=codigo, local_id=local.id).first()
                
                if peca:
                    # Atualizar a quantidade do sistema
                    peca.quantidade_sistema = quantidade
                    db.session.commit()
                    print(f"Quantidade da peça {codigo} atualizada para {quantidade} no almoxarifado {almoxarifado}.")
                else:
                    print(f"Peça com código {codigo} não encontrada no setor {setor} do almoxarifado {almoxarifado}.")
            else:
                print(f"Almoxarifado {almoxarifado} não encontrado para o setor {setor}.")
    except Exception as e:
        trans.rollback()  # Reverter transações em caso de erro
        print(f"Erro ao processar o arquivo: {csv_file} - Erro: {e}")
    finally:
        connection.close()  # Garantir que a conexão seja fechada
        print("Conexão encerrada.")
