def add_contact(name, phone, email, is_favorite=False):
    if not name or not phone or not email:
        print("Todos os campos são obrigatórios!")
        return
    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'is_favorite': is_favorite
    }
    contacts.append(contact)
    print(f"{name} foi adicionado(a) com sucesso!")

def view_contacts(contacts):
    if not contacts:
        print("Nenhum contato cadastrado.")
        return
    for index, contact in enumerate(contacts, start=1):
        favorite_status = "❤" if contact['is_favorite'] else ""
        print(f"{index}. {favorite_status} {contact['name']} - {contact['phone']} - {contact['email']}")

def update_contact(index):
    if index < 0 or index >= len(contacts):
        print("Contato não encontrado.")
        return
    print("Informe os novos dados do contato:")
    name = input("Nome: ")
    phone = input("Telefone: ")
    email = input("Email: ")
    is_favorite = input("É favorito? (s/n): ").lower() == 's'
    contacts[index] = {
        'name': name,
        'phone': phone,
        'email': email,
        'is_favorite': is_favorite
    }
    print(f"Contato de {name} atualizado com sucesso!")

def toggle_favorite(index):
    if not (0 <= index < len(contacts)):
        print("Contato não encontrado.")
        return
    contact = contacts[index]
    contact['is_favorite'] = not contact['is_favorite']
    status = "favoritado" if contact['is_favorite'] else "desfavoritado"
    print(f"O contato {contact['name']} foi {status}.")

contacts = []

while True:
    print("1 - Adicionar um contato")
    print("2 - Visualizar contatos cadastrados")
    print("3 - Editar um contato")
    print("4 - Favoritar/Desfavoritar um contato")
    print("5 - Visualizar contatos favoritos")
    print("6 - Remover um contato")
    print("7 - Sair")

    selected_option = input("Escolha uma opção: ")

    if selected_option == "1":
        print("Para adicionar um contato, preencha todas as informações solicitadas:")
        name = input("Informe o nome: ")
        phone = input("Informe o telefone: ")
        email = input("Informe o email: ")
        is_favorite = input("É favorito? (s/n): ").lower() == 's'
        add_contact(name, phone, email, is_favorite)

    elif selected_option == "2":
        view_contacts(contacts)

    elif selected_option == "3":
        print("Contatos disponíveis para edição:")
        view_contacts(contacts)
        index = int(input("Informe o número (index) do contato que deseja editar: ")) - 1
        update_contact(index)

    elif selected_option == "4":
        print("Contatos disponíveis para favoritar/desfavoritar:")
        view_contacts(contacts)
        index = int(input("Informe o número (index) do contato que deseja favoritar/desfavoritar: ")) - 1
        toggle_favorite(index)

    elif selected_option == "7":
        print("Saindo do programa...")
        break