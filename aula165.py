# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

montante = 0
total = 1000000
parcela = 1000000/(5*12)
# print(parcela)
init_date = datetime.strptime('20/12/2020', '%d/%m/%Y')
final_date = datetime.strptime('20/12/2025', '%d/%m/%Y')
delta = 1
montante = 16666
print(init_date)
contador = 1
while montante <= 1000000:
    print('Parcela',contador)
    print(init_date+relativedelta(months=delta))
    print(f'Parcela: R$ {parcela:.2f}')
    print(f'Montante: R$ {montante:.2f}')
    print()
    montante += parcela
    contador += 1
    delta += 1