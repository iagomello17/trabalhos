class Carro:
    def __init__(self, modelo, ano):
        self.__modelo = modelo
        self.__ano = ano

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, novo_modelo):
        self.__modelo = novo_modelo

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, novo_ano):
        self.__ano = novo_ano

meu_carro = Carro("DODGE RAM", 2020)

print("Modelo:", meu_carro.modelo)
print("Ano:", meu_carro.ano)

meu_carro.modelo = "Ford Mustang"
meu_carro.ano = 2022

print("Novo Modelo:", meu_carro.modelo)
print("Novo Ano:", meu_carro.ano)

