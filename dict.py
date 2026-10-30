
produto = {
    "codigo": 101,
    "nome": "Teclado Mecânico Gamer",
    "preco": 250.0,
    "estoque": 14
}


print("Produto cadastrado:")
print(produto)

# Exibindo nome e preço
print("Nome:", produto["nome"])
print("Preço:", produto["preco"])



produto["preco"] = 220.0
produto["estoque"] += 6
produto["categoria"] = "Periféricos"


print("\nProduto atualizado:")
print(produto)




usuario = {
    "nome": "Carlos Eduardo",
    "nivel": "Administrador",
    "ativo": True
}


print("\nChaves do usuário:")
print(usuario.keys())

print("Valores do usuário:")
print(usuario.values())
