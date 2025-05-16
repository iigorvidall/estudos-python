saldo = 1000
user_name = input("Bem vindo ao branco plimbank \nDigite seu nome:")

while True:
    print("=====================================")
    user_select = input(f"Olá {user_name}, oque deseja fazer? \n\n1 - Depositar \n2 - Sacar \n3 - Ver saldo \n4 - Transferir\n5 - Sair\n")
    print("=====================================")

    if user_select == "1":
        novo_deposito = float(input("Digite o valor a ser depositado: "))
        saldo = saldo + novo_deposito
        print(f"Seu novo saldo é: R${saldo:.2f}")
        
    elif user_select == "2":
        novo_saque = float(input("Digite o valor para o saque: "))
        saldo = saldo - novo_saque
        print(f"Seu novo saldo é: R${saldo:.2f}")
    elif user_select == "3":
        (print(f"Seu saldo atual é: R${saldo:.2f}"))
    elif user_select == "4":
        user_transfer = input("Para quem deseja transferir?\n")
        user_transfer_saldo = float(input(f"Digite o valor a ser transferido: "))
        saldo = saldo - user_transfer_saldo
        print("--------------")
        print(f"Foi transferido R${user_transfer_saldo:.2f} para {user_transfer}\n Seu saldo atual é de: R${saldo:.2f}")
        print("--------------")
    elif user_select == "5":
        print("Encerrando sua sessão...")
        print("...")
        print("...")
        break