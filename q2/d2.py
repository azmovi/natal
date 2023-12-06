with open('input.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

total = 0
for linha in linhas:
    game, resto = linha[:-1].split(':')
    id = int(game[5:])
    analises = resto.split(';')
    red = 0
    green = 0
    blue = 0
    for analise in analises:
        bag = analise.split(',')
        for item in bag:
            valor, cor = item.split()
            valor = int(valor)
            if cor == 'red' and red < valor:
                red = valor
            elif cor == 'green' and green < valor:
                green = valor
            elif cor == 'blue' and blue < valor:
                blue = valor
    valor = red * blue * green
    total += valor

print(total)
