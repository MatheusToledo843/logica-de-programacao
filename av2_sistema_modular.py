# ==============================================================================
# PROVA PRÁTICA AV2 - 3º BIMESTRE
# ARQUIVO: av2_sistema_modular.py
# Nome do Aluno: Matheus Toledo de OLiveira
# Data: 18/09/2026
# Link do Repositório: https://github.com/MatheusToledo843/logica-de-programacao
# ==============================================================================

# Lista inicial de dados brutos
dados_brutos = [
    "  carlos eduardo silva;desenvolvedor;11988887777  ",
    "  ana paula mendes;analista de rh;21977776666  ",
    "  roberto carlos oliveira;gerente de projetos;31966665555  "
]


# ------------------------------------------------------------------------------
# 1. FUNÇÕES DO SISTEMA
# ------------------------------------------------------------------------------

def limpar_e_formatar_texto(texto):
    """
    FUNÇÃO 1:
    Remove espaços extras das pontas e converte o texto para MAIÚSCULAS.
    """
    texto_formatado = texto.strip().upper()
    return texto_formatado


def extrair_codigo_ou_ddd(dado):
    """
    FUNÇÃO 2:
    Remove espaços das pontas e utiliza fatiamento para
    extrair os 2 primeiros dígitos do telefone.
    """
    dado_limpo = dado.strip()
    codigo = dado_limpo[0:2]
    return codigo


def processar_e_exibir_cadastros(lista_dados):
    """
    FUNÇÃO 3:
    Percorre a lista, separa os dados, formata nome e cargo,
    extrai o DDD e exibe os resultados.
    """
    total = 0

    for cadastro in lista_dados:
        
        partes = cadastro.strip().split(";")

        nome = partes[0]
        cargo = partes[1]
        telefone = partes[2]

        
        nome_formatado = limpar_e_formatar_texto(nome)
        cargo_formatado = limpar_e_formatar_texto(cargo)

        
        ddd = extrair_codigo_ou_ddd(telefone)

        
        print(f"Nome: {nome_formatado}")
        print(f"Cargo/Setor: {cargo_formatado}")
        print(f"DDD: {ddd}")
        print("-" * 50)

        total += 1

    return total


# ------------------------------------------------------------------------------
# 2. PROGRAMA PRINCIPAL
# ------------------------------------------------------------------------------

def main():
    print("==================================================")
    print("     SISTEMA DE GESTÃO MODULARIZADO - AV2")
    print("==================================================\n")

    print("Iniciando o processamento dos dados...\n")

    
    total_processado = processar_e_exibir_cadastros(dados_brutos)

    
    print(f"\nTotal de registros processados: {total_processado}")

    print("\n==================================================")
    print("             PROCESSAMENTO CONCLUÍDO")
    print("==================================================")


if __name__ == "__main__":
    main()