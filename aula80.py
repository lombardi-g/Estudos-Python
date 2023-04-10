"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],#teste aqui
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]


'''
for digito in lista_de_listas_de_inteiros[5]:
    primeira_posicao=0

    vezes_que_aparece = lista_de_listas_de_inteiros[5].count(digito)
    if vezes_que_aparece ==1:
        continue
    else:
        print(digito)
        primeira_posicao = lista_de_listas_de_inteiros[5].index(digito)
        distancia = lista_de_listas_de_inteiros[5][primeira_posicao+1::].index(digito)
        resultado_final=distancia if d
        print ('dist',distancia)
        # resultado_final=distancia if dis
        # print (resultado_final)
'''


# minha solução:
'''
def verificar_unicos(lista_de_dentro):
    set1 = set(lista_de_dentro)
    if len(lista_de_dentro) == len(set1):
        return -1


    
for listas in lista_de_listas_de_inteiros:
    resultado=verificar_unicos(listas)
    if resultado == -1:
        print(listas,resultado)
    else:
        maior_distancia=10
        for digito in listas:
            vezes_que_aparece = listas.count(digito)
            if vezes_que_aparece ==1:
                continue
            else:
                for digito in listas:
                    primeira_posicao=0

                    vezes_que_aparece = listas.count(digito)
                    if vezes_que_aparece ==1:
                        continue
                    else:
                        primeira_posicao = listas.index(digito)
                        distancia = listas[primeira_posicao+1::].index(digito)
                        if distancia<maior_distancia:
                            maior_distancia=distancia
                            resultado_final=digito
        print(listas,resultado_final)
'''

# solução do prof


def encontra_primeiro_duplicado(lista_de_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in lista_de_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break

        numeros_checados.add(numero)

    return primeiro_duplicado


for lista in lista_de_listas_de_inteiros:
    print(
        lista,
        encontra_primeiro_duplicado(lista)
    )