soma_idade = 0
mais_velho = 0
nome_velho = ""
mulheres_nova = 0

for i in range(0,4):

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo: ").upper()

    soma_idade += idade

    if sexo == "M":

        if idade > mais_velho:
            mais_velho = idade
            nome_velho = nome

    if sexo == "F":

        if idade < 20:
            mulheres_nova += 1

media = soma_idade / 4

print(f"Media das idades: {media}")
print(f"Homem mais velho: {nome_velho}")
print(f"Mulheres menores de 20 anos: {mulheres_nova}")