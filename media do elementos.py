# Lista fornecida
numeros = [2, 4, 6, 8, 10]

# Calculando a média
media = sum(numeros) / len(numeros)

# Encontrando o índice do elemento central (assumindo que a lista tenha um número ímpar de elementos)
indice_central = len(numeros) // 2

# Substituindo o elemento central pela média
numeros[indice_central] = media

# Exibindo a lista modificada
print("Lista após inserir a média no elemento central:")
for numero in numeros:
    print(numero)
