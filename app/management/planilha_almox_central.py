from app import db
from app.models import Local, Peca  # Certifique-se de que models.py tem Local e Peca
import pandas as pd

def carregar_dados_csv(caminho_csv):
    # Ler o arquivo CSV ignorando colunas indesejadas
    df = pd.read_csv(caminho_csv, usecols=lambda col: col not in ['Cod. Localizacao', 'Nome do Local', 'Unnamed: 8'])

    # Remover registros com campos obrigatórios nulos
    df = df.dropna(subset=['Códigos', 'Local'])
    
    # Iterar sobre as linhas do DataFrame
    for _, row in df.iterrows():
        try:
            # Extrair valores das colunas
            local_nome = row['Local']
            celula = row['Célula'] if pd.notna(row['Célula']) else ''
            local_nome = f"{local_nome}-{celula}".strip('-')
            posicao = row['Posição'] if pd.notna(row['Posição']) else ''
            estante = f"{celula}-{posicao}".strip('-')  # Evita '-' isolado quando uma das partes está vazia
            almoxarifado = 'Central'
            
            # Verificar se o Local já existe
            local = Local.query.filter_by(nome=local_nome, estante=estante).first()
            if not local:
                local = Local(nome=local_nome, estante=estante, almoxarifado=almoxarifado)
                db.session.add(local)
                db.session.commit()
                print(f"Local criado: {local.nome}")

            # Criar a peça
            codigo = row['Códigos']
            
            # Verificar se o código contém '-'. Se sim, ignorar essa linha.
            if '-' in str(codigo):
                print(f"Código '{codigo}' contém '-', ignorado.")
                continue
            
            descricao = row['Item'] if pd.notna(row['Item']) else ''
            quantidade_sistema = (
                float(row['Saldo'].replace('.', '').replace(',', '.')) 
                if pd.notna(row['Saldo']) and isinstance(row['Saldo'], str) 
                else float(row['Saldo']) 
                if pd.notna(row['Saldo']) 
                else 0.0
            )
            peca_fora_lista = False
            
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

# Chame a função com o caminho do arquivo CSV
caminho_csv = 'excel_dados_inventario/Mapeamento Almoxarifado - Mapeamento.csv'
