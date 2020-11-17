from classes import Equipe, Partida, Usuario

EQUIPES = [
    Equipe('Corinthians', 'COR', 'São Paulo-SP'),
    Equipe('São Paulo', 'SAO', 'São Paulo-SP'),
    Equipe('Santos', 'SAN', 'São Paulo-SP'),
    Equipe('Palmeiras', 'PAL', 'São Paulo-SP'),
    Equipe('Fluminense', 'FLU', 'Rio de Janeiro-RJ'),
    Equipe('Vasco', 'VAS', 'Rio de Janeiro-RJ'),
    Equipe('Botafogo', 'BOT', 'Rio de Janeiro-RJ'),
    Equipe('Flamengo', 'FLA', 'Rio de Janeiro-RJ')  
]
PARTIDAS = [
    Partida(EQUIPES[0], EQUIPES[1], 1, 0),
    Partida(EQUIPES[1], EQUIPES[0], 2, 5),
    Partida(EQUIPES[0], EQUIPES[2], 1, 3),
    Partida(EQUIPES[2], EQUIPES[0], 5, 3),
    Partida(EQUIPES[0], EQUIPES[3], 5, 2),
    Partida(EQUIPES[3], EQUIPES[0], 5, 3),
    Partida(EQUIPES[0], EQUIPES[4], 3, 5),
    Partida(EQUIPES[4], EQUIPES[0], 3, 1),
    Partida(EQUIPES[5], EQUIPES[2], 0, 0),
    Partida(EQUIPES[6], EQUIPES[2], 3, 3),
    Partida(EQUIPES[7], EQUIPES[2], 1, 1)
]

USUARIOS = [
    Usuario('admin@admin.com', 'admin123*')
]