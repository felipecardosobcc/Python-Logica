print("="*150)
print()

idade = int(input('Digite sua idade: '))
if idade >= 18:
    while True:
        doc = int(input('Você possui CNH?\nResponda 1 para sim ou 2 para não:\n'))
        if doc == 1 or doc == 2:
            break
    if doc == 1:
        print("\nVocê poderá realizar os cursos de direção defensiva e de defesa pessoal.")
    else:
        print("\nVocê poderá realizar o curso de defesa pessoal.")
else:
    print("\nVocê precisa atingir a maioridade para realizar um dos cursos.")

print()
print("="*150)