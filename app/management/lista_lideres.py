lideres = [
    {"Almoxarifado": "Almox Corte e Estamparia", "Setor": "MP", "Líder": "ALEX"},
    {"Almoxarifado": "Almox Corte e Estamparia", "Setor": "PEÇA", "Líder": "ALEX"},
    {"Almoxarifado": "Almox Pintura - Embalagem", "Setor": "COMPONENTES", "Líder": "ERICA"},
    {"Almoxarifado": "Almox Pintura - Embalagem", "Setor": "CONJ", "Líder": "ERICA"},
    {"Almoxarifado": "Almox Pintura - Embalagem", "Setor": "PEÇA", "Líder": "ERICA"},
    {"Almoxarifado": "Almox Pintura - Embalagem", "Setor": "PEÇAS", "Líder": "ERICA"},
    {"Almoxarifado": "Almox Prod Especiais", "Setor": "MP", "Líder": "VICTOR"},
    {"Almoxarifado": "Almox Prod Especiais", "Setor": "PEÇA", "Líder": "VICTOR"},
]

def get_lider(almoxarifado, setor):
    """Retorna o nome do líder com base no almoxarifado e setor."""
    for lider in lideres:
        if lider["Almoxarifado"] == almoxarifado and lider["Setor"] == setor:
            return lider["Líder"]
    return "Líder não definido"