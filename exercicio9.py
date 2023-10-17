from abc import ABC, abstractmethod

class ContaBancaria(ABC):
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def __str__(self):
        pass

class ContaCorrente(ContaBancaria):
    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self._saldo -= valor
            print(f"Saque de R${valor} efetuado na conta corrente de {self.titular}")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor} efetuado na conta corrente de {self.titular}")
        else:
            print("Valor de depósito inválido.")

    def __str__(self):
        return f"Conta Corrente de {self.titular}: Saldo R${self.saldo}"

class ContaPoupanca(ContaBancaria):
    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self._saldo -= valor
            print(f"Saque de R${valor} efetuado na conta poupança de {self.titular}")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor} efetuado na conta poupança de {self.titular}")
        else:
            print("Valor de depósito inválido.")

    def __str__(self):
        return f"Conta Poupança de {self.titular}: Saldo R${self.saldo}"

conta_corrente = ContaCorrente("João")
conta_poupanca = ContaPoupanca("Maria")

print(conta_corrente)
conta_corrente.depositar(1000)
conta_corrente.sacar(500)
print(conta_corrente)

print(conta_poupanca)
conta_poupanca.depositar(500)
conta_poupanca.sacar(300)
print(conta_poupanca)
