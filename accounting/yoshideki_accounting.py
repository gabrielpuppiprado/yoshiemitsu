import pandas

### template para a tabela
TEMPLATE = \
""" TEMPLATE para a tabela de banco de dados:
OBS: montar campos e valores separados por virgula ","
EXEMPLO:
campos --> emergencia,comum,yoshie,hideki,comum_topico1,comum_topico2,yoshie_topico1,hideki_topico1
valores --> 0,0,0,0,0,0,0,0
"""
###


def load_db(path):
    db = read_csv(path)

def save_db(db):
    with open() as newfile:
        newfile.write()
    db.to_csv()

CONFIGS = {}

template = {
    'emergencia': {'porcentagem': 50.0, 'linhas': False},
    'comum': {'porcentagem': 30.0, 'total': 0.0, 'linhas': {
        'topico1': {'porcentagem': 70.0, 'total': 0.0},
        
        'topico2': {'porcentagem': 20.0, 'total': 0.0},
        'topico3': {'porcentagem': 10.0, 'total': 0.0},
    }},
    'yoshie': {'porcentagem': 10.0, 'linhas': {
        'topico1': {'porcentagem': 60.0, 'total': 0.0},
        'topico2': {'porcentagem': 25.0, 'total': 0.0},
        'topico3': {'porcentagem': 15.0, 'total': 0.0},
    }},
    'hideki': {'porcentagem': 10.0, 'linhas': {
        'topico1': {'porcentagem': 65.0, 'total': 0.0},
        'topico2': {'porcentagem': 20.0, 'total': 0.0},
        'topico3': {'porcentagem': 15.0, 'total': 0.0},
    }},
}

def logica_principal():
    while True:
        try:
            novo_valor = float(input('Digite um valor para salvar: (R$): '))
            break
        except:
            print('Tente novamente um numero valido (EX: --> 99.99 <-- = R$ 99,99)')

    if novo_valor:
        diluir_proporcionalmente(novo_valor) # chamando a funcao para diluir o valor conforme as porcentagems

def diluir_proporcionalmente(valor):
    # ler dados
    # diluir valores
    # salvar tabela
    template.

if __name__ == '__main__':
    logica_principal()