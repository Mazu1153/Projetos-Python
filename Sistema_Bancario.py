menu = '''
[d] - Depósito
[s] - Saque
[e] - Extrato
[x] - Sair

=>>'''

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito no valor{valor:.2f}\n"
        else:
            print("Valor inválido")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Você não possui saldo")

        elif excedeu_limite:
            print("Você excedeu o limite de saldo")

        elif excedeu_saques:
            print("Você excedeu seu limite de saques")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: {valor:.2f}\n"

        else:
            print("Operação inválida")



    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "x":
        break

    else:
        print("Opção inválida, selecione a opção desejada novamente")

       
