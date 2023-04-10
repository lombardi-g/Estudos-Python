nome='Gabriel'
altura=1.7934
peso=79.6

imc=peso/(altura**2)

#f-strings
linha_1=f'{nome} tem {altura:.2f} de altura'#dois pontos, depois ponto e quantas casas decimais se quer
linha_2=f'pesa {peso} kg e seu imc é'
linha_3=f'{imc:.3f}'

print(linha_1)
print(linha_2,linha_3)
