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
        vitorias = []
        empates = []
        equipes = []
        # Listando equipes e pontos (list).
        for dado in dados:
            equipes.append(dado)
            pontos.append(dados[dado]['pontos'])
            vitorias.append(dados[dado]['vitorias'])
            empates.append(dados[dado]['empates'])

        ordenacoes = cls.ordernar_por(vitorias, equipes, pontos, vitorias, empates)
        equipes = ordenacoes[0]
        pontos = ordenacoes[1]
        vitorias = ordenacoes[2]
        empates = ordenacoes[3]

        ordenacoes = cls.ordernar_por(pontos, equipes, pontos, vitorias, empates)
        equipes = ordenacoes[0]
        pontos = ordenacoes[1]
        vitorias = ordenacoes[2]
        empates = ordenacoes[3]

        #TRATAMENTO FINAL
        # Retornando os dados ordenados.
        dados_ordenados = {}
        count = 1
        for sigla in equipes:
            dados_ordenados[sigla] = dados[sigla]
            dados_ordenados[sigla]['posicao'] = count
            count += 1
        print(dados_ordenados)
        return dados_ordenados

    @classmethod
    def ordernar_por(cls, criterio, equipes, pontos, vitorias, empates):
        indices_ordenados = []
        for _ in range(len(criterio)):
            i = criterio.index(max(criterio)) #Índice do maior 'criterio' na lista.
            indices_ordenados.append(i)
            criterio[i] = -1
        
        equipes_ordenadas = []
        for i in  indices_ordenados:
            equipes_ordenadas.append(equipes[i])

        if criterio != pontos:
            pontos_ordenados = []
            for i in  indices_ordenados:
                pontos_ordenados.append(pontos[i])
        else:
            pontos_ordenados = pontos

        if criterio != vitorias:
            vitorias_ordenadas = []
            for i in  indices_ordenados:
                vitorias_ordenadas.append(vitorias[i])
        else:
            vitorias_ordenadas = vitorias

        if criterio != empates:
            empates_ordenados = []
            for i in  indices_ordenados:
                empates_ordenados.append(empates[i])
        else:
            empates_ordenados = empates

        return [equipes_ordenadas, pontos_ordenados,  vitorias_ordenadas, empates_ordenados]





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
