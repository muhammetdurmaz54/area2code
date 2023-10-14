# FOR (Decremento)
print("FOR (Decremento)")
for andar in range(20,0,-1):
  if andar == 13:
    continue
  print(andar)

# FOR (Incremento)
print("FOR (Incremento)")
for andar in range(1,21,1):
  if andar == 13:
    continue
  print(andar)

# WHILE (Incremento)
print("WHILE (Incremento)")
andar = 1
while andar <= 20:
    if andar != 13:
        print(andar)
    andar += 1

# WHILE (Decremento)
print("WHILE (Decremento)")
andar = 20
while andar >= 1:
    if andar != 13:
        print(andar)
    andar -= 1