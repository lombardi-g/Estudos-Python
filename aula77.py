# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos=0


for todas in perguntas:
    print(todas['Pergunta'])
    for alternativas in todas['Opções']:
        
        print(alternativas)

    print('')
    resposta = input('Digite a resposta:')
    print('')
    if resposta==todas['Resposta']:
        print('Acertou!')
        print()
        acertos+=1
    else:
        print('Errou')
        print()

print(f'Você acertou',acertos,'de 3 perguntas')
print()