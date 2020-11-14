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
    def classificar(cls, dados):
        pontos = []
        vitorias = []
        equipes = []
       
        # Listando equipes e pontos (list).
        for dado in dados:
            equipes.append(dado)
            pontos.append(dados[dado]['pontos'])
            vitorias.append(dados[dado]['vitorias'])
        
        #Ordenando dados por critérios
        for criterio in [vitorias, pontos]:
            ordenacoes = cls.ordernar_por(criterio, equipes, pontos, vitorias)
            equipes = ordenacoes[0]
            pontos = ordenacoes[1]
            vitorias = ordenacoes[2]

        # Retornando os dados ordenados.
        dados_ordenados = {}
        count = 1
        for sigla in equipes:
            dados_ordenados[sigla] = dados[sigla]
            dados_ordenados[sigla]['posicao'] = count
            count += 1
        return dados_ordenados

    @classmethod
    def ordernar_por(cls, criterio, equipes, pontos, vitorias):
        indices_ordenados = []
        for _ in range(len(criterio)):
            i = criterio.index(max(criterio)) #Índice do maior 'criterio' na lista.
            indices_ordenados.append(i)
            criterio[i] = -1
        
        equipes_ordenadas = cls.ordernar_lista_por_indice(indices_ordenados, equipes, equipes == criterio)
        pontos_ordenados  = cls.ordernar_lista_por_indice(indices_ordenados, pontos, pontos == criterio)
        vitorias_ordenadas  = cls.ordernar_lista_por_indice(indices_ordenados, vitorias, vitorias == criterio)

        return [equipes_ordenadas, pontos_ordenados,  vitorias_ordenadas]

    @classmethod
    def ordernar_lista_por_indice(cls, indices, lista, is_criterio):
        lista_ordenada = []
        if is_criterio: return lista
        for i in indices:
            lista_ordenada.append(lista[i])
        return lista_ordenada



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
