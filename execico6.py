class Veiculo:
    def __init__(self, tipo):
        self.tipo = tipo


    def descricao(self):
        print(f"Este é um veículo do tipo {self.tipo}.")

class Carro(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__('Carro')
        self.marca = marca
        self.modelo = modelo

    def descricao(self):
        print(f"Este é um carro da marca {self.marca}, modelo {self.modelo}.")



class Moto(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__('Moto')
        self.marca = marca
        self.modelo = modelo

    def descricao(self):
        print(f"Esta é uma moto da marca {self.marca}, modelo {self.modelo}.")

    

# Cria uma lista de objetos Veiculo contendo instâncias de Carro e Moto
veiculos = [
    Carro("Toyota", "Corolla"),
    Moto("Honda", "CBR600"),
    Carro("Ford", "Focus"),
    Moto("Yamaha", "YZF-R6")
]

# Itera sobre a lista e chama o método descricao() para cada objeto
for veiculo in veiculos:
    veiculo.descricao()
