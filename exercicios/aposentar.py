from datetime import date

print()
print("="*151)
print()
idade_atual = int(input('Forneça sua idade: '))
idade_aposento = int(input('Forneça a idade que voce gostaria de se aposentar: '))
espera = idade_aposento - idade_atual
print()
print(f'Ainda faltam {espera} anos para voce se aposentar')

time = date.today()
ano = time.year
anofinal = ano + espera
print(f'É {ano}, então voce pode se aposentar em {anofinal}')
print()
print("="*151)

