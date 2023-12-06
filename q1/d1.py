
with open('input.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()

total = 0

for linha in conteudo:
    achou = False
    for i in range(len(linha)):
        if linha[i].isdigit():
            decimal = int(linha[i]) * 10
            achou = True

        if achou:
            break

    achou = False
    for i in range(len(linha)-1, -1, -1):
        if linha[i].isdigit():
            unidade = int(linha[i])
            achou = True

        if achou:
            break

    valor = decimal + unidade
    total += valor
print(total)
