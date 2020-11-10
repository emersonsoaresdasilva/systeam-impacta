from database.dados import *


''' BANCO DE DADOS GERAL '''
def classificar_equipes(dados):
    pass

''' BANCO DADOS EQUIPE '''
def criar_equipe(Equipe):
    EQUIPES.append(Equipe)

def pegar_equipe(sigla='*'):
    if sigla == '*':
        return EQUIPES
    else:
        for e in EQUIPES:
            if e.sigla == sigla: return e 
    return False

def obter_dados_da_equipe(Equipe):
    partidas = listar_partidas_da_equipe(Equipe)
    dados = {'pontos': 0, 'jogos' : 0, 'vitorias' : 0, 'derrotas' : 0, 'empates' : 0 }
    dados['jogos'] = len(partidas)
    for p in partidas:
        if p.pontos_casa == p.pontos_visita:
            dados['empates'] += 1
        elif p.equipe_casa.sigla == Equipe.sigla and p.pontos_casa > p.pontos_visita or p.equipe_visita.sigla == Equipe.sigla and p.pontos_casa < p.pontos_visita:
            dados['vitorias'] += 1
    dados['derrotas'] = dados['jogos'] - (dados['vitorias'] + dados['empates'])
    dados['pontos'] +=  dados['vitorias'] * 3 + dados['empates']
    return dados


''' BANCO DADOS PARTIDAS '''
def pegar_partida(id='*'):
    if id == '*':
        return PARTIDAS
    else:
        for p in PARTIDAS:
            if p.equipe_casa.sigla + p.equipe_casa.sigla == id or p.equipe_casa.sigla + p.equipe_casa.sigla == id: return p
    return False

def listar_partidas_da_equipe(Equipe):
    partidas = []
    for p in PARTIDAS:
        if p.equipe_casa.sigla == Equipe.sigla or p.equipe_visita.sigla == Equipe.sigla:
            partidas.append(p)
    return partidas

''' BANCO DADOS USUARIOS '''
def pegar_usuario(email, senha):
    return [u for u in USUARIOS if u.email == u.email][0]


def criar_equipe(Equipe):
    EQUIPES.append(Equipe)