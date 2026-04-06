class Pessoa:
    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.idade = idade
        self.altura = altura

    def apresentar(self):
        print(f"Olá, meu nome é {self.__nome}, tenho {self.idade} anos e minha altura é:{self.altura} m.")
#Uso:
pessoa1 = Pessoa("Cristiano", 35, 1.92)
pessoa1 = Pessoa("Daniel", 35, 1.92)

pessoa1.apresentar()