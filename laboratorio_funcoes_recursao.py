TAXA_PROCESSAMENTO = 2.00

def calcular_frete(valor_compra, peso_kg):
    frete = peso_kg * 5

    if valor_compra >= 200:
        frete = frete * 0.50

    return frete

def aplicar_cupom(valor_item, cupom_desconto):
    valor_com_desconto = valor_item - (valor_item * cupom_desconto / 100)
    preco_final = valor_com_desconto + TAXA_PROCESSAMENTO

    return preco_final

def exibir_cronograma_regressivo(parcelas_restantes, valor_parcela):
    if parcelas_restantes == 0:
        print("Todas as parcelas foram quitadas!")
        return

    print(f"Restam {parcelas_restantes} parcela(s) de R$ {valor_parcela}")
    exibir_cronograma_regressivo(parcelas_restantes - 1, valor_parcela)


print("=== TESTE PARTE 1: CALCULADORA DE FRETE ===")
frete = calcular_frete(200, 4)
print(f"Frete Final Esperado (10.0): {frete}")

print("\n=== TESTE PARTE 2: CUPOM E TAXAS DE ESCOPO ===")
preco = aplicar_cupom(100, 10)
print(f"Preço Final Esperado (92.0): {preco}")

print("\n=== TESTE PARTE 3: CRONOGRAMA RECURSIVO ===")
exibir_cronograma_regressivo(3, 150.0)