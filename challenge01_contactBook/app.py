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
        print(f"{favorite_status} {index}. {contact['name']} - {contact['phone']} - {contact['email']}")

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

    elif selected_option == "7":
        print("Saindo do programa...")
        break