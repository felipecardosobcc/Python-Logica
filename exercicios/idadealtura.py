idade = []
altura = []
soma = 0
count = 0

print()
for i in range(3):
    idade.append(int(input(f'Informe a idade do {i+1}° aluno: ')))
    altura.append(float(input(f'Informa a altura do {i+1}° aluno: ')))
    print()
    soma += altura[i]

media = soma/3

for x in range(3):
    if idade[x] > 13 and altura[x] < media:
        count += 1

print(f'{count} aluno(s) com mais de 13 anos estão abaixo da média da altura da turma, que é de {media:.2f} metros.')


