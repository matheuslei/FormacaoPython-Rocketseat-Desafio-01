def mostrar_menu():
    print("\nAgenda de Contatos")
    print("1. Adicionar Contato")
    print("2. Listar Contatos")
    print("3. Editar Contato")
    print("4. Marcar/Desmarcar Favorito")
    print("5. Listar Favoritos")
    print("6. Deletar Contato")
    print("0. Sair")


def adicionar_contato(lista_contatos):
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    favorito = input("Favorito (s/n): ").lower() == 's'
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": favorito}
    lista_contatos.append(contato)
    print(f"Contato {nome} adicionado com sucesso!")


def listar_contatos(lista_contatos):
    if not lista_contatos:
        print("Nenhum contato cadastrado.")
    else:
        for i, contato in enumerate(lista_contatos, start=1):
            print(f"{i}. Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}, Favorito: {'Sim' if contato['favorito'] else 'Não'}")


def editar_contato(lista_contatos):
    indice = int(input("Índice do contato a editar: ")) - 1
    if 0 <= indice < len(lista_contatos):
        contato = lista_contatos[indice]
        print("Deixe em branco para manter o valor atual.")
        novo_nome = input(f"Novo nome ({contato['nome']}): ") or contato['nome']
        novo_telefone = input(f"Novo telefone ({contato['telefone']}): ") or contato['telefone']
        novo_email = input(f"Novo email ({contato['email']}): ") or contato['email']

        contato['nome'] = novo_nome
        contato['telefone'] = novo_telefone
        contato['email'] = novo_email

        print(f"Contato {novo_nome} atualizado com sucesso!")
    else:
        print("Contato não encontrado.")


def marcar_desmarcar_favorito(lista_contatos):
    indice = int(input("Índice do contato a marcar/desmarcar favorito: ")) - 1
    if 0 <= indice < len(lista_contatos):
        contato = lista_contatos[indice]
        contato['favorito'] = not contato['favorito']
        status = "favorito" if contato['favorito'] else "não favorito"
        print(f"Contato {contato['nome']} marcado como {status}.")
    else:
        print("Contato não encontrado.")


def listar_favoritos(lista_contatos):
    favoritos = [contato for contato in lista_contatos if contato['favorito']]
    if not favoritos:
        print("Nenhum contato favorito.")
    else:
        for i, contato in enumerate(favoritos, start=1):
            print(f"{i}. Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}, Favorito: {'Sim' if contato['favorito'] else 'Não'}")


def deletar_contato(lista_contatos):
    indice = int(input("Índice do contato a deletar: ")) - 1
    if 0 <= indice < len(lista_contatos):
        contato = lista_contatos.pop(indice)
        print(f"Contato {contato['nome']} deletado com sucesso!")
    else:
        print("Contato não encontrado.")


def principal():
    lista_contatos = []

    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_contato(lista_contatos)
        elif escolha == '2':
            listar_contatos(lista_contatos)
        elif escolha == '3':
            editar_contato(lista_contatos)
        elif escolha == '4':
            marcar_desmarcar_favorito(lista_contatos)
        elif escolha == '5':
            listar_favoritos(lista_contatos)
        elif escolha == '6':
            deletar_contato(lista_contatos)
        elif escolha == '0':
            print("Saindo da agenda. Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    principal()
