def escada(number):
    for i in range(number):
        print(f'{i + 1} ' * (i+1))

escada(5)

def escadainversa(number):
    for i in range(1, number+1):
        esp = number - i
        print("  "*esp, end = "")
        print(f' {i}'*i)

print()
escadainversa(5)