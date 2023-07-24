def saque(saldo):
    while True:
        if saldo[0] <= 0:
            print("Valor de saque indisponível")
        else:
            saque_str = input("Informe o valor do saque: ")
            if "," in saque_str:
                saque_str = saque_str.replace(",", ".")
            saque = float(saque_str)
            if saque <= 0 or saque > 500 or saque > saldo[0]:
                print(f"Não foi possível realizar o saque de R$ {saque}")
            else:
                saldo[0] -= saque
                print(f"Saque realizado com sucesso, você tem R$ {saldo[0]}, em sua conta")
                break
    return saldo




def deposito(saldo):
    valorDepositado = float(input("Informe o valor que deseja depositar: "))
    if valorDepositado <= 0:
        print("Valor inválido")
    else:
        saldo[0] += valorDepositado
        print(f"Deposito realizado com sucesso, você tem R$ {saldo[0]}, em sua conta")
    return saldo



