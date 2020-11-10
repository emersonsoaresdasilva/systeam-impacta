from database.dados import *

''' BANCO DADOS EQUIPE '''
def pegar_equipe(sigla='*'):
    if sigla == '*':
        return EQUIPES
    else:
        for e in EQUIPES:
            if e.sigla == sigla: return e 
    return False

def calcular_pontos_da_equipe(Equipe):
    pontos = 0
    partidas = listar_partidas_da_equipe(Equipe)
    for p in partidas:
        if p.pontos_casa == p.pontos_visita:
            pontos += 1
        elif p.equipe_casa.sigla == Equipe.sigla:
            if p.pontos_casa > p.pontos_visita:
                pontos += 3
        elif p.equipe_visita.sigla == Equipe.sigla:
            if p.pontos_casa < p.pontos_visita:
                pontos += 3
    return pontos



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