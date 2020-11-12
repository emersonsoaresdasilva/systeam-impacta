from database.dados import *

''' BANCO DE DADOS GERAL '''
def classificar_equipes(dados):
    pass

''' BANCO DADOS EQUIPE '''
def criar_equipe(equipe):
    if pegar_equipe(equipe.sigla) == False:
        EQUIPES.append(equipe)
        return True
    return False

def deletar_equipe(sigla):
    i = pegar_indice_equipe(sigla)
    if i != False or i == 0:
        del(EQUIPES[i])
        return True
    return False

def alterar_equipe(sigla_anterior, equipe):
    if pegar_equipe(equipe.sigla) == False or sigla_anterior == equipe.sigla:
        i = pegar_indice_partida(sigla_anterior)
        if i != False or i == 0:
            EQUIPES[i] = equipe
            return True
    return False

def pegar_equipe(sigla='*'):
    if sigla == '*':
        return EQUIPES
    else:
        for e in EQUIPES:
            if e.sigla == sigla: return e 
    return False

def obter_dados_da_equipe(equipe):
    partidas = listar_partidas_da_equipe(equipe.sigla)
    dados = {'pontos': 0, 'jogos' : 0, 'vitorias' : 0, 'derrotas' : 0, 'empates' : 0 }
    dados['jogos'] = len(partidas)
    for p in partidas:
        if p.pontos_casa == p.pontos_visita:
            dados['empates'] += 1
        elif p.equipe_casa.sigla == equipe.sigla and p.pontos_casa > p.pontos_visita or p.equipe_visita.sigla == equipe.sigla and p.pontos_casa < p.pontos_visita:
            dados['vitorias'] += 1
    dados['derrotas'] = dados['jogos'] - (dados['vitorias'] + dados['empates'])
    dados['pontos'] +=  dados['vitorias'] * 3 + dados['empates']
    return dados

''' BANCO DADOS PARTIDAS '''
def criar_partida(partida):
    if pegar_partida(partida.equipe_casa.sigla + partida.equipe_visita.sigla) == False:
        PARTIDAS.append(partida)
        return True
    return False

def deletar_partida(id):
    i = pegar_indice_partida(id)
    if i != False or i == 0:
        del(PARTIDAS[i])
        return True
    return False

def pegar_partida(id='*'):
    if id == '*':
        return PARTIDAS
    else:
        for p in PARTIDAS:
            if p.id() == id: return p
    return False

def alterar_partida(id_anterior, partida):
    if pegar_partida(partida.id()) == False or id_anterior == partida.id():
        i = pegar_indice_partida(id_anterior)
        if i != False or i == 0:
            PARTIDAS[i] = partida
            return True
    return False

def listar_partidas_da_equipe(sigla):
    partidas = []
    for p in PARTIDAS:
        if p.equipe_casa.sigla == sigla or p.equipe_visita.sigla == sigla:
            partidas.append(p)
    return partidas

''' BANCO DADOS USUARIOS '''
def pegar_usuario(email, senha):
    user = [u for u in USUARIOS if u.email == email and u.senha == senha]
    if user: return user[0] 
    return []

#Auxiliar
def pegar_indice_partida(id):
    indice = 0
    for p in PARTIDAS:
        if p.id() == id:
            return indice
        indice += 1
    return False

def pegar_indice_equipe(sigla):
    indice = 0
    for e in EQUIPES:
        if e.sigla == sigla:
            return indice
        indice += 1
    return False