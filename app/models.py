from app import db

class Local(db.Model):
    __tablename__ = 'locais'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(60), nullable=False)
    estante = db.Column(db.String(100), nullable=False)
    pecas = db.relationship('Peca', backref='local', lazy=True)
    almoxarifado = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Local {self.nome} do {self.almoxarifado}>'

class Peca(db.Model):
    __tablename__ = 'pecas'

    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(120), nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    local_id = db.Column(db.Integer, db.ForeignKey('locais.id'), nullable=False) 
    quantidade = db.relationship('Quantidade', backref='peca', lazy=True)
    quantidade_sistema = db.Column(db.Integer, nullable=True)
    peca_fora_lista = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Peça {self.codigo}, Quantidade {self.quantidade.quantidade if self.quantidade else "não definida"} no Local {self.local.nome}>'

class Quantidade(db.Model):
    __tablename__ = 'quantidades'

    id = db.Column(db.Integer, primary_key=True)
    quantidade = db.Column(db.Integer, nullable=False)
    peca_id = db.Column(db.Integer, db.ForeignKey('pecas.id'), nullable=False)  # Chave estrangeira para Peca

    def __repr__(self):
        return f'<Quantidade {self.quantidade}>'
