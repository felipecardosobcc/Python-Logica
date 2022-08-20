nomes = []

num = int(input('Quantos nomes você quer adicionar?\n'))

for i in range(num):
    nomes.append(input(f'Digite o {i+1}° nome: '))

print("\nNomes com caracteres maior que 7:")

for x in range(num):
    if len(nomes[x]) > 7:
        print(nomes[x])

print()