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
        print(self.num + self.num2)


    def subtracao(self):
           print(self.num - self.num2)


    def multiplicacao(self):
         print(self.num * self.num2)


    def divisao(self):
         print(self.num / self.num2)

print(logo) 
num = float(input('Digite um numero:'))
op = str(input('O que deseja, [+] [-] [*] [/] :'))
num2 = float(input('Digite um numero:'))



calcular = calculadora(num, num2)

operacao = {'+': calcular.soma, '-':calcular.subtracao, '*':calcular.multiplicacao, '/':calcular.divisao}[op]()
