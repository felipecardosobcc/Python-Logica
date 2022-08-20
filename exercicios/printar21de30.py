from random import randint

lista = []

for i in range(30):
    lista.append(randint(1,100))

print()
print(lista)
print(f'\nO elemento da 21° posição da lista criada é {lista[21]}\n')