primeiro_valor = input('Digite um valor:')
segundo_valor = input('Digite outro valor:')

num_primeiro_valor=(int(primeiro_valor))
num_segundo_valor=(int(segundo_valor))

if num_primeiro_valor>num_segundo_valor :
    print(f'O número {num_primeiro_valor} é maior que o número {num_segundo_valor}')

elif num_segundo_valor>num_primeiro_valor :
    print(f'O número {num_segundo_valor} é maior que o número {num_primeiro_valor}')

else: print('Os dois números são iguais')