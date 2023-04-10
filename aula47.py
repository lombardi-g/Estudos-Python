"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
print('Palavra Secreta')

palavra_secreta = 'marquinhos'

print(f'Adivinhe a palavra de',len(palavra_secreta),'letras')

palavra_armazenada = str('*'*len(palavra_secreta))

print(palavra_armazenada)

qtde_tentativas = 0

letra_tratada=None

i=1

j=int('0')

while True:
    letra_digitada=input('Digite uma letra minúscula:')

    if len(letra_digitada)>1:
        print('Apenas uma letra.')
        print('')
        continue

    if letra_digitada.isnumeric():
        print('Números não.')
        print('')
        continue

    if letra_digitada.isspace():
        print('Sem valor inserido')
        print('')
        continue

    
    letra_tratada=letra_digitada.lower()

    posicao = palavra_secreta.find(letra_tratada)

    if posicao == -1:
        print(palavra_armazenada)
        print('')
        qtde_tentativas += 1
        print('Tentativas :',qtde_tentativas)
        print('')
        continue
    
    j=0
    while j <= len(palavra_secreta):
        if j == posicao:
            palavra_armazenada = palavra_armazenada[:j] + letra_tratada + palavra_armazenada[j+1:len(palavra_secreta):]
        j+=1
    posicao = None


    print(palavra_armazenada)
    print('')

    qtde_tentativas += 1
    print('Tentativas :',qtde_tentativas)
    print('')
    if '*' not in palavra_armazenada:
        break

print('Você descobriu a palavra, com ',qtde_tentativas, 'tentativas.')
print('')

    
'''
palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0
'''