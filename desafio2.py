# Desafio 2 - Controle de Sensores com Tratamento de Erros

entrada = input("Digite o valor do sensor: ")
valor = None

try:
    valor = float(entrada)
    if valor < 0:
        print("Valor inválido (menor que zero). Retornando None.")
        valor = None
    else:
        print(f"Valor válido: {valor}")
except ValueError:
    print("Entrada inválida! Não é possível converter para float. Retornando None.")
    valor = None

print(f"id(valor): {id(valor)}")
print("O id() mostra o identificador único do objeto na memória. Objetos imutáveis como float e None podem compartilhar o mesmo id se forem reutilizados pelo Python.")