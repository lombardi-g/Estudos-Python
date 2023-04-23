from aula127 import caminho_arquivo, Celular
import json

with open(caminho_arquivo, 'r')as arquivo:
    data = json.load(arquivo)
    c1 = Celular(**data[0])
    c2 = Celular(**data[1])
    c3 = Celular(**data[2])

    print(c1.marca,c1.modelo)
    print(c2.marca,c2.modelo)
    print(c3.marca,c3.modelo)

