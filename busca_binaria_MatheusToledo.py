
numeros = [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 72, 81, 89, 94, 99]

alvo = int(input("Digite o número que deseja procurar: "))

inicio = 0
fim = len(numeros) - 1

comparacoes = 0
posicao = -1

while inicio <= fim:

    meio = (inicio + fim) // 2

    comparacoes += 1

    if numeros[meio] == alvo:
        posicao = meio
        break

    elif numeros[meio] < alvo:
        inicio = meio + 1

    else:
        fim = meio - 1

if posicao != -1:
    print(f"Número {alvo} encontrado no índice {posicao}.")
else:
    print(f"Número {alvo} não foi encontrado na lista.")

print(f"Total de comparações: {comparacoes}")
