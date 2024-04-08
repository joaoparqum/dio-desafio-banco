AGENCIA = "0001"
LIMITE_SAQUE = 3

saldo = 0
limite = 500
extrato = " "
numero_saques = 0
opcao = -1
usuarios = []
contas = []

def sacar_dinheiro(*,saldo,saque,extrato,limite,numero_saques,limite_saques):

    if saque > saldo:
        print("Não será possivel fazer o saque, saldo insuficiente!!")
    elif saque > limite:
        print("O valor do saque está maior que o limite!") 
    elif numero_saques >= limite_saques:
        print("Não é possível fazer mais saques! Limite diário excedido!")
    elif saque > 0:
        saldo -= saque
        extrato += f"Você fez o saque de R$ {saque:.2f} reais\n"
        numero_saques += 1
    else:
        print("Valor inválido!") 
    return saldo, extrato

def depositar_dinheiro(saldo,valor,extrato,/):

    if valor > 0:
        saldo += valor
        extrato += f"Foi depositado R$ {valor:.2f} reais\n"
    elif valor < 0:
        print("Valor inválido!")
    return saldo, extrato

def mostrar_extrato(saldo,/,*,extrato):
    print("========EXTRATO========\n")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("========================")

def criar_usuario(usuarios):
    print("========CADASTRO DE USUÁRIO========\n")
    cpf = int(input("Digite seu CPF:\n"))
    usuario = valida_usuario(cpf, usuario)

    if usuario:
        print("Usuário já existente!")

    nome = input("Digite seu nome:\n")
    data_nasc = input("Digite sua data de nascimento:\n")
    endereco = input("Digite seu endereço: Ex: Rua/Numero/Bairro/Cidade-Sigla do estado\n")

    usuarios.append({"nome":nome,"cpf":cpf,"data_nasc":data_nasc,"endereco":endereco})
    print("Usuário cadastrado com sucesso!\n")

def valida_usuario(cpf, usuarios):
    usuarios_validados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_validados[0] if usuarios_validados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = int(input("Digite o CPF do usuário:"))
    usuario = valida_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!\n")
        return {"agencia":agencia,"numero_conta":numero_conta,"usuario":usuario}
    
    print("Usuário não encontrado! Cadastre uma conta!\n")

while opcao != 0:
    opcao = int(input("""
    ======== Banco ========
    Selecione uma opção:
    [1] - Depositar                  
    [2] - Sacar
    [3] - Extrato
    [4] - Cadastrar usuário
    [5] - Cadastrar conta bancária                                    
    [0] - Sair
    =======================
    """                                                  
    ))
    
    if opcao == 1:
        valor = float(input("Digite o valor para depositar: "))
        saldo, extrato = depositar_dinheiro(saldo=saldo,valor=valor,extrato=extrato)

    elif opcao == 2:
        saque = float(input("Digite o valor para sacar: "))
        saldo, extrato = sacar_dinheiro(saldo=saldo,saque=saque,extrato=extrato,limite=limite,numero_saques=numero_saques,limite_saques=LIMITE_SAQUE)

    elif opcao == 3:
        mostrar_extrato(saldo, extrato=extrato)
    
    elif opcao == 4:
        criar_usuario(usuarios)

    elif opcao == 5:
        numero_conta = len(contas)+1
        conta = criar_conta(AGENCIA,numero_conta,usuarios)
        if conta:
            contas.append(conta)

    elif opcao == 0:
        break

    else:
        print("Opção inválida!")

