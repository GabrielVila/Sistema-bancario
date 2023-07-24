from funcionalidades import *

opcao = 0
saldo = [2000]
extrato = [saldo[0]]
repeticao = 0



while opcao != 4:
    opcao = int(input("Informe um número sendo:\n1 - Saque\n2 - Deposito\n3 - Extrato\n4 - Para sair\n"))
    if opcao == 1:
        if(repeticao < 3):
            saldo = saque(saldo)
            saldo_str = str(saldo[0])
            extrato.append(saldo_str)
            repeticao += 1
        else:
            print("Limite de saque atingido\n")
            pass
    elif opcao == 2:
        saldo = deposito(saldo)
        saldo_str = str(saldo[0])
        extrato.append(saldo_str)
    elif opcao == 3:
        for i, valor in enumerate(extrato):
            print(f'{i + 1}° operação --- R$ {valor}')
else:
    print("Obrigado, volte sempre!")
    

    

