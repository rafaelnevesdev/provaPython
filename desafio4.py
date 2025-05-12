# Desafio 4 - Sistema de Cadastro Simples com Flags e Validação

cadastros = []

while True:
    nome = input("Digite o nome (ou 'sair' para encerrar): ")
    if nome.lower() == "sair":
        break

    flag_idade_invalida = True
    while flag_idade_invalida:
        idade_str = input("Digite a idade: ")
        try:
            idade = int(idade_str)
            flag_idade_invalida = False
        except ValueError:
            print("Idade inválida! Por favor, digite um número inteiro.")

    cadastros.append((nome, idade))

print("\nCadastros realizados:")
for cadastro in cadastros:
    print(f"Nome: {cadastro[0]}, Idade: {cadastro[1]}")

maiores_18 = [c for c in cadastros if c[1] > 18]
print(f"\nQuantidade de pessoas com mais de 18 anos: {len(maiores_18)}")