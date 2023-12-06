numericos = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
             'seven': 7, 'eight': 8, 'nine': 9}
reverse = {'eno': 1, 'owt': 2, 'eerht': 3, 'ruof': 4, 'evif': 5, 'xis': 6,
           'neves': 7, 'thgie': 8, 'enin': 9}

with open('input.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()

total = 0
texto = []
for linha in conteudo:
    achou = False
    for i in range(len(linha)):
        if linha[i].isdigit():
            decimal = int(linha[i]) * 10
            achou = True
        else:
            for key in numericos.keys():
                if linha[i] == key[0]:
                    if linha[i:i+len(key)] in numericos:
                        decimal = int(numericos[linha[i:i+len(key)]]) * 10
                        achou = True
        if achou:
            break

    achou = False
    for i in range(len(linha)-1, -1, -1):
        if linha[i].isdigit():
            unidade = int(linha[i])
            achou = True
        else:
            for key in reverse.keys():
                if linha[i] == key[-1]:
                    if linha[i:i+len(key)] in numericos:
                        unidade = int(numericos[linha[i:i+len(key)]])
                        achou = True
        if achou:
            break
    valor = decimal + unidade
    total += valor
print(total)
