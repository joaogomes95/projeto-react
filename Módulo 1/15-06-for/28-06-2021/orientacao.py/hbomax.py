class Hbomax:
    def __init__(self, nome, ano):
        self.__nome = nome
        self.__ano = ano
        self.__like = 0

    @property
    def nome(self):
        return self.__nome

    @property
    def ano(self):
        return self.__like

    @property
    def like(self):
        return self.__like

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def dar_like(self, nome):
        self.__like += 1
