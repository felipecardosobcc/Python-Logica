print()

pedido = float(input('Informe o valor do pedido: '))
estado = input('Informe seu Estado(sigla): ')

print()
if estado in ["PA", "Pa", "pa", "pA"]:
    imposto = (5.5/100)*pedido
    total = imposto + pedido
    print(f'Subtotal: R$ {pedido:.2f}')
    print(f'Valor do imposto: R$ {imposto:.2f}')
    print(f'Total: R$ {total:.2f}')
else:
    print(f'Total: R$ {pedido:.2f}')

print()

