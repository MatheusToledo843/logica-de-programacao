# Lista que guarda os filmes cadastrados
filmes = [
    {"id": 1, "titulo": "Madagascar", "genero": "Animacao", "ano": 2004},
    {"id": 2, "titulo": "Toy Story", "genero": "Animacao", "ano": 1995},
    {"id": 3, "titulo": "Transformers", "genero": "Acao", "ano": 2007},
]

# Funcao para cadastrar um novo filme
def cadastrar(filmes):
    # Pede as informacoes do filme ao usuario
    titulo = input("Titulo: ")
    genero = input("Genero: ")
    ano = int(input("Ano: "))

    # Cria um novo ID automaticamente
    novo = {"id": max([f["id"] for f in filmes], default=0) + 1,
            "titulo": titulo, "genero": genero, "ano": ano}

    # Adiciona o novo filme na lista
    filmes.append(novo)
    print("Filme cadastrado!")

# Funcao para mostrar todos os filmes cadastrados
def listar(filmes):
    # Verifica se a lista esta vazia
    if len(filmes) == 0:
        print("Nenhum filme cadastrado.")

    # Percorre a lista e mostra cada filme
    for f in filmes:
        print(f)

# Funcao para procurar um filme pelo titulo
def buscar(filmes):
    nome = input("Digite o titulo do filme: ")
    encontrado = False

    # Percorre todos os filmes da lista
    for f in filmes:
        # Compara os titulos sem diferenciar letras maiusculas e minusculas
        if f["titulo"].lower() == nome.lower():
            print(f)
            encontrado = True

    # Mostra uma mensagem caso nao encontre o filme
    if not encontrado:
        print("Filme nao encontrado!")

# Funcao para remover um filme da lista
def remover(filmes):
    nome = input("Digite o titulo para remover: ")

    # Percorre a lista usando a posicao de cada filme
    for i in range(len(filmes)):
        # Verifica se o titulo corresponde ao digitado
        if filmes[i]["titulo"].lower() == nome.lower():
            # Remove o filme encontrado
            filmes.pop(i)
            print("Filme removido!")
            return

    # Aparece caso nenhum filme seja encontrado
    print("Filme nao encontrado!")

# Repeticao que mantem o menu funcionando
while True:
    # Mostra as opcoes disponiveis
    print("\n1 - Adicionar filme")
    print("2 - Mostrar filmes")
    print("3 - Buscar filme")
    print("4 - Remover filme")
    print("5 - Sair")

    # Recebe a opcao escolhida pelo usuario
    opcao = input("Escolha: ")

    # Verifica qual opcao foi escolhida
    if opcao == "1":
        cadastrar(filmes)
    elif opcao == "2":
        listar(filmes)
    elif opcao == "3":
        buscar(filmes)
    elif opcao == "4":
        remover(filmes)
    elif opcao == "5":
        # Encerra o programa
        break
    else:
        # Mensagem para uma opcao que nao existe
        print("Opcao invalida!")
