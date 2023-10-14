def calculadora(num1,op,num2):
  if op == 1:
    res = num1 + num2
  elif op == 2:
    res = num1 - num2
  elif op == 3:
    res = num1 * num2
  elif op == 4:
    res = num1 / num2
  else:
    res = 0
  return res

num1=int(input("primeiro numero: "))
op=int(input("operação: "))
num2=int(input("segundo numero: "))

#Substitua os valores "num1,op,num2" por numeros pra realizar a operação ou descomente os inputs acima.
res = calculadora(num1,op,num2)

print(res)