# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def dobrar (x):
    return x*2


def triplicar (x):
    return x*3


def quadruplicar (x):
    return x*4


numero_digitado = input('Número:')
operacao = input ('multiplicado por:')
operacao = int(operacao)

if operacao == 2:
    dobrar (numero_digitado)
    
elif operacao == 3:
    triplicar (numero_digitado)
    
elif operacao == 4:
    quadruplicar (numero_digitado)
    
else:
    print('inválido')