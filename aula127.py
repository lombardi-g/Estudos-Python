# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

class Celular:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo



'''
def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho_arquivo)
    return dados
'''


c1 = Celular('Samsung','S21')
c2 = Celular('Samsung','S22')
c3 = Celular('Apple','iPhone')

bd=[vars(c1), c2.__dict__, vars(c3)]

caminho_arquivo = 'aula127.json'

def salvar(caminho_arquivo):
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        json.dump(bd, arquivo, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    salvar(caminho_arquivo)