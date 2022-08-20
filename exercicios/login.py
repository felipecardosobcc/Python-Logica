print("="*150)
print()
user_1 = input("Crie um novo usuário: ")
key_1 = input("Crie uma nova senha: ")

print()
verif_user = input("Digite seu nome de usuário: ")
verif_key = input("Digite sua senha: ")

if verif_user == user_1 and verif_key == key_1:
    print("\nBem-vindo!")
else:
    print("\nLOGIN INVÁLIDO")

print()
print("="*150)