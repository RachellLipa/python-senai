escolha=input("Escolha a sequência: c - crescente, d- decrescente. ")
inicio=int(input("Digite o início da sequência "))
fim=int(input("Digite o fim da sequência "))

for n in range(inicio, fim+1):
  if(escolha == "c"):
    print(n)
  else:
    print(fim+1-n)