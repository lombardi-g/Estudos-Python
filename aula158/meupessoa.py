import meucontas

class Pessoa:
    def __init__ (self):
        self._nome=None
        self._idade=None
    
    @property
    def nome (self):
        return self._nome

    @nome.setter
    def nome (self, primeironome):
        self._nome = primeironome

    @property
    def idade (self):
        return self._idade

    @idade.setter
    def idade (self, anos):
        self._idade = anos

class Cliente (Pessoa):
    def __init__(self,nome,idade):
        super().__init__(nome,idade)
        self.conta: meucontas.Conta


if __name__ == '__main__':
    p1=Pessoa
    p1.nome='Astolfo'
    p1.idade=67
    # p2=Pessoa('Benildo',75)
    # p3=Pessoa('Cromilda',52)
    print(p1.nome)
    print(p1.idade)
    conta1 = meucontas.ContaPoupanca(1234,56789)
    p1.conta = conta1
    print(conta1.agencia)
    print(conta1.numconta)
    conta1.depositar(20)
    conta1.depositar(30)
    print(p1.nome)
