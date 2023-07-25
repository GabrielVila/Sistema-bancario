def saque(*, saldo, extrato, numero_saques, limite_saques ):

    saques_atingidos = numero_saques >= limite_saques
    saques_restantes = limite_saques - (numero_saques + 1) 
                
    while True:
        if saldo <= 0:
            print("Deposite algum valor em sua conta para conseguir realizar o saque!")
            break
        elif saques_atingidos:
            print("Limite de saque atingido :(\n")
            break
        else:
            saque = float(input("Informe o valor do saque: "))

            if saque <= 0 or saque > saldo:
                print(f"Não foi possível realizar o saque de R$ {saque:.2f}")  

            else:
                saldo -= saque
                if(saques_restantes == 0):
                    print(f"Saque realizado com sucesso! Seu saldo atual é de R$ {saldo:.2f}. Este foi o último saque disponível no dia.")
                else:
                    print(f"Saque realizado com sucesso! Seu saldo atual é de R$ {saldo:.2f}. Você ainda pode realizar mais {saques_restantes} saques hoje.")
                extrato += f"Saque:\t\tR$ {saque:.2f}\n"
                numero_saques += 1
                break
    return saldo, extrato, numero_saques




def deposito(saldo, extrato, /):
    valorDepositado = float(input("Informe o valor que deseja depositar: "))
    if valorDepositado <= 0:
        print("Valor inválido")
    else:
        saldo += valorDepositado
        extrato += f"Depósito:\tR$ {valorDepositado:.2f}\n"
        print(f"Deposito realizado com sucesso, você tem R$ {saldo:.2f}, em sua conta")
    return saldo, extrato



def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Nenhuma movimentação registrada." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")
    return saldo, extrato