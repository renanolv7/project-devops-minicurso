from config import connect_bd
import webbrowser

# Conecta ao banco de dados uma única vez, quando o programa inicia.
# A conexão só será fechada quando o usuário escolher SAIR no menu.
connection = connect_bd()


def insert():
    """Insere um novo produto no banco de dados."""
    cursor = connection.cursor()
    try:
        nome_produto = input("Informe o nome do produto: ")
        valor = float(input("Informe o valor do produto: "))

        query = "INSERT INTO produtos (nome_produto, valor) VALUES (%s, %s)"
        cursor.execute(query, (nome_produto, valor))
        connection.commit()

        print("Produto inserido com sucesso!")
    except ValueError:
        print("Erro: o valor informado não é um número válido.")
    finally:
        cursor.close()


def read():
    """Lista todos os produtos cadastrados na tabela 'vendas'."""
    cursor = connection.cursor()
    try:
        query = "SELECT * FROM produtos"
        cursor.execute(query)
        resultado = cursor.fetchall()

        if resultado:
            for produto in resultado:
                id_produto, nome_produto, valor = produto
                print(f"{nome_produto} - R$ {valor:.2f}")
        else:
            print("Nenhum produto cadastrado ainda.")

    finally:
        cursor.close()


def update():
    """Atualiza o nome ou o valor de um produto já cadastrado."""
    cursor = connection.cursor()
    try:
        id_vendas = int(input("Informe o ID do produto que deseja alterar: "))
        opcao = input("Deseja alterar o NOME ou o VALOR? ").lower()

        if opcao == "nome":
            novo_valor = input("Informe o novo nome do produto: ")
            query = "UPDATE vendas SET nome_produto = %s WHERE idVendas = %s"
        elif opcao == "valor":
            novo_valor = float(input("Informe o novo valor do produto: "))
            query = "UPDATE vendas SET valor = %s WHERE idVendas = %s"
        else:
            print("Opção inválida. Digite NOME ou VALOR.")
            return

        cursor.execute(query, (novo_valor, id_vendas))
        connection.commit()

        # rowcount diz quantas linhas foram realmente alteradas
        if cursor.rowcount:
            print("Produto atualizado com sucesso!")
        else:
            print("Nenhum produto encontrado com esse ID.")
    except ValueError:
        print("Erro: valor informado inválido.")
    finally:
        cursor.close()


def delete():
    """Remove um produto do banco de dados pelo ID."""
    cursor = connection.cursor()
    try:
        id_vendas = int(input("Informe o ID do produto que deseja deletar: "))
        query = "DELETE FROM vendas WHERE idVendas = %s"
        cursor.execute(query, (id_vendas,))
        connection.commit()

        if cursor.rowcount:
            print("Produto deletado com sucesso!")
        else:
            print("Nenhum produto encontrado com esse ID.")
    except ValueError:
        print("Erro: ID inválido. Digite apenas números.")
    finally:
        cursor.close()



def exibir_menu():
    print(" ________________________________________________________")
    print(" _                                                     _ ")
    print(" _    INSERIR NOVO PRODUTO                    (1)      _ ")
    print(" _    VISUALIZAR PRODUTOS                     (2)      _ ")
    print(" -    SAIR                                    (6)      _ ")
    print(" _______________________________________________________ ")
    print()


def main():
    # while True + break: mantém o menu aparecendo até o usuário
    # escolher a opção SAIR (6).
    while True:
        exibir_menu()

        try:
            opcao = int(input("Informe uma das opções do CRUD acima: "))
        except ValueError:
            print("Digite apenas o número da opção.\n")
            continue

        if opcao == 1:
            insert()
        elif opcao == 2:
            read()
        elif opcao == 3:
            update()
        elif opcao == 4:
            delete()
        elif opcao == 5:
            open_info_dev()
        elif opcao == 6:
            print("Você resolveu nos deixar... Até breve!")
            break
        else:
            print("Opção inválida. Escolha um número de 1 a 6.")

        print()  # linha em branco para separar a próxima rodada do menu

    # Fecha a conexão com o banco só quando o programa realmente termina
    connection.close()


if __name__ == "__main__":
    main()