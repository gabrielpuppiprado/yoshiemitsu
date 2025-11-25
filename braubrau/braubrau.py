# TODO 1600g de massa final em cada forma grande.
#  o bolo cresceu demais, pode ter sido a bicarbonato de sodio ou o forno da cozinha
#  e a massa ficou grande nas laterais e fina no meio
# TODO 1315g de massa final em cada forma grande.
#  aconteceu a mesma coisa, só que a as laterais ficaram finas iguais ao meio

# essa receita funciona para 2 da forma grande (45x25?)
# ou 5 da forma pequena (20x20)
# peguei a receita e achei o valor para cada forma.
sugar = 1050 # (g)
egg = 15 # (un)
butter = 650 # (g)
chocolate = 600 # (g)
salt = 5 # (g)
coffee = 5 # (g)
cacao = 200 # (g)
baking_soda = 5 # (g)
wheat = 300 # (g)

while True:
    try:
        qty_para_fazer_grande = int(input('Digite a quantidade de formas GRANDE(s): '))
        break
    except Exception as exc:
        print('Precisa ser um número inteiro!')

qty_grande = 2
forma_grande = {
    'sugar': (sugar / qty_grande) * qty_para_fazer_grande,
    'egg': (egg / qty_grande) * qty_para_fazer_grande,
    'butter': (butter / qty_grande) * qty_para_fazer_grande,
    'chocolate': (chocolate / qty_grande) * qty_para_fazer_grande,
    'salt': (salt / qty_grande) * qty_para_fazer_grande,
    'coffee': (coffee / qty_grande) * qty_para_fazer_grande,
    'cacao': (cacao / qty_grande) * qty_para_fazer_grande,
    'baking_soda': (baking_soda / qty_grande) * qty_para_fazer_grande,
    'wheat': (wheat / qty_grande) * qty_para_fazer_grande
}

while True:
    try:
        qty_para_fazer_pequena = int(input('Digite a quantidade de formas PEQUENA(s): '))
        break
    except Exception as exc:
        print('Precisa ser um número inteiro!')

qty_pequena = 5
forma_pequena = {
    'sugar': (sugar / qty_pequena) * qty_para_fazer_pequena,
    'egg': (egg / qty_pequena) * qty_para_fazer_pequena,
    'butter': (butter / qty_pequena) * qty_para_fazer_pequena,
    'chocolate': (chocolate / qty_pequena) * qty_para_fazer_pequena,
    'salt': (salt / qty_pequena) * qty_para_fazer_pequena,
    'coffee': (coffee / qty_pequena) * qty_para_fazer_pequena,
    'cacao': (cacao / qty_pequena) * qty_para_fazer_pequena,
    'baking_soda': (baking_soda / qty_pequena) * qty_para_fazer_pequena,
    'wheat': (wheat / qty_pequena) * qty_para_fazer_pequena
}
from pprint import pprint
# pprint(forma_grande, indent=4)
# pprint(forma_pequena, indent=4)

if qty_para_fazer_grande > 0:
    print(f'\nFORMA GRANDE ({qty_para_fazer_grande} formas):\n' + '\n'.join([f'{x}: {y}' for x, y in forma_grande.items()]))

if qty_para_fazer_pequena> 0:
    print(f'\nFORMA PEQUENA ({qty_para_fazer_pequena} formas):\n' + '\n'.join([f'{x}: {y}' for x, y in forma_pequena.items()]))
