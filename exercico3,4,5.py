class Veiculo:
    def __init__(self, tipo, velocidade):
        self.tipo = tipo
        self.velocidade = velocidade

    def acelerar(self, valor):
        self.velocidade += valor

    def descricao(self):
        print(f"Este é um veículo do tipo {self.tipo} com velocidade de {self.velocidade} km/h.")

class Carro(Veiculo):
    def __init__(self, marca, modelo, velocidade):
        super().__init__('Carro', velocidade)
        self.marca = marca
        self.modelo = modelo

    def descricao(self):
        print(f"Este é um carro da marca {self.marca}, modelo {self.modelo} com velocidade de {self.velocidade} km/h.")

    def buzinar(self):
        print(f"{self.marca} {self.modelo} está buzinando!")

class Moto(Veiculo):
    def __init__(self, marca, modelo, velocidade):
        super().__init__('Moto', velocidade)
        self.marca = marca
        self.modelo = modelo

    def descricao(self):
        print(f"Esta é uma moto da marca {self.marca}, modelo {self.modelo} com velocidade de {self.velocidade} km/h.")

    def empinar(self):
        print(f"{self.marca} {self.modelo} está empinando!")

carro = Carro("Honda", "Civic", 120)
moto = Moto("Honda", "CBR1000", 160)

carro.descricao()
carro.acelerar(30)
print(f"Nova velocidade do carro: {carro.velocidade}")
carro.buzinar()

moto.descricao()
moto.acelerar(20)
print(f"Nova velocidade da moto: {moto.velocidade}")
moto.empinar()
