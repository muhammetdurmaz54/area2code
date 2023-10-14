while True:
  try:
    nome = str(input("Digite seu nome completo: "))
    ano = int(input("Digite o ano de nascimento: "))
    if (ano >= 1922) and (ano <= 2021):
      print("Em 2022", nome, "completou", 2021 - ano + 1, "anos")
      break
    else:
      print("Data invalida, tente outra data")
  except:
    print("Caracter invalido, tente novamente")