lista_usuarios = []
lista_contas = []

def criar_usuario():
    nome = input("Informe o seu nome: ")
    nascimento = input("Informe a data de seu nascimento: ")

    cpf = cpf_exception()

    if verificar_existencia("cpf", cpf, lista_usuarios):
        print("Usuário já cadastrado.\n")
        return        

    endereco = input("Informe seu Endereço: ")
    

    while True:
            cidade = input("Informe a sua cidade em sigla (Ex: RJ): ")
            if len(cidade) > 3:
                print("Cidade inválida. Digite a sigla da cidade (Ex: RJ).")
            else:
                break    

    usuario = {
        "nome": nome,
        "data_nascimento": nascimento,
        "cpf": cpf,
        "endereco": endereco     
        }
    
    lista_usuarios.append(usuario)
    print("Usuário criado com sucesso! \n")
    
    



def criar_conta():

    cpf = cpf_exception()
    
    if verificar_existencia("cpf", cpf, lista_usuarios) == False:
        print("Usuário não encontrado no banco. Por favor, crie um novo usuário para prosseguir.\n")
        return        
    
    conta = {
            "agencia": "0001",
            "numero_conta": len(lista_contas) + 1,
            "usuario": cpf
        }

    lista_contas.append(conta)
    print(f"\nConta criada com sucesso!\n")
    print(f"""\n
    Agência:\t\t{conta['agencia']}
    C/C:\t\t{conta['numero_conta']}
    CPF Titular:\t{conta['usuario']}
            \n
        """)
    


def visualizar_conta():

    cpf = cpf_exception()
    if verificar_existencia("usuario", cpf, lista_contas) == False:
        print("Conta não encontrada no banco. Por favor, verifique o número da conta ou crie uma nova conta.\n")
        return        
    
    for conta in lista_contas:
        if conta["usuario"] == cpf:
            print(f"""\n
    Agência:\t\t{conta['agencia']}
    C/C:\t\t{conta['numero_conta']}
    CPF Titular:\t{conta['usuario']}
            \n
        """)   





def cpf_exception():
    while True:
        cpf = input("Informe o seu CPF (apenas números): ")
        if not cpf.isdigit() or len(cpf) != 11:
            print("CPF inválido. O CPF deve conter exatamente 11 dígitos numéricos.")
        else:
            return int(cpf)




def verificar_existencia(chave, valor, lista):
    for item in lista:
        if item[chave] == valor:
            return True
    return False