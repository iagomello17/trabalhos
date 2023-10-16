class Carro:
    def __init__(self, modelo, ano):
        self._modelo = modelo
        self._ano = ano

    def get_modelo(self):
        return self._modelo

    def get_ano(self):
        return self._ano

meu_carro = Carro("DODGE RAM", 2020)

print("Modelo:", meu_carro.get_modelo())
print("Ano:", meu_carro.get_ano())

