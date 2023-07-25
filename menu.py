from funcionalidades_tela import *

while True:
    opcao = int(input("""\nInforme um número sendo:\n
1 - Saque
2 - Depósito
3 - Extrato
4 - Criar um novo usuário 
5 - Criar uma nova conta corrente
6 - Visualizar a conta
7 - Sair\n"""))
    
    funcao_selecionada = menu_options.get(opcao, opcao_invalida)
    funcao_selecionada()
    
    if opcao == 7:
        break
