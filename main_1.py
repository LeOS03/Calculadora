from calculo import calculo
import os
import sys

print("""1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão""")
print("""5. Potência\n6. Logaritmo\n7. Raiz quadrada\n0. Sair""")
op = int(input('Informe a operação desejada: '))

if op == 0:
    print("Muito obrigado! Volte sempre! <3")

while op != 0:
    if op not in [0, 1, 2, 3, 4, 5, 6, 7]:
        print('Oops! Operando inexistente. Tente novamente.')
    try:
        
            if op == 5:
                n1 = float(input('Informe a base: '))
                n2 = float(input('Informe o expoente: '))
                os.system('clear')
                calculo(op, n1, n2)
                
            elif op == 6:
                n1 = float(input('Informe o logaritmando: '))
                n2 = float(input('Informe a base: '))
                os.system('clear')
                calculo(op, n1, n2)

            elif op == 7:
                n1 = float(input('Informe o número: '))
                os.system('clear')
                calculo(op, n1, 2)

            else:
                n1 = input('Informe o primeiro número: ')
                n2 = input('Informe o segundo número: ')
                os.system('clear')
                calculo(op, n1, n2)
                
    except:           
        print("Não é possível efetuar a operação. Número não fornecido ou número zero inserido no divisor.")

    print("""\n1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão""")
    print("""5. Potência\n6. Logaritmo\n7. Raiz quadrada\n0. Sair""")
    op = int(input('Informe a operação desejada: '))

    if op == 0:
        print("Muito obrigado! Volte sempre! <3")
