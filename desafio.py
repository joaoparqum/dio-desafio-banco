saldo = 0
limite = 500
extrato = " "
numero_saques = 0
LIMITE_SAQUE = 3
opcao = -1

while opcao != 0:
    opcao = int(input("""
    ======== Banco ========
    Selecione uma opção:
    [1] - Depositar                  
    [2] - Sacar
    [3] - Extrato
    [0] - Sair
    =======================
    """                                                  
    ))
    
    if opcao == 1:
        valor = float(input("Digite o valor para depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Foi depositado R$ {valor:.2f} reais\n"
        elif valor < 0:
            print("Valor inválido!")

    elif opcao == 2:
        saque = float(input("Digite o valor para sacar: "))

        if saque > saldo:
            print("Não será possivel fazer o saque, saldo insuficiente!!")
        elif saque > limite:
            print("O valor do saque está maior que o limite!") 
        elif numero_saques >= LIMITE_SAQUE:
            print("Não é possível fazer mais saques! Limite diário excedido!")
        elif saque > 0:
            saldo -= saque
            extrato += f"Você fez o saque de R$ {saque:.2f} reais\n"
            numero_saques += 1
        else:
            print("Valor inválido!")

    elif opcao == 3:
        print("========EXTRATO========\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("========================")

    elif opcao == 0:
        break

    else:
        print("Opção inválida!")

