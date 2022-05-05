import os,random

soma = 0

for i in range(10000):
  #sorteio de números
  n = (random.randint (0,10000))
  print(n)
  
  #Verificar se é par
  if(n % 2 == 0):
    soma = soma + n

else:
  os.system('clear')
  print("A soma de todos os números pares:",soma)
  