from database.dados import *

def carregar_classe(lista):
    for objeto in lista:
        if objeto not in objeto.listar():
            objeto.__class__.criar(objeto)

def carregar(classe):
    if classe == Partida:
        carregar_classe(PARTIDAS)
    elif classe == Equipe:
        carregar_classe(EQUIPES)
    elif classe == Usuario:
        carregar_classe(USUARIOS)

#COMENTÁRIO

def calcular_pontos(Equipe):
    pontos = 0
    for p in PARTIDAS:
        if p.equipe_casa.sigla == Equipe.sigla or Equipe.sigla == p.equipe_visita.sigla:
            if p.pontos_casa == p.pontos_visita:
                pontos += 1
            elif p.equipe_casa.sigla == Equipe.sigla:
                if p.pontos_casa > p.pontos_visita:
                    pontos += 3
            elif p.equipe_visita.sigla == Equipe.sigla:
                if p.pontos_casa < p.pontos_visita:
                    pontos += 3
    return pontos