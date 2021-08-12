from hbomax import Hbomax


class Serie(Hbomax):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.__temporadas = temporadas

    @property
    def temporadas(self):
        return self.__temporadas

    def __str__(self):
        return f'''
        Nome: {self.nome}
        Ano: {self.ano}
        Temporadas: {self.temporadas}
        Likes: {self.likes}      
        '''
