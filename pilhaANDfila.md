import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

pilhaPratos = []

while (True):
    
    print("\nO que você deseja fazer?")
    print("1. Adicionar um prato")
    print("2. Remover um prato")

    opcao = input("Escolha uma opção (1/2): ")
    
    clear_screen()
    if opcao == "1":
        prato = f"Prato {len(pilhaPratos) + 1}"  
        pilhaPratos.append(prato)
        print(f"'{prato}' foi adicionado à pilha.")
    elif opcao == "2":
        if pilhaPratos:
            removePrato= pilhaPratos.pop()
            print(f"'{removePrato}' foi removido da pilha.")
        else:
            print("A pilha está vazia. Não há pratos para remover.") 
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2")
