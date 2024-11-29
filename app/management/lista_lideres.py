lideres = [
    {"Almoxarifado": "Almox Corte e Estamparia", "Setor": "MP", "Líder": "ALEX"},
    {"Almoxarifado": "Almox Corte e Estamparia", "Setor": "PEÇA", "Líder": "ALEX"},
    {"Almoxarifado": "Almox Pintura - Embalagem", "Setor": "COMPONENTES", "Líder": "ERICA"},
    {"Almoxarifado": "Almox Pintura - Embalagem", "Setor": "CONJ", "Líder": "ERICA"},
    {"Almoxarifado": "Almox Pintura - Embalagem", "Setor": "PEÇA", "Líder": "ERICA"},
    {"Almoxarifado": "Almox Pintura - Embalagem", "Setor": "PEÇAS", "Líder": "ERICA"},
    {"Almoxarifado": "Almox Prod Especiais", "Setor": "MP", "Líder": "VICTOR"},
    {"Almoxarifado": "Almox Prod Especiais", "Setor": "PEÇA", "Líder": "VICTOR"},
    {"Almoxarifado": "Central", "Setor": "AL01 - COR", "Líder": "ERIC"},
    {"Almoxarifado": "Central", "Setor": "AL01 - GAV", "Líder": "EVANDRO"},
    {"Almoxarifado": "Central", "Setor": "AL01 - SL1", "Líder": "ERIC"},
    {"Almoxarifado": "Central", "Setor": "AL01 - EST", "Líder": "EVANDRO"},
    {"Almoxarifado": "Central", "Setor": "AL01 - SL2", "Líder": "MAYLSON"},
    {"Almoxarifado": "Central", "Setor": "AL01 - AM", "Líder": "MAYLSON"},
    {"Almoxarifado": "Central", "Setor": "AL07 - SALA", "Líder": "EVANDRO"},
    {"Almoxarifado": "Central", "Setor": "AL03 - INFLAMÁVEIS", "Líder": "EVANDRO"},
    {"Almoxarifado": "Central", "Setor": "AL02 - GALPÃO", "Líder": "MAYLSON"},
    {"Almoxarifado": "Central", "Setor": "AL08 - PROJETOS", "Líder": "ERIC"},
    {"Almoxarifado": "Central", "Setor": "AL06 - CARPINTARIA", "Líder": "MAYLSON"},
    {"Almoxarifado": "Central", "Setor": "AL05 - BORRACHARIA", "Líder": "MAYLSON"},
    {"Almoxarifado": "Central", "Setor": "AL10 - GASES", "Líder": "ERIC"},
    {"Almoxarifado": "Central", "Setor": "AL01 - EPI", "Líder": "SESMT"},
    {"Almoxarifado": "Central", "Setor": "AL09 - SALA", "Líder": "MAYLSON"},
    {"Almoxarifado": "Central", "Setor": "AL04 - CHA", "Líder": "PCP"},
    {"Almoxarifado": "Central", "Setor": "AL04 - SER", "Líder": "PCP"},
    {"Almoxarifado": "Central", "Setor": "NÃO EXISTE - NÃO EXISTE", "Líder": "EVANDRO"},
    {"Almoxarifado": "Central", "Setor": "MANUTENÇÃO - MANUTENÇÃO", "Líder": "MANUTENÇÃO"},
    {"Almoxarifado": "Central", "Setor": "AL01 - ACESS", "Líder": "MAYLSON"},
]

def get_lider(almoxarifado, setor):
    """Retorna o nome do líder com base no almoxarifado e setor."""
    for lider in lideres:
        if lider["Almoxarifado"] == almoxarifado and lider["Setor"] == setor:
            return lider["Líder"]
    return "Líder não definido"