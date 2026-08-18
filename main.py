from config import connect_bd

# Conecta ao banco de dados uma única vez, quando o programa inicia
conexão = connect_bd()


def cadastrar_produto():
    # Pergunta o nome e o valor, e salva um novo produto no banco
    cursor = conexão.cursor()

    nome_produto = input("Nome do produto: ")
    valor = float(input("Valor do produto: "))

    # Usamos %s como "espaço reservado" para os valores. O banco preenche
    # esses espaços de forma segura, sem risco de SQL Injection.
    query = "INSERT INTO produtos (nome_produto, valor) VALUES (%s, %s)"
    cursor.execute(query, (nome_produto, valor))
    conexão.commit()

    cursor.close()
    print("Produto cadastrado com sucesso!\n")


def visualizar_produtos():
    
    cursor = conexão.cursor()

    cursor.execute("SELECT nome_produto, valor FROM produtos")
    produtos = cursor.fetchall()

    cursor.close()

    if not produtos:
        print("Nenhum produto cadastrado ainda.\n")
        return

    print("\n--- PRODUTOS CADASTRADOS ---")
    for nome_produto, valor in produtos:
        print(f"{nome_produto} - R$ {valor:.2f}")
    print()

def exibir_menu():
    print("===========================================")
    print("=      (1) - Cadastrar produto            =")
    print("=      (2) - Visualizar produtos          =")
    print("=      (3) - Sair                         =")
    print("===========================================")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            visualizar_produtos()
        elif opcao == "3":
            print("\nAté mais!")
            break
        else:
            print("\nOpção inválida. Escolha 1, 2 ou 3.\n")

    conexão.close()

if __name__ == "__main__":
    main()