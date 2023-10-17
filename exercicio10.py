from abc import ABC, abstractmethod

class Personagem(ABC):
    def __init__(self, nome, hp):
        self.nome = nome
        self.__hp = hp

    @property
    def hp(self):
        return self.__hp

    @abstractmethod
    def ataque(self):
        pass

class Guerreiro(Personagem):
    def ataque(self):
        return f"{self.nome}, o Guerreiro, desfere um golpe de espada!"

class Mago(Personagem):
    def ataque(self):
        return f"{self.nome}, o Mago, lança uma bola de fogo!"

class Arqueiro(Personagem):
    def ataque(self):
        return f"{self.nome}, o Arqueiro, atira uma flecha certeira!"

def batalha(personagem1, personagem2):
    while personagem1.hp > 0 and personagem2.hp > 0:
        print(f"{personagem1.nome} ({personagem1.__class__.__name__}, HP: {personagem1.hp}) ataca {personagem2.nome} ({personagem2.__class__.__name__}, HP: {personagem2.hp}):")
        print(personagem1.ataque())
        personagem2._Personagem__hp -= 10
        print(f"{personagem2.nome} agora tem {personagem2.hp} HP.\n")

        if personagem2.hp <= 0:
            print(f"{personagem2.nome} foi derrotado!")

guerreiro = Guerreiro("Conan", 100)
mago = Mago("Merlin", 80)
arqueiro = Arqueiro("Legolas", 90)

batalha(guerreiro, mago)
