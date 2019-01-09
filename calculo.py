import math as m


def calculo(op, n1, n2):
    if op == 1:
        print('O resultado de {} + {} = {}'.format(n1, n2, round(float(n1) + float(n2), 2)))

    elif op == 2:
        print('O resultado de {} - {} = {}'.format(n1, n2, round(float(n1) - float(n2), 2)))

    elif op == 3:
        print('O resultado de {} * {} = {}'.format(n1, n2, round(float(n1) * float(n2), 2)))

    elif op == 4:
        print('O resultado de {} / {} = {}'.format(n1, n2, round(float(n1) / float(n2), 2)))

    elif op == 5:
        print('O resultado da potência de {}^{} = {}'.format(n1, n2, round(m.pow(n1, n2), 2)))

    elif op == 6:
        print('O resultado do logaritmo de {} na base {} = {}'.format(n1, n2, round(m.log(n1, n2), 2)))

    elif op == 7:
        print('O resultado da raiz quadrada de {} = {}'.format(n1, round(m.sqrt(n1), 2)))
