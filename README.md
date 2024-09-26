Sobre o desafio:

Um banco precisa renovar seu sistema bancário e contratou nossos serviços para melhorar e emplementar novos recursos.
A primeira estapa do projeto basea-se em criar um programa que possibilita ao usuário depositar, sacar e ver o extrato de todas as transações feitas.
Sendo assim:

Depositar:
* Ser possível depositar valores positivos. 
* A versão 1 tabalhará com apenas um usuário.
* Todos os depósitos devem ser armazenados em uma variável e exibidas na operação "extrato".

Sacar:
* O saque terá limite de 3 saques por dia.
* limite diário de R$500,00.
* Caso o saldo seja insuficiente, uma mensagem deverá ser exibida.
* Assim como no depósito, todos os saques deverão ser armazenados em uma variável e exibidas na operação "extrato".

Extrato:
* Deve listar toda a movimentação ocorrida na conta bancária (depósitos e saques).
* O valor deverá ser exibido em "R$...,..".


Iniciando o código:

Por sugestão do bootcamp iniciamos com essa base:

menu = """

[d] depositar
[s] sacar
[e] extrato
[q] sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

While True:

  opcao = input(menu)

  if opcao == "d":
    print("Extrato")

  elif opcao == "s":
    print("Saque")

  elif opcao == "e":
    print("Extrato")

  elif opcao == "q":
    break

  else:
  print("Opção inválida!")
  



Lembrando que essa é apenas uma base e segui-la não é obrigatório!
O importante é fazer um sistema bancário de maneira que ele funcione de acordo com as lógicas da vida real.
