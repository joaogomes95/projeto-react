class Pessoa:
    # Métudo construtor/inicializador de atributos.
    def __init__(self, nome, idade, peso):
        self.nomePessoa = nome
        self.idadePessoa = idade
        self.pesoPessoa = peso

    def comer(self, calorias):
        if self.idadePessoa > 30:
            dobro = calorias * 2
            self.pesoPessoa += dobro
            self.pesoPessoa += calorias
        else:
            self.pesoPessoa += calorias

    def malhar(self, calorias):
        if self.idadePessoa < 30:
            self.pesoPessoa -= calorias*2

    def mostrarDados(self):
        return f'''
        Nome = {self.nomePessoa}
        Idade = {self.idadePessoa}
        Peso = {self.pesoPessoa}        
        '''


pessoa1 = Pessoa('João', 26, 88.5)
pessoa2 = Pessoa('Francis', 41, 92.5)

pessoa2.malhar(5)
pessoa1.malhar(2)

# Crie uma classe chamada Conta para simular as operações de uma conta corrente.
# Sua classe deverá ter os atributos Titular e Saldo, e os métodos Sacar e Depositar.
# Crie um objeto da classe Conta e teste os atributos e métodos implementados.​
# Adicione uma regra no método Sacar, onde o usuário só poderá sacar se o Saldo for maior que zero, caso contrário mostre a mensagem na tela: "Você não tem saldo suficiente para essa operação."
