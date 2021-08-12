
# Isso serve para garantir que o código desse arquivo só será executado no arquivo principal
# if __name__ == '__main__':
#     pass
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


if __name__ == '__main__':

    banco = list()

    while True:
        conta = Conta(input('Titular da conta: '))
        banco.append(conta)

        resp = input('Deseja continuar: [S/N]:').upper().strip()[0]
        if resp == 'N':
            break

    print(banco[1].depositar(50))

    for o in banco:
        print(o)
