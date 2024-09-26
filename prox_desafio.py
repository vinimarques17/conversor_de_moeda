# Declarando variaveis do escopo
dolar = 5.45
euro = 6.10
peso = 177.08

# tornando um função para facilitar na manutenção do código
def converter(value: float, choose: str):  
    if (choose == 'dolar'):
        return value * dolar
    elif (choose == 'euro'):
        return value * euro
    elif (choose == 'peso'):
        return value * peso
    else:
        return False

# Nova feature para o usuário
def compareCoins(value: float):
    compare_dolar = value * dolar
    compare_euro = value * euro
    compare_peso = value * peso
    return print(f'Dolar: {compare_dolar} | Euro: {compare_euro} | Pesos argentinos: {compare_peso}')

# inputs
real = input('Qual o valor a converter? ')
choose = input('Qual moeda irá converter? ')

# Transformando o texto em letras minusculas
choose = choose.lower()

# Validando os dados recebidos e printando
if converter(float(real), choose):
    print(f'A cotação em {choose} resultou em: $ {converter(float(real), choose)}')
else:
    print('Não foi possível fazer a conversão, moeda inválida.')

# Print na cotação de todas moedas
print('A cotação para cada moeda:')
compareCoins(float(real))