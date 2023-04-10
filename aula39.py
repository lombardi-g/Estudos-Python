"""
Iterando strings com while
"""
#       012345678910
nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321
tamanho_nome = len(nome)

passo = 0
novo_nome=''

while passo<tamanho_nome:
    letra = f'{nome[passo]}'
    novo_nome += f'*{letra}'    
    passo += 1


print(novo_nome,'*')
