print()

while True:
    control = input("Digite C para converter de Fahrenheit para Celsius.\nDigite F para converter de Celsius para Fahrenheit.\nSua escolha: ")
    if control in ["c", "C", "f", "F"]:
        break

if control.upper() == "C":
    fah = int(input('Insira a temperatura em Fahrenheit: '))
    cel = (fah-32)*5/9
    print(f'A temperatura em Celsius é {cel}°C')   
else:
    cel = int(input('Insira a temperatura em Celsius: '))
    fah = (cel*(9/5))+32
    print(f'A temperatura em Fahrenheit é {fah}F')

print()

