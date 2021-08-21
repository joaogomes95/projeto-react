class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        if self.saldo == 0:
            return f'''
            Titular:{self.titular}
            '''
        else:
            return f'''
            Titular: {self.titular}
            Saldo: {self.saldo}
            '''

    def depositar(self, valor):
        self.saldo += valor
        return f'{self.titular} seu saldo atual é {self.saldo}'

    def sacar(self, valor):
        if valor > 0:
            if self.saldo < valor:
                print(f'{self.titular} você não tem {valor:.f} para sacar. ')
                self.extrato()
            else:
                print('Você não pode sacar 0 reais!')
