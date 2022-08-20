# Strip: ignora os espaços em brancos antes do primeiro caractere, ou seja, bom para evitar bugs.
nome = input('Digite seu nome completo: ').strip()
nome1 = nome
print(nome)
print()
nome_upper = nome.upper()
print(f'Seu nome com letras maiúsculas é:\n{nome_upper}')
print()
nome_lower = nome.lower()
print(f'Seu nome com letras minúsculas é:\n{nome_lower}')
print()

# Split: Pega as palavras de uma variável e armazena em uma lista. Cada palavra tem um índex diferente.
controle = nome.split()
soma = 0
for i in range(len(controle)):
    letras = len(controle[i])
    soma += letras
print(f'Seu nome possui {soma} letras')
# OU PODE FAZER UTILIZANDO A FUNÇÃO "JOIN":
# O join coloca o elemento entre aspas entre todos elementos de uma lista.
controle = "".join(controle)
soma = len(controle)
print(f'Seu nome possui {soma} letras')
# OU PODE FAZER UTILIZANDO A FUNÇÃO "REPLACE":
# O replace precisa de dois parâmetros, o primeiro é o que voce quer substituir na string, o segundo é pelo o que voce vai substituir.
nome = nome.replace(" ", "")
print(f'Seu nome possui {len(nome)} letras')

controle = nome1.split()
first_name = len(controle[0])
print()
print(f'Seu primeiro nome possui {first_name} letras')
print()