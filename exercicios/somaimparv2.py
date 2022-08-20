while True:  
    inicio = int(input('Digite o número impar inicial: '))
    if inicio%2 == 1:
        break

fim = int(input('Quantas vezes você deseja realizar a soma?\n'))

if inicio == 1:
    soma = 1
elif inicio >= 3:
    soma = inicio

for n in range(fim):
    inicio += 2
    soma += inicio

print()
print(f'A soma é {soma}')