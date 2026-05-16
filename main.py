soma_idade = 0

for i in range(0,4):

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo: ").upper()

    soma_idade += idade

media = soma_idade / 4

print(f"Media das idades: {media}")