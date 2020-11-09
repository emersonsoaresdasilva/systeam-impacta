class Usuario(object):

    __dados = []

    def __init__(self, email='', senha=''):
        self.email = email
        self.senha = senha

    def __str__(self):
        return f'{self.email}'
    
    @classmethod
    def criar(cls, usuario):
        cls.__dados.append(usuario)

    @classmethod
    def listar(cls):
        return cls.__dados



class Equipe(object):

    __dados = []

    def __init__(self, nome='', sigla='', local=''):
        self.nome = nome
        self.sigla = sigla
        self.local = local

    def __str__(self):
        return f'{self.nome} ({self.sigla})'

    @classmethod
    def criar(cls, equipe):
        cls.__dados.append(equipe)

    @classmethod
    def listar(cls):
        return cls.__dados



class Partida(object):

    __dados = []

    def __init__(self, equipe_casa, equipe_visita, pontos_casa,  pontos_visita):
        self.equipe_casa = equipe_casa
        self.equipe_visita = equipe_visita
        self.pontos_casa = pontos_casa
        self.pontos_visita = pontos_visita

    def __str__(self):
        return f'{self.equipe_casa} ({self.pontos_casa}) - {self.equipe_visita} ({self.pontos_visita})'

    @classmethod
    def criar(cls, partida):
        cls.__dados.append(partida)

    @classmethod
    def listar(cls):
        return cls.__dados

    @classmethod
    def listar_da_equipe(cls, Equipe):
        partidas = []
        for p in cls.__dados:
            if p.equipe_casa == Equipe or p.equipe_visita == Equipe:
                partidas.append(p)
        return partidas