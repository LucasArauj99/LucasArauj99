import os

logo = '''
 _____________________
|  _________________  |
| |                 | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''

class calculadora:
    def __init__(self, num, num2) -> None:
        self.num = num 
        self.num2 = num2

    def soma(self):
        return self.num + self.num2

    def subtracao(self):
        return self.num - self.num2

    def multiplicacao(self):
        return self.num * self.num2


    def divisao(self):
        return self.num / self.num2
print(logo)
while True:
    num = float(input('Digite um numero:'))
    nova_conta = True
    while nova_conta:
        op = str(input('O que deseja, [+] [-] [*] [/] :'))
        num2 = float(input('Digite um numero:'))

        calcular = calculadora(num, num2)

        operacao = {'+': calcular.soma, '-':calcular.subtracao, '*':calcular.multiplicacao, '/':calcular.divisao}[op]()
        print(f'resultado: {operacao}')
        conf = str(input('Deseja continuar?\n[S] sim \n[N] nova conta\n[F] Sair:')).upper()[0]
        if conf == 'S':
            num = operacao
        elif conf == 'N':
            os.system('cls')
            nova_conta = False

        else:
            nova_conta = False
    if conf == 'F':
        break
    