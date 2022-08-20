n = int(input('Quantos cálculos você deseja realizar?\n'))

print()
print("Digite '+' para soma.")
print("Digite '-' para subtração.")
print("Digite '*' para multiplicação.")
print("Digite '/' para divisão.")
print("Digite '^' para potenciação")
print()

for i in range(n):
    operador = input("Que operação voce deseja realizar?\n")
    a = int(input("Digite um número inteiro: "))
    b = int(input("Digite um número inteiro: "))
    if operador == '+':
        print(f'Resultado: {a+b}')
    elif operador == '-':
        print(f'Resultado: {a-b}')    
    elif operador == '*':
        print(f'Resultado: {a*b}')
    elif operador == '/':
        print(f'Resultado: {a/b}') 
    elif operador == '^':
        print(f'Resultado: {a**b}') 
    else:
        print("Operador não reconhecido.")  




    
    
    
