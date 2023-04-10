'''
Faça uma lista de compras com listas
O usuário deve ter a possiblidade de inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com índices inexistentes.
'''

lista_de_compras = list()
while True:
    print('Selecione uma opção:')
    entrada = input('[i]nserir [a]pagar [l]istar ')


    if entrada == 'l':
        for i,valor in enumerate(lista_de_compras):
            print(i,valor)
    
    elif entrada =='i':
        novo_item=input('Insira o item na lista de compras:')
        lista_de_compras.append(novo_item)


    elif entrada == 'a':
        apagar=input('Digite o número do item que deseja apagar')
        if apagar not in enumerate(lista_de_compras):
            print ('Não tem',apagar,'itens na lista.')
            continue
        lista_de_compras=lista_de_compras.remove(apagar)
    else:
        print('Inválido.')



