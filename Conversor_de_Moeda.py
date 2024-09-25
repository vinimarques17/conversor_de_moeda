real = input('Qual o valor a converter? ')
dolar = float(real) * 5.45
euro = float(real) * 6.10
peso_argentino = float(real) * 177.08

choose = input('Qual moeda irá converter? ')

if choose == 'Dolar':
    print(f'A cotacão do Dólar hoje é {dolar:.2f}.')
elif choose == 'Euro':
    print(f'A cotacão do Euro hoje é {euro:.2f}.')
elif choose == 'Peso':
    print(f'A cotacão do Peso Argetino hoje é {peso_argentino:.2f}.')
else:
    print('Digite uma moeda válida')