# Desafio 1 - Processador de Texto com Fatiamento e Listas

frase = input("Digite uma frase: ")
palavras = frase.split()

print("\nAs três primeiras palavras (usando slicing):")
print(palavras[:3])

print("\nÍndice e valor de cada palavra (usando enumerate):")
for indice, palavra in enumerate(palavras):
    print(f"{indice}: {palavra}")

print("\nFrase com ordem das palavras invertida:")
print(' '.join(palavras[::-1]))