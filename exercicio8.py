from abc import ABC, abstractmethod

class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self):
        pass

class Carro(Imprimivel):
    def __init__(self, marca, modelo, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = velocidade

    def imprimir(self):
        print(f"Carro: {self.marca} {self.modelo}, Velocidade: {self.velocidade} km/h")

class Moto(Imprimivel):
    def __init__(self, marca, modelo, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = velocidade

    def imprimir(self):
        print(f"Moto: {self.marca} {self.modelo}, Velocidade: {self.velocidade} km/h")

carro = Carro("Toyota", "Corolla", 120)
moto = Moto("Honda", "CBR600", 160)

carro.imprimir()
moto.imprimir()
