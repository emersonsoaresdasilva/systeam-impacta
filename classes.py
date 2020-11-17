class Usuario(object):

    def __init__(self, email='', senha=''):
        self.email = email
        self.senha = senha

    def __str__(self):
        return f'{self.email}'


class Equipe(object):

    def __init__(self, nome='', sigla='', local=''):
        self.nome = nome
        self.sigla = sigla
        self.local = local

    def __str__(self):
        return f'{self.nome} ({self.sigla})'


class Partida(object):

    def __init__(self, equipe_casa, equipe_visita, pontos_casa,  pontos_visita):
        self.equipe_casa = equipe_casa
        self.equipe_visita = equipe_visita
        self.pontos_casa = pontos_casa
        self.pontos_visita = pontos_visita

    def __str__(self):
        return f'{self.equipe_casa} ({self.pontos_casa}) - {self.equipe_visita} ({self.pontos_visita})'

    def vencedor(self):
        if self.pontos_casa > self.pontos_visita:
            return self.equipe_casa
        elif self.pontos_visita > self.pontos_casa:
            return self.equipe_visita
        return False

    def id(self):
        return (self.equipe_casa.sigla+self.equipe_visita.sigla)

    def trocar_equipe(self, sigla_anterior, equipe):
        if self.equipe_casa.sigla == sigla_anterior:
            self.equipe_casa = equipe
        elif self.equipe_visita.sigla == sigla_anterior:
            self.equipe_visita = equipe
