# ESSE CODIGO NÃO FUNCIONA 💀

quantidadeDeRodas = int
pesoBruto = float
quantidadeDePessoasNoVeiculo = int

print("Quantidade de Rodas:")
quantidadeDeRodas = input()
print("Quantidade de pessoas no veiculo:")
quantidadeDePessoasNoVeiculo = input()
print("Peso bruto em quilogramas:")
pesoBruto = input()

if (quantidadeDeRodas <= 3):
  print("Carteira A")
elif (quantidadeDeRodas == 4) and (quantidadeDePessoasNoVeiculo <= 8) and (pesoBruto <= 3500):
  print("Carteira B")
elif (pesoBruto >= 3500) and (pesoBruto <= 6000):
 print("Carteira C")
elif (quantidadeDePessoasNoVeiculo > 8):
  print("Carteira D")
elif (pesoBruto > 6000):
  print("Carteura E")

# EDIT: 01
# Codigo funcionando ✔
# OBS: Essa questão é estranha!

quantidadeDeRodas = int
pesoBruto = float
quantidadeDePessoasNoVeiculo = int

print("Quantidade de Rodas:")
quantidadeDeRodas = int(input())
print("Quantidade de pessoas no veiculo:")
quantidadeDePessoasNoVeiculo = int(input())
print("Peso bruto em quilogramas:")
pesoBruto = float(input())

if (quantidadeDeRodas <= 3):
  print("Carteira A")
elif (quantidadeDeRodas == 4) and (quantidadeDePessoasNoVeiculo <= 8) and (pesoBruto <= 3500):
  print("Carteira B")
elif (pesoBruto >= 3500) and (pesoBruto <= 6000):
 print("Carteira C")
elif (quantidadeDePessoasNoVeiculo > 8):
  print("Carteira D")
elif (pesoBruto > 6000):
  print("Carteura E")