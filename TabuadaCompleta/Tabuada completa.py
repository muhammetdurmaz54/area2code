# ADIÇÃO

def adicao(num1,num2):
  res = num1 + num2
  return res
for num1 in range(1,11):
  print(f'\nTABUADA DE SOMA {num1}\n')
  for num2 in range(1,11):
    print(f'{num1} + {num2} = {adicao(num1,num2)}')

# SUBTRAÇÃO

def subtracao(num1,num2):
  res = num1 - num2
  return res
for num1 in range(1,11):
  print(f'\nTABUADA DE SUBTRAÇÃO {num1}\n')
  for num2 in range(1,11):
    print(f'{num1} - {num2} = {subtracao(num1,num2)}')

# MULTIPLICAÇÃO

def multiplicacao(num1,num2):
  res =  num1 * num2
  return res
for num1 in range(1,11):
  print(f'\nTABUADA DE MULTIPLICAÇÃO {num1}\n')
  for num2 in range(1,11):
    print(f'{num1} X {num2} = {multiplicacao(num1,num2)}')

# DIVISÃO

def divisao(num1,num2):
  res = num1 / num2
  return round(res,1)
for num1 in range(1,11):
  print(f'\nTABUADA DE DIVISÃO {num1}\n')
  for num2 in range(1,11):
    print(f'{num1} / {num2} = {divisao(num1,num2)}')