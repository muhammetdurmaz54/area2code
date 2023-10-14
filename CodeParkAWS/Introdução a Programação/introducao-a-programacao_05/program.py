def calc(x,op,y):
  if op == 1:
    res = x + y
  elif op == 2:
    res = x - y
  elif op == 3:
    res = x * y
  elif op == 4:
    res = x / y
  return res

while True:
  print(f'1. SOMA\n2. SUBTRAÇÃO\n3. MULTIPLICAÇÃO\n4. DIVISÃO\n0. SAIR')
  op = int(input("Hora do calculo XD escolha qual a operação: "))
  if op > 4:
    print(f'Essa opção não existe x-x')
  elif op == 0:
    print(f'Operação Finalizada! :)')
    break
  else:
    x = int(input())
    y = int(input())
    print("Resultado: ", calc(x,op,y))