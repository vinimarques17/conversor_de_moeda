# Declarando variaveis do escopo
book_of_coins = {

    'dolar': 5.45,
    'euro': 6.10,
    'peso': 177.08,
    'yen': 0.037,
    'yuan': 0.78,
    'franco_suico': 0.16,
    'dolar_canadense': 0.25,
    'rupia_indonesia': 2784.15,
    'kwanza_angola': 172.87,
    'rublo_russo': 16.98

}

# tornando um função para facilitar na manutenção do código
def converter(value: float, moeda: str):  
    if (moeda in book_of_coins):
        return value * book_of_coins[moeda]
    else:
        return False

# Nova feature para o usuário (necessário atualizar e modificar para encaixar no dicinário)
# def compareCoins(value: float):
#     compare_dolar = value * dolar
#     compare_euro = value * euro
#     compare_peso = value * peso
#     return print(f'Dolar: {compare_dolar:.2f} | Euro: {compare_euro:.2f} | Pesos argentinos: {compare_peso:.2f}')

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
    # compareCoins(float(real))
else:
    print('Não foi possível fazer a conversão, moeda inválida.')

