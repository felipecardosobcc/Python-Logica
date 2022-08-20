while True:
    cpf = input('Forneça seu CPF: ')
    controle = len(cpf)
    if controle == 11 or controle == 14:
        break

if controle == 11:
    print(f'SEU CPF FOI VALIDADO: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}')
elif controle == 14:
    print("SEU CPF FOI VALIDADO:", cpf)
        
    