
saldo = 0

def ver_saldo():
    print(f"\nSaldo atual: R$ {saldo:.2f}")

def depositar():
    global saldo
    valor = float(input("\nDigite o valor para o depósito: "))
    
    if valor > 0:
        saldo += valor
        print(f"\nDepósito de R$ {valor:.2f} foi realizado com sucesso!")
    else:
        print("Valor inválido! O depósito deve ser maior que zero!")

def sacar():
    global saldo
    valor = float(input("Digite o valor que deseja sacar: "))
    
    if valor > 0 and valor <= saldo:
        saldo -= valor
        print(f"\nO saque de R$ {valor:.2f} foi realizado com sucesso!")
    else:
        print("Valor inválido!!!")

def menu_principal():
    while True:
        print("\n ... MENU ...")
        print("\n1 - Ver saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Sair \n")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            ver_saldo()
        elif opcao == '2':
            depositar()
        elif opcao == '3':
            sacar()
        elif opcao == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

menu_principal()