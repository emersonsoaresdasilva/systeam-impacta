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

    @classmethod
    def ordenar_por_pontos(cls, dados):
        pontos = []
        equipes = []
        pontos_ordenados = []

        # Listando equipes e pontos (list).
        for dado in dados:
            equipes.append(dado)
            pontos.append(dados[dado]['pontos'])

        # Ordenação de pontos.
        for _ in range(len(pontos)):
            i = pontos.index(max(pontos))  # Maior pontos na lista.
            if len(pontos_ordenados) > 0:
                if pontos_ordenados[-1] != pontos[i]:
                    pontos_ordenados.append(i)
            else:
                pontos_ordenados.append(i)
            pontos[i] = 0

        # Ordenação de equipes.
        equipes_pontos = []

        for pontos in pontos_ordenados:
            equipes_pontos.append(equipes[pontos])

        # Retornando os dados ordenados.
        dados_ordenados = {}
        for sigla in equipes_pontos:
            dados_ordenados[sigla] = dados[sigla]
        return dados_ordenados

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
