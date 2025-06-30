while True:
    print("1 - Adicionar um contato")
    print("2 - Visualizar contatos cadastrados")
    print("3 - Editar um contato")
    print("4 - Favoritar/Desfavoritar um contato")
    print("5 - Visualizar contatos favoritos")
    print("6 - Remover um contato")
    print("7 - Sair")

    selectedOption = input("Escolha uma opção: ")

    if selectedOption == "7":
        print("Saindo do programa...")
        break