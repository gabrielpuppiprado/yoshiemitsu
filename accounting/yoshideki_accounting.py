import json
import os

### template para a tabela
TEMPLATE = \
""" TEMPLATE para a tabela de banco de dados:
OBS: montar campos e valores separados por virgula ","
EXEMPLO:
campos --> emergencia,comum,yoshie,hideki,comum_topico1,comum_topico2,yoshie_topico1,hideki_topico1
valores --> 0,0,0,0,0,0,0,0
"""
###

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


def load_db(path):
    if not os.path.exists(path):
        return {}
    with open(path, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}

def save_db(db, save_on):
    with open(save_on, 'w') as newfile:
        json.dump(db, newfile, indent=4)

def diluir_proporcionalmente(valor, path='db.json'):
    # Carregar dados
    db = load_db(path)
    
    # Se não houver banco de dados salvo, usar template inicial
    if not db:
        db = {k: {'total': 0.0, 'porcentagem': v['porcentagem'], 'linhas': v.get('linhas', {})} for k, v in template.items()}
        for categoria in db.values():
            if 'linhas' in categoria and isinstance(categoria['linhas'], dict):
                for sub in categoria['linhas']:
                    categoria['linhas'][sub]['total'] = 0.0
    
    # Distribuir o valor proporcionalmente
    for categoria, dados in template.items():
        porcentagem_cat = dados['porcentagem'] / 100.0
        valor_cat = valor * porcentagem_cat
        db[categoria]['total'] += valor_cat
        
        if 'linhas' in dados and isinstance(dados['linhas'], dict):
            for subcat, subdados in dados['linhas'].items():
                porcentagem_sub = subdados['porcentagem'] / 100.0
                valor_sub = valor_cat * porcentagem_sub
                db[categoria]['linhas'][subcat]['total'] += valor_sub
    
    # Salvar novo banco de dados
    save_db(db, path)

    # Mostrar os dados salvos no banco de dados
    mostrar_resultado(db)

def mostrar_resultado(db):
    """Exibe os valores finais de cada categoria e subtópico na tela."""
    print("\n==== TABELA ATUALIZADA ====")
    for categoria, dados in db.items():
        print(f"\n[{categoria.upper()}] - Total: R$ {dados['total']:.2f} ({dados['porcentagem']}%)")
        if 'linhas' in dados and isinstance(dados['linhas'], dict):
            for sub, subdados in dados['linhas'].items():
                print(f"  └── {sub}: R$ {subdados['total']:.2f} ({subdados['porcentagem']}%)")

def logica_principal():
    while True:
        try:
            novo_valor = float(input('Digite um valor para salvar: (R$): '))
            break
        except:
            print('Tente novamente um numero valido (EX: --> 99.99 <-- = R$ 99,99)')

    if novo_valor:
        diluir_proporcionalmente(novo_valor) # chamando a funcao para diluir o valor conforme as porcentagems

if __name__ == '__main__':
    logica_principal()