from hbomax import Hbomax


class Filme(Hbomax):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.__duracao = duracao

    @property
    def duracao(self):
        return self.__duracao

    def __str__(self):
        return f'''
        Nome: {self.nome}
        Ano: {self.ano}
        Duração: {self.duracao}
        Likes: {self.likes}      
        '''
