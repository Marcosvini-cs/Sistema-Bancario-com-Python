menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[i] Informações
[q] Sair

=> '''

saldo = 0
limite = 500
extrato = ''''''
numero_saques = 0
limite_saques = 3

while True:
    opcao = input(menu)

    match opcao:
        case 'd':
            valor = float(input('Informe o valor do depósito: '))

            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R${valor:.2f}\n"

            else:
                print('-=-'*16)
                print("Operação falhou! O valor informado é inválido.")
                print('-=-'*16)

        case 's':
            if numero_saques == limite_saques:
                print('Você atingiu o limite de saques.')
                continue

            print(f'|Seu saldo: R${saldo:.2f}|')

            valor_saque = float(input('Informe o valor do saque: '))

            if valor_saque <= saldo:
                if valor_saque <= limite:
                    saldo -= valor_saque
                    extrato += f'Saque: R${valor_saque:.2f}\n'
                    numero_saques += 1
                else:
                    print('-=-'*21)
                    print('Operação falhou! O valor informado extrapola limite por saque.')
                    print('-=-'*21)

            else:
                print('-=-'*18)
                print('Operação falhou! O valor informado extrapola seu saldo')
                print('-=-'*18)

        case 'e':
            if extrato:
                print("\n================ EXTRATO ================")
                print(extrato)
                print("==========================================")
            else: 
                print('Ainda não ocorreu nenhuma movimentação.')

        case 'i':
            print('''- O limite por saque é R$500,00
- Só pode ser realizado 3 saques diários''')

        case 'q':
            break

        case e:
            print('-=-'*23)
            print('Operação inválida, por favor selecione novamente a operação desejada.')
            print('-=-'*23)