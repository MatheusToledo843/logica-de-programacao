catalogo = [
    {
        "produto": "Notebook",
        "preco": 2500.00,
        "em_estoque": True
    },
    {
        "produto": "Mouse",
        "preco": 80.00,
        "em_estoque": True
    }
]

for item in catalogo:
    print(f"Produto: {item['produto']} | Preço: R$ {item['preco']:.2f}")
