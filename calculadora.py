import os
import interface
import FabricaDeOperador as fab

from somar import Somar
from subtrair import Subtrair
from multiplicar import Multiplicar
from dividir import Dividir

'''Classe Calculadora que contém os atributos para ralizar as operações'''
class Calculadora(object):

    def __init__(self, numero1, numero2):
        self.__numero1 = numero1
        self.__numero2 = numero2

    def get_numero1(self):
        return self.__numero1

    def get_numero2(self):
        return self.__numero2

'''Classe responsável por executar a criação dos operadores'''
class executaFabrica(object):
    def fabrica_operador(self, operador: str) -> str:
        operacao = {}
        operacao = fab.FabricarOperador.define_operador(operador)
        return operacao['operacao']

'''Classe responsável por executar as operações'''
class executaCalculo(object):
    def realiza_calculo(self, numero1: int, numero2: int, icalc) -> int:
        operacao = icalc.calcular(self, numero1, numero2)
        return operacao

'''Variáveis globais'''
numero1  = None
numero2  = None
operacao = None
operador = ''

'''Função para limpar tela'''
def limpa_tela():
    os.system('clear')

'''Programa principal'''
def main():

    global numero1, numero2, operador, operacao

    limpa_tela()
    numero1  = input('digite o primeiro numero: ')
    limpa_tela()
    numero2  = input('digite o segundo numero: ')
    limpa_tela()
    operador = input('Digite o operador: ')
    limpa_tela()

    ef = executaFabrica()
    operacao = ef.fabrica_operador(operador)

    
                
if __name__ == '__main__':
    '''Instancia de classes e execução de programa principal'''
    main()
    ec = executaCalculo()
    calc = Calculadora(numero1, numero2)
    numero1 = calc.get_numero1()
    numero2 = calc.get_numero2()

    resultado = ec.realiza_calculo(int(numero1), int(numero2), operacao)
    print(f'{numero1} {operador} {numero2} =', resultado, end=' ') if resultado != None else print('Divisão por 0 é inválida', end='')
