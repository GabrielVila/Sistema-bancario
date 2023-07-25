from funcionalidades_banco import *
from clientes import *

saldo = 0
numero_saques = 0
limite_saques_global = 3
extrato_global = []

def saque_funcao():
    global saldo, extrato_global, numero_saques
    saldo, extrato_global, numero_saques = saque(
        saldo=saldo, 
        extrato=extrato_global, 
        numero_saques=numero_saques, 
        limite_saques=limite_saques_global
    )

def deposito_funcao():
    global saldo, extrato_global
    saldo, extrato_global = deposito(saldo, extrato_global)

def extrato_funcao():
    global saldo, extrato_global
    saldo, extrato_global = exibir_extrato(
            saldo,
            extrato=extrato_global
    )

def opcao_invalida():
    print("Por favor, digite um número de 1 a 7 para selecionar uma ação.")


menu_options = {
    1: saque_funcao,
    2: deposito_funcao,
    3: extrato_funcao,
    4: criar_usuario,
    5: criar_conta,
    6: visualizar_conta,
    7: lambda: print("Muito obrigado! Esperamos vê-lo novamente em breve!"),
}