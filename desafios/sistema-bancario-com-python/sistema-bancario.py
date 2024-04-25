# O sistema terá 3 funções básicas: depósito, saque e ver extrato.

# DEPÓSITO
# A v1 terá apenas um usuário; depósitos serão valores positivos, armazenados em uma variável
# e exibidos na operação de extrato.

# SAQUE
# 3 saques diários com limite máximo de $500.
# Caso o usuário não tenha saldo em conta,
# o sistema deverá exibir uma mensagem informando
# que não será possível sacar dinheiro por falta
# de saldo.
# Os saques devem ser armazenados em uma variável
# e exibidos na operação de extrato.

# EXTRATO
# Essa operação deve listar todos os depósitos
# e saues realizados na conta.
# No fim da listagem deve ser exibido o saldo atual
# da conta.
# No formato R$ xxx.xx, exemplo: R$ 1500.45

menuInicial = """
Selecione uma das opções abaixo:

[1] Depósito
[2] Sacar
[3] Extrato
[s] Sair

"""

saldo = 0
limite = 500
extrato = ""
numeroSaques = 0
LIMITE_SAQUES = 3

print('*** Bem vindo ao DIOBANK ***')

while True:

  opcao = input(menuInicial)

  if opcao == '1': # DEPÓSITO
    valorDeposito = float(input('Digite o valor do seu depósito: '))
    
    if valorDeposito > 0:
      saldo += valorDeposito
      extrato += f'Depósito: R$ {valorDeposito:.2f}\n'
    
    else:
      print("Valor informado inválido.")

  elif opcao == '2': # SAQUE
    valorSaque = float(input('Digite o valor do seu saque: '))

    excedeuSaldo = valorSaque > saldo
    excedeuLimite = valorSaque > limite
    excedeuSaques = numeroSaques > LIMITE_SAQUES

    if excedeuSaldo:
      print("Seu saldo é insuficiente.")

    elif excedeuLimite:
      print("Limite do saque excedido.")
    
    elif excedeuSaques:
      print("Número de saques excedido.")

    elif valorSaque > 0:
      saldo -= valorSaque
      extrato += f'Saque: R$ {valorSaque:.2f}\n'
      numeroSaques += 1

    else:
      print("Valor informado inválido.")
  
  elif opcao == '3': # EXTRATO
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("=========================================")

  elif opcao == 's' or 'S': # SAIR
    break

  else:
    print('Operação inválida. Por favor, selecione novamente a operação desejada.')