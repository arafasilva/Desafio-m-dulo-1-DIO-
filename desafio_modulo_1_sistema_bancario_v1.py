menu = """

[d] depositar
[s] sacar 
[e] extrato
[q] sair 

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3 

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor de depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito de: R${valor:.2f}\n"

        else:
            print("Operação inválida! Tente novamente.")
        
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saque >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente!")

        elif excedeu_limite:
            print("Valor limite diário de saque excedido!")

        elif excedeu_saques:
            print("Limite diário de saques ultrapassado!")

        elif valor > 0:
            print(f"Saque de R${valor:.2f} realizado com sucesso!\n")
            saldo -= valor
            extrato += f"Saque de: R${valor:.2f}\n"
            numero_saque += 1

        else:
            print("Operação inválida! Por favor, digite um valor válido.")

    elif opcao == "e":
        print("\n ======== Extrato ========")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("==========================")

    elif opcao == "q":
        print(f"Obrigada por utilizar nossos serviços!")
        break

    else:
        print("Opção inválida, por favor selecione novamente a opção desejada.")


