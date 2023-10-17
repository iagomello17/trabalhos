from abc import ABC, abstractmethod
import math

class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Retangulo(Forma):
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def calcular_area(self):
        return self.comprimento * self.largura

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * (self.raio ** 2)

# Exemplo de uso:
retangulo = Retangulo(5, 4)
circulo = Circulo(3)

print(f"Área do Retângulo: {retangulo.calcular_area()}")
print(f"Área do Círculo: {circulo.calcular_area()}")
