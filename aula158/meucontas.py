import abc

class Conta(abc.ABC):
    def __init__ (self,agencia,numconta):
        self.agencia = agencia
        self.numconta = numconta
        self.saldo = 0
    
    @abc.abstractmethod
    def sacar (self, dinheiro):
        self.saldo -= dinheiro
        print(f'Sacado {dinheiro}R$, Total {self.saldo}R$')
    
    def depositar (self, dinheiro):
        self.saldo += dinheiro
        print(f'Depositado {dinheiro}R$, Total {self.saldo}R$')

class ContaPoupanca (Conta):
    def sacar(self, dinheiro):
        check = self.saldo - dinheiro
        if check < 0:
            print ('Saldo insuficiente')
        else:
            return super().sacar(dinheiro)

class ContaCorrente (Conta):
    def sacar (self, dinheiro):
        check = self.saldo - dinheiro
        if check < -5000:
            print ('Excede o limite de -R$5000,00')
        else:
            return super().sacar(dinheiro)


if __name__ == '__main__':
    conta1 = ContaPoupanca(1234,56789)
    print(conta1.agencia)
    print(conta1.numconta)
    conta1.depositar(20)
    conta1.depositar(30)
    print()
    conta2 = ContaCorrente(4321,98765)
    print(conta2.agencia)
    print(conta2.numconta)
    conta2.depositar(5)
    conta2.sacar(100)
    conta2.depositar(50)
    print()

