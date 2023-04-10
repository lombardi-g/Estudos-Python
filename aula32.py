"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero=input('Digite um número inteiro que eu te digo se é par ou ímpar:')

try:
    numero_int=int(numero)
    if numero_int%2 ==0:
            print(f'O número {numero_int} é par')
    else:
            print(f'O número {numero_int} é ímpar')


except:
    print('Eu disse inteiro, jumento')

print('')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora_digitada=input('Digite a hora atual em número inteiro:')

try:
    hora_atual=int(hora_digitada)
    hora_de_bom_dia=hora_atual>=0 and hora_atual <=11
    hora_de_boa_tarde=hora_atual>11 and hora_atual<=17
    hora_de_boa_noite=hora_atual >17 and hora_atual<=24
    hora_negativa=hora_atual<0
    hora_inexistente=hora_atual>24

    if hora_de_bom_dia:
        print('Bom dia!')
    if hora_de_boa_tarde:
        print('Boa Tarde!')
    if hora_de_boa_noite:
        print('Boa Noite!')
    if hora_negativa:
        print('Hora negativa?')
    if hora_inexistente:
        print('O dia tem 24h.')



except:
    print('Eu disse número inteiro, jegue')

print('')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome_digitado=input('Digite seu nome:')

try:
    nome_a_analisar=str(nome_digitado)
    nome_curto=len(nome_a_analisar)<=4
    nome_medio=len(nome_a_analisar)>4 and len(nome_a_analisar)<=6
    nome_grande=len(nome_a_analisar)>6
    
    if nome_curto:
        print('Seu nome é curto')
    if nome_medio:
        print('Seu nome é normal')
    if nome_grande:
        print('Seu nome é muito grande')


except:
    print('Isso não é um nome.')
print('')