filmes = [
    {"id": 1, "titulo": "Madagascar", "genero": "Animacao", "ano": 2004},
    {"id": 2, "titulo": "Toy Story", "genero": "Animacao", "ano": 1995},
    {"id": 3, "titulo": "Transformers", "genero": "Acao", "ano": 2007},
]

def cadastrar(filmes):
    titulo = input("Titulo: ")
    genero = input("Genero: ")
    ano = int(input("Ano: "))
    novo = {"id": max([f["id"] for f in filmes], default=0) + 1,
            "titulo": titulo, "genero": genero, "ano": ano}
    filmes.append(novo)
    print("Filme cadastrado!")

def listar(filmes):
    if len(filmes) == 0:
        print("Nenhum filme cadastrado.")
    for f in filmes:
        print(f)

def buscar(filmes):
    nome = input("Digite o titulo do filme: ")
    encontrado = False
    for f in filmes:
        if f["titulo"].lower() == nome.lower():
            print(f)
            encontrado = True
    if not encontrado:
        print("Filme nao encontrado!")

def remover(filmes):
    nome = input("Digite o titulo para remover: ")
    for i in range(len(filmes)):
        if filmes[i]["titulo"].lower() == nome.lower():
            filmes.pop(i)
            print("Filme removido!")
            return
    print("Filme nao encontrado!")

while True:
    print("\n1 - Adicionar filme")
    print("2 - Mostrar filmes")
    print("3 - Buscar filme")
    print("4 - Remover filme")
    print("5 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar(filmes)
    elif opcao == "2":
        listar(filmes)
    elif opcao == "3":
        buscar(filmes)
    elif opcao == "4":
        remover(filmes)
    elif opcao == "5":
        break
    else:
        print("Opcao invalida!")
