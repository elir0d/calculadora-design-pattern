from ast import If
from pprint import pprint
import unittest
import FabricaDeOperador as fab
import calculadora as calc
import somar, subtrair, multiplicar, dividir

ef = calc.executaFabrica()
class Testes(unittest.TestCase):
    def test_deveria_somar_dois_numeros_e_retornar_10(self):
        operacao = ef.fabrica_operador('+')
        self.assertEqual(calc.executaCalculo.realiza_calculo(self, 5, 5, operacao), 10)

    def test_deveria_subtrair_3_de_6_e_retornar_3(self):
        operacao = ef.fabrica_operador('-')
        self.assertEqual(calc.executaCalculo.realiza_calculo(self, 6, 3, operacao), 3)

    def test_deveria_multiplicar_dois_numeros_e_retornar_50(self):
        operacao = ef.fabrica_operador('*')
        self.assertEqual(calc.executaCalculo.realiza_calculo(self, 10, 5, operacao), 50)

    def test_deveria_dividir_dois_numeros_e_retornar_5(self):
        operacao = ef.fabrica_operador('/')
        self.assertEqual(calc.executaCalculo.realiza_calculo(self, 25, 5, operacao), 5)

    def test_deveria_retornar_None_para_divisoes_por_0(self):
        operacao = ef.fabrica_operador('/')
        self.assertEqual(calc.executaCalculo.realiza_calculo(self, 0, 0, operacao), None)
        self.assertEqual(calc.executaCalculo.realiza_calculo(self, 2, 0, operacao), None)

    def test_deveria_criar_a_operacao_de_somar_e_retornar_um_dicionario(self):
        operacao = fab.FabricarOperador.define_operador('+')
        self.assertEqual(operacao, {'operador':'+', 'operacao': somar.Somar})
        self.assertTrue(isinstance(operacao, dict))
   
    def test_deveria_criar_a_operacao_de_subtrair_e_retornar_um_dicionario(self):
        operacao = fab.FabricarOperador.define_operador('-')
        self.assertEqual(operacao, {'operador':'-', 'operacao': subtrair.Subtrair})
        self.assertTrue(isinstance(operacao, dict))
   
    def test_deveria_criar_a_operacao_de_multiplicar_e_retornar_um_dicionario(self):
        operacao = fab.FabricarOperador.define_operador('*')
        self.assertEqual(operacao, {'operador':'*', 'operacao': multiplicar.Multiplicar})
        self.assertTrue(isinstance(operacao, dict))
   
    def test_deveria_criar_a_operacao_de_dividir_e_retornar_um_dicionario(self):
        operacao = fab.FabricarOperador.define_operador('/')
        self.assertEqual(operacao, {'operador':'/', 'operacao': dividir.Dividir})
        self.assertTrue(isinstance(operacao, dict))
        
    def test_deveria_criar(self):
        if(True): return print("teste concluido")

def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Testes)
    unittest.TextTestRunner(verbosity=2,failfast=False).run(suite)

if __name__ == '__main__':
    runTests()

