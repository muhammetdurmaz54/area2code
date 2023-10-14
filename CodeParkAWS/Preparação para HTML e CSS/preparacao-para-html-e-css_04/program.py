lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 
                  'loções', 'xampus', 'sabonetes', 'delineadores']

lista_produtos[1], lista_produtos[4] = 'rímel', 'cremes hidratantes'
lista_produtos.append('alisantes')
lista_produtos.append('neutralizantes')
lista_produtos.pop(7)

for x in range(len(lista_produtos)):
  print(f'Temos {lista_produtos[x]} à venda!')