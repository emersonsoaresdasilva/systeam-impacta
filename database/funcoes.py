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