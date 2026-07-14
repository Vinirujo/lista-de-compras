compras = []

while True:
    print("===== Lista de Compras =====")
    print("1 - Adicionar item para comprar")
    print("2 - Remover item da lista")
    print("3 - Exibir lista de compras")
    print("0 - Sair")
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        item = input("Digite o nome do item que deseja adicionar: ")
        compras.append(item)
        print(f"Item {item} adicionado à lista de compras.")
        
    elif opcao == 2:
        item = input("Digite o nome do item que deseja remover: ")
        if item in compras:
            compras.remove(item) 
            print(f"Item {item} removido da lista de compras.")  
        else:
            print(f"Item {item} não encontrado na lista de compras.") 
            
    elif opcao == 3:
        print("Lista de compras:")
        for i, item in enumerate(compras, start=1):
            print(f" {i} - {item}")
            
    elif opcao == 0:
        print("Saindo do programa. Ate mais") 
        break
    else:
        print("Opção invalida, tente novamente.")                      