from datetime import date

print("Quando as aulas começam?")
dia = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))

inicio_aulas = date(ano, mes, dia)
dia_atual = date.today()

if dia_atual == inicio_aulas:
    print("\nVACATION IS OVER BITCH !!! Suas aulas já começaram :(\n")
elif dia_atual > inicio_aulas:
    print("As aulas já começaram, atente-se !!!")    
else:
    espera = inicio_aulas - dia_atual
    print("\nAinda há tempo para curtir.\nDias restantes das férias:")
    print(f'{espera.days} dias\n')