from flask import render_template, request, jsonify
from . import db
from app.models import Local,Peca, Quantidade

from flask import current_app as app

@app.route("/", methods=['GET'])
def index():
    locais = db.session.query(Local.nome, Local.almoxarifado).distinct().all()
    return render_template("local/local_list.html", locais=locais)

@app.route("/inventario/<local_nome>", methods=['GET'])
def local(local_nome):
    todas_as_pecas = Peca.query.join(Local).filter(Local.nome == local_nome).all()
    estantes = list(set([peca.local.estante for peca in todas_as_pecas]))

    pecas = Peca.query.join(Local).outerjoin(Quantidade).filter(
        Local.nome == local_nome, Quantidade.id == None, Peca.peca_fora_lista == False).all()
    
    return render_template("local/dados_inventario.html", pecas=pecas,estantes=estantes ,local=local_nome)

@app.route("/dashboard", methods=['GET'])
def dashboard():
    return render_template("dashboard/dashboard.html")

@app.route("/api/fora-da-lista", methods=['POST'])
def fora_da_lista():
    data = request.get_json()

    localNome = data.get('localNome')
    codigoPecaForaLista = data.get('codigoPecaForaLista')
    descricaoPecaForaLista = data.get('descricaoPecaForaLista')
    estantePecaForaLista = data.get('estantePecaForaLista')
    quantidadePecaForaLista = data.get('quantidadePecaForaLista')
    peca_fora_lista = True

    # Verificação dos campos obrigatórios
    if not all([localNome, codigoPecaForaLista, estantePecaForaLista, quantidadePecaForaLista]):
        print("Preencha todos os campos obrigatórios")
        print(data)
        return jsonify({'message': 'Preencha todos os campos obrigatórios'}), 400

    # Verifique se o Local com o nome e estante especificados existe
    local = Local.query.filter_by(nome=localNome, estante=estantePecaForaLista).first()
    if not local:
        print("Local não encontrado")
        return jsonify({'message': 'Local não encontrado'}), 404

    # Verifique se já existe uma Peça com o mesmo código no Local
    peca_existente = Peca.query.filter_by(codigo=codigoPecaForaLista, local_id=local.id).first()
    if peca_existente:
        print("Peça já existe no local")
        return jsonify({'message': 'Peça já existe no local'}), 400

    # Criar a nova peça e quantidade
    nova_peca = Peca(
        codigo=codigoPecaForaLista,
        descricao=descricaoPecaForaLista,
        local_id=local.id,
        quantidade_sistema=quantidadePecaForaLista,  # ou ajuste conforme a lógica
        peca_fora_lista=peca_fora_lista
    )
    db.session.add(nova_peca)
    db.session.commit()

    # Criar a nova quantidade associada à peça
    nova_quantidade = Quantidade(
        quantidade=quantidadePecaForaLista,
        peca_id=nova_peca.id
    )
    db.session.add(nova_quantidade)
    db.session.commit()

    return jsonify({'message': 'Peça fora da lista adicionada com sucesso'}), 201

@app.route("/deletar_quantidades", methods=['GET'])
def deletar_quantidades():
    # Deletando as quantidades com IDs entre 1 e 11
    Quantidade.query.filter(Quantidade.id.between(1, 11)).delete(synchronize_session=False)
    
    # Commitando as mudanças no banco de dados
    db.session.commit()

    return jsonify({'message': 'Quantidades deletadas com sucesso'}), 200

@app.route('/mock-data', methods=['GET'])
def mock_data():
    # Dados dos Locais e almoxarifados com diferentes estantes
    locais = [
        {"nome": "Estamparia", "estante": "A1", "almoxarifado": "Estamparia"},
        {"nome": "Estamparia", "estante": "A2", "almoxarifado": "Estamparia"},
        {"nome": "Estamparia", "estante": "A3", "almoxarifado": "Estamparia"},
        {"nome": "Corte", "estante": "B1", "almoxarifado": "Corte"},
        {"nome": "Corte", "estante": "B2", "almoxarifado": "Corte"},
        {"nome": "Eixo", "estante": "C1", "almoxarifado": "Montagem"},
        {"nome": "Eixo", "estante": "C2", "almoxarifado": "Montagem"},
        {"nome": "Chassi", "estante": "D1", "almoxarifado": "Montagem"},
        {"nome": "Chassi", "estante": "D2", "almoxarifado": "Montagem"},
    ]

    # Dados das Peças com referência aos locais e estantes específicas
    pecas = [
        {"codigo": "P001", "descricao": "Peça A1 - Estamparia", "local_nome": "Estamparia", "estante": "A1", "quantidade_sistema": 100},
        {"codigo": "P001", "descricao": "Peça A1 - Estamparia", "local_nome": "Estamparia", "estante": "A2", "quantidade_sistema": 120},
        {"codigo": "P002", "descricao": "Peça A2 - Estamparia", "local_nome": "Estamparia", "estante": "A2", "quantidade_sistema": 150},
        {"codigo": "P002", "descricao": "Peça A2 - Estamparia", "local_nome": "Estamparia", "estante": "A3", "quantidade_sistema": 124},
        {"codigo": "P009", "descricao": "Peça A3 - Estamparia", "local_nome": "Estamparia", "estante": "A3", "quantidade_sistema": 132},
        {"codigo": "P003", "descricao": "Peça B1 - Corte", "local_nome": "Corte", "estante": "B1", "quantidade_sistema": 240},
        {"codigo": "P004", "descricao": "Peça B2 - Corte", "local_nome": "Corte", "estante": "B2", "quantidade_sistema": 260},
        {"codigo": "P005", "descricao": "Peça C1 - Eixo", "local_nome": "Eixo", "estante": "C1", "quantidade_sistema": 150},
        {"codigo": "P006", "descricao": "Peça C2 - Eixo", "local_nome": "Eixo", "estante": "C2", "quantidade_sistema": 170},
        {"codigo": "P007", "descricao": "Peça D1 - Chassi", "local_nome": "Chassi", "estante": "D1", "quantidade_sistema": 300},
        {"codigo": "P008", "descricao": "Peça D2 - Chassi", "local_nome": "Chassi", "estante": "D2", "quantidade_sistema": 320},
    ]

    # Inserção dos Locais
    for local_data in locais:
        local = Local(
            nome=local_data["nome"],
            estante=local_data["estante"],
            almoxarifado=local_data["almoxarifado"]
        )
        db.session.add(local)

    db.session.commit()

    # Inserção das Peças e Quantidades
    for peca_data in pecas:
        # Filtragem do local com nome e estante correspondentes
        local = Local.query.filter_by(nome=peca_data["local_nome"], estante=peca_data["estante"]).first()
        if local:
            peca = Peca(
                codigo=peca_data["codigo"],
                descricao=peca_data["descricao"],
                local=local,
                quantidade_sistema=peca_data["quantidade_sistema"]
            )
            db.session.add(peca)
            db.session.commit()

            # Adicionando quantidade inicial
            quantidade = Quantidade(
                quantidade=peca_data["quantidade_sistema"],
                peca=peca
            )
            db.session.add(quantidade)

    db.session.commit()

    return jsonify({
        "message": "Novos locais e peças adicionados com sucesso!"
    })

@app.route("/api/inventario", methods=['POST'])
def quantidadePecas():
    data = request.get_json()
    idLocal = data.get('id')
    peca = data.get('peca')
    estante = data.get('estante')
    quantidade = data.get('quantidade')
    
    if not all([idLocal, peca, estante, quantidade]):
        print("Algum campo vazio")
        return jsonify({'message': 'Todos os campos são obrigatórios e devem ser preenchidos'}), 400
    
    try:
        quantidade = float(quantidade)  # Converter quantidade para inteiro
    except ValueError:
        return jsonify({'message': 'Quantidade deve ser um número válido'}), 400
    
    if quantidade < 0:
        return jsonify({'message': 'Quantidade não pode ser menor que 0'}), 400

    # Verificando se já existe uma quantidade associada à peça, local e estante fornecidos
    local = Local.query.filter_by(id=idLocal).first()
    if not local:
        print("Local não encontrado")
        return jsonify({'message': 'Local não encontrado'}), 400

    # Verificando se a peça e estante pertencem ao local
    peca_obj = Peca.query.filter_by(local_id=idLocal, codigo=peca).first()
    if not peca_obj:
        print("Peça não encontrada no local especificado")
        return jsonify({'message': 'Peça não encontrada no local especificado'}), 401

    # Verificar se já existe uma quantidade registrada para a peça e estante
    quantidade_existente = Quantidade.query.join(Peca).join(Local).filter(
        Peca.id == peca_obj.id,
        Local.id == idLocal,
        Peca.local_id == idLocal,
        Peca.codigo == peca,
    ).first()

    if quantidade_existente:
        print("Já existe uma quantidade registrada para esta peça e estante")
        return jsonify({'message': 'Já existe uma quantidade registrada para esta peça e estante'}), 402

    # Se não houver quantidade registrada, adiciona a nova quantidade
    nova_quantidade = Quantidade(
        quantidade=quantidade,
        peca_id=peca_obj.id
    )
    db.session.add(nova_quantidade)
    db.session.commit()

    return jsonify({'message': 'Quantidade registrada com sucesso'}), 200

@app.route("/api/dashboard", methods=['GET'])
def pecas_contagem():
    
    total_pecas = Peca.query.count()
    pecas_com_quantidade = Peca.query.join(Quantidade).count()
    pecas_sem_quantidade = total_pecas - pecas_com_quantidade

    if total_pecas > 0:
        porcentagem_com_quantidade = (pecas_com_quantidade / total_pecas) * 100
        porcentagem_sem_quantidade = (pecas_sem_quantidade / total_pecas) * 100
    else:
        porcentagem_com_quantidade = 0
        porcentagem_sem_quantidade = 0

    return jsonify({"nao_contadas": round(porcentagem_sem_quantidade, 2), "contadas": round(porcentagem_com_quantidade, 2)})