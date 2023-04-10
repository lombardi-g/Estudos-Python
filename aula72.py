# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica (*args):
    valor=1
    for i in args:
        valor*= i
    return(valor)

final=multiplica(30,2,3)
print(final)
# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def parimpar (x):
    conta=x%2==0
    return(conta)
    


final_2=parimpar(29)
print('par') if final_2 else print('ímpar')