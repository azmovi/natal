with open('q2/input.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

total = 0
for linha in linhas:
    game, resto = linha[:-1].split(':')
    id = int(game[5:])
    total += id
    analises = resto.split(';')
    for analise in analises:
        red = 12
        green = 13
        blue = 14
        bag = analise.split(',')
        for item in bag:
            valor, cor = item.split()
            valor = int(valor)
            if cor == 'red':
                red -= valor
            elif cor == 'green':
                green -= valor
            else:
                blue -= valor
        if red < 0 or green < 0 or blue < 0:
            total -= id
            break

print(total)
