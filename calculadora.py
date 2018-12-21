import math as m


def calculo(op, n1, n2):
    if op == 1:
        print('O resultado da soma é: {}'.format(round(float(n1) + float(n2), 2)))
    elif op == 2:
        print('O resultado da subtração é: {}'.format(round(float(n1) - float(n2), 2)))
    elif op == 3:
        print('O resultado da multiplicação é: {}'.format(round(float(n1) * float(n2), 2)))
    elif op == 4:
            print('O resultado da divisão é: {}'.format(round(float(n1) / float(n2), 2)))


print("""1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão\n0. Sair""")
op = int(input('Informe a operação desejada: '))

while op != 0:
    if op != 1 or op != 2 or op != 3 or op != 4 or op != 0:
        print('Oops! Operando inexistente. Tente novamente.')
        op = int(input('\nInforme a operação desejada: '))

    try:
        n1 = input('Informe o primeiro número: ')
        n2 = input('Informe o segundo número: ')
        calculo(op, n1, n2)
    except:
        print("Não é possível efetuar a operação. Número não fornecido ou número zero inserido no divisor.")

    print("""\n1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão\n0. Sair""")
    op = int(input('Informe a operação desejada: '))