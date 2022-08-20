notas = []
soma = 0

for i in range(4):
    notas.append(float(input(f'Digite a {i+1}° nota: ')))
    soma += notas[i]

print(f'\nA média das notas é {soma/4}')

