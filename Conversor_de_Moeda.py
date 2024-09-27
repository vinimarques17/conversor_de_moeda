# Declarando variaveis do escopo
dolar = 5.45
euro = 6.10
peso = 177.08

# tornando um função para facilitar na manutenção do código
def converter(value: float, moeda: str):  
    if (moeda == 'dolar'):
        return value * dolar
    elif (moeda == 'euro'):
        return value * euro
    elif (moeda == 'peso'):
        return value * peso
    else:
        return False

# Nova feature para o usuário
def compareCoins(value: float):
    compare_dolar = value * dolar
    compare_euro = value * euro
    compare_peso = value * peso
    return print(f'Dolar: {compare_dolar:.2f} | Euro: {compare_euro:.2f} | Pesos argentinos: {compare_peso:.2f}')

# inputs
real = input('Qual o valor a converter? ')
choose = input('Qual moeda irá converter? ')

# Transformando o texto em letras minusculas
choose = choose.lower()

# Validando os dados recebidos e printando
if converter(float(real), choose):
    print(f'A cotação em {choose} resultou em: $ {converter(float(real), choose):.2f}')
# Print na cotação de todas moedas
    print('A cotação para cada moeda:')
    compareCoins(float(real))
else:
    print('Não foi possível fazer a conversão, moeda inválida.')

