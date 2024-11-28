from app import db
import os
from app.models import Local, Peca  # Certifique-se de que models.py tem Local e Peca
import pandas as pd
from dotenv import load_dotenv
load_dotenv('.env')

DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

def carregar_dados_csv(caminho_csv):
    # Ler o arquivo CSV ignorando colunas indesejadas
    df = pd.read_csv(caminho_csv, dtype={'CÓDIGO': str})

    # Remover registros com campos obrigatórios nulos
    df = df.dropna(subset=['CÓDIGO', 'SETOR'])
    
    # Iterar sobre as linhas do DataFrame
    for _, row in df.iterrows():
        try:
            # Extrair valores das colunas
            local_nome = row['SETOR'].replace('/', '-') 
            estante = row['LOCALIZAÇÃO'] if pd.notna(row['LOCALIZAÇÃO']) else ''
            almoxarifado = row['ALMOXARIFADO']
            
            # Verificar se o Local já existe
            local = Local.query.filter_by(nome=local_nome, estante=estante,almoxarifado=almoxarifado).first()
            if not local:
                local = Local(nome=local_nome, estante=estante, almoxarifado=almoxarifado)
                db.session.add(local)
                db.session.commit()
                print(f"Local criado: {local.nome}")

            # Criar a peça
            codigo = str(row['CÓDIGO']).strip()
            
            descricao = row['DESCRIÇÃO'] if pd.notna(row['DESCRIÇÃO']) else ''
            quantidade_sistema = (
                float(row['QTD'].replace('.', '').replace(',', '.')) 
                if pd.notna(row['QTD']) and isinstance(row['QTD'], str) 
                else float(row['QTD']) 
                if pd.notna(row['QTD']) 
                else 0.0
            )
            peca_fora_lista = False

             # Verificar se a peça já existe
            peca_existente = Peca.query.filter_by(codigo=codigo, local_id=local.id).first()
            if peca_existente:
                print(f"Peça já existe: {peca_existente}")
                continue  # Ignorar e passar para a próxima linha
            
            peca = Peca(
                codigo=codigo,
                descricao=descricao,
                local_id=local.id,
                quantidade_sistema=quantidade_sistema,
                peca_fora_lista=peca_fora_lista
            )
            db.session.add(peca)
            print(f"Peça criada: {peca}")
        
        except Exception as e:
            print(f"Erro ao processar a linha: {row.to_dict()} - Erro: {e}")
    
    # Commit final
    db.session.commit()
    print("Dados carregados com sucesso!")

def carregar_varios_csv(lista_caminhos_csv):
    for caminho_csv in lista_caminhos_csv:
        print(f"Iniciando processamento do arquivo: {caminho_csv}")
        carregar_dados_csv(caminho_csv)
        print(f"Finalizado processamento do arquivo: {caminho_csv}")

caminhos_csv = [
    'excel_dados_inventario/MODELO BASE INVENTÁRIO 2024 - Almox Corte e Estamparia.csv',
    'excel_dados_inventario/MODELO BASE INVENTÁRIO 2024 - Almox Pintura - Embalagem.csv',
    'excel_dados_inventario/MODELO BASE INVENTÁRIO 2024 - Almox Prod Especiais.csv'
]