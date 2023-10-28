numeros = []
numerosaocontrario=[]
for i in range(5):
    numero = float(input("Digite um número:"))
    numeros.append(numero)
print(numeros)
for x in range(4, -1, -1):
    numerosaocontrario.append(numeros[x])
print(numerosaocontrario)