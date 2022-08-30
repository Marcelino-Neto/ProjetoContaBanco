cpf = '11122233345'
senha = '5678'
a = 0
b = 0
while (a != cpf and b != senha):
    a = str(input('Digite seu cpf:'))
    b = str(input('Senha: '))

    if a != cpf and b != senha:
        print("Acesso Negado")
    else:
        print("Acesso Aprovado")

class conta:
    def __init__(self, cliente, cpf, numero, saldo):
        self.cliente = cliente
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo

    def Menu(self):

        print(' MENU ')

        print('Opções:')
        print('1 - Extrato')
        print('2 - Depósito')
        print('3 - Saque')
        print('4 - Transferência')
        print('5 - Sair')
        opcao = input('Digite a opção desejada: ')
        if opcao == '1':
            self.Extrato()

        elif opcao == '2':
            valor = float(input('Digite o valor a ser depositado: '))
            self.deposita(valor)

        elif opcao == '3':
            valor = float(input('Digite o valor do saque: '))
            self.saca(valor)

        elif opcao == '4':
             valor = float(input('Digite o valor da transferência:'))
             self.transfere(ContaDestino,valor)

        elif opcao == '5':
            print('Programa encerrado, volte sempre!')
            exit()

    def Extrato(self):

        print(f'CLIENTE - {self.cliente}')
        print(f'NÚMERO DA CONTA - {self.numero}')
        print(f'SALDO: R$ {self.saldo}')

        aperte = input('Aperte M para retornar ao MENU ou (X) para sair: ')
        if aperte == 'X' or aperte == 'x':
            print('Programa encerrado, volte sempre!')
            exit()
        else:
            self.Menu()

    def rendimento(self):
        self.saldo = self.saldo + self.saldo/100

    def imprimeSaldo(self):
        print("Saldo: R$ %.2f " %self.saldo)

    def saca(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print('Saque feito!')
            return True
        else:
            print("Saldo insuficiente.")
            return False
    def deposita(self, valor):
        self.saldo += valor

    def transfere(self, ccdestino, valor):
        if self.saca(valor) == True:
           ccdestino.deposita(valor)
           print('Transferencia concluida!')
           return True
        else:
            print("Transferência Recusada")
            return False

ContaPoupanca = conta('Marcelino', 11122233345, 3333456, 5000)
ContaCorrente = conta('Marcelino', 11122233345, 3333456, 1000)
ContaDestino = conta('joão', '55566677784', 2213456, 6000)

while True:
    print('TIPO DE CONTA')
    print('1 - Conta Poupança')
    print('2 - Conta Corrente')
    TipoConta = int(input('Digite 1 para conta poupança ou 2 para conta corrente:'))
    if(TipoConta == 1):
        ContaPoupanca.rendimento()
        while True:
            ContaPoupanca.Menu()
    elif(TipoConta == 2):
        while True:
            ContaCorrente.Menu()
    else:
        print('Inválido')
