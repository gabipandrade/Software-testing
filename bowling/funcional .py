import unittest
from placar import Placar


class TestPlacarFuncional(unittest.TestCase):
    def setUp(self):
        self.p = Placar()


    def test_estado_inicial_score_zero(self):
        self.assertEqual(self.p.getScore(), 0)
        for i in range(10):
            self.assertFalse(self.p.getTaken(i))

    def test_uns(self):
        self.p.add(1, [1, 1, 2, 4, 6])  
        self.assertEqual(self.p.getScore(), 2)
    
    def test_dois(self):
        self.p.add(2, [1, 1, 2, 2, 6])  
        self.assertEqual(self.p.getScore(), 4)
    
    def test_tres(self):
        self.p.add(3, [1, 3, 2, 3, 3])  
        self.assertEqual(self.p.getScore(), 9)
    
    def test_quatros(self):
        self.p.add(4, [1, 2, 4, 4, 4])  
        self.assertEqual(self.p.getScore(), 12)
    
    def test_cincos(self):
        self.p.add(5, [1, 2, 2, 5, 5])  
        self.assertEqual(self.p.getScore(), 10)
    
    def test_seis(self):
        self.p.add(6, [6, 6, 6, 1, 2])  
        self.assertEqual(self.p.getScore(), 18)

    def test_uns_invalido(self):
        self.p.add(1, [6, 6, 6, 2, 2])  
        self.assertEqual(self.p.getScore(), 0)


    def test_full_valido(self):
        self.p.add(7, [2, 2, 3, 3, 3])  
        self.assertEqual(self.p.getScore(), 15)

    def test_full_invalido(self):
        self.p.add(7, [2, 2, 2, 3, 4])  
        self.assertEqual(self.p.getScore(), 0)

    def test_sequencia_maior(self):
        self.p.add(8, [2, 3, 4, 5, 6])
        self.assertEqual(self.p.getScore(), 20)
    
    def test_sequencia_menor(self):
        self.p.add(8, [1, 2, 3, 4, 5])
        self.assertEqual(self.p.getScore(), 20)

    def test_sequencia_invalida(self):
        self.p.add(8, [1, 1, 2, 3, 4])  
        self.assertEqual(self.p.getScore(), 0)

    def test_quadra_valida(self):
        self.p.add(9, [4, 4, 4, 4, 1])
        self.assertEqual(self.p.getScore(), 30)

    def test_quadra_invalida(self):
        self.p.add(9, [4, 4, 4, 1, 1])
        self.assertEqual(self.p.getScore(), 0)

    def test_general_valido(self):
        self.p.add(10, [5, 5, 5, 5, 5])
        self.assertEqual(self.p.getScore(), 40)

    def test_general_invalido(self):
        self.p.add(10, [5, 5, 5, 5, 4])
        self.assertEqual(self.p.getScore(), 0)

    def test_pontuacao_acumulada(self):
        self.p.add(1, [1, 1, 3, 5, 6])      
        self.p.add(7, [2, 2, 3, 3, 3])      
        self.p.add(9, [6, 6, 6, 6, 2])      
        self.p.add(10, [4, 4, 4, 4, 4])     
        self.assertEqual(self.p.getScore(), 87)

    def test_posicao_fora_do_intervalo_abaixo(self):
       with self.assertRaises(IndexError):
           self.p.add(0, [1, 2, 3, 4, 5])
    
    def test_posicao_fora_do_intervalo_acima(self):
       with self.assertRaises(IndexError):
           self.p.add(11, [1, 2, 3, 4, 5])

    def test_adicionar_posicao_duas_vezes(self):
       self.p.add(1, [1, 1, 2, 3, 4])
       with self.assertRaises(ValueError):
           self.p.add(1, [1, 1, 1, 1, 1])

    def test_get_score_por_indice(self):
        self.p.add(6, [6, 6, 6, 1, 2])  
        self.assertEqual(self.p.getScore(5), 18)  

    def test_get_name_ordem(self):
        esperados = ["Ones", "Twos", "Threes", "Fours", "Fives",
                     "Sixes", "Full", "Sequence", "Four of a kind", "General"]
        self.assertEqual([self.p.getName(i) for i in range(10)], esperados)

    
    
    # PARTE ADICIONADA APOS O COVERAGE
    def test_str_repr(self):
        self.p.add(1, [1, 1, 2, 3, 4])
        self.p.add(10, [5, 5, 5, 5, 5])
        
        resultado = str(self.p)
        self.assertIsInstance(resultado, str)
        self.assertIn(" 2 ", resultado)
        self.assertIn("40", resultado)
        self.assertIn("(2)", resultado)
        self.assertIn("(9)", resultado)
    
    def test_uma_linha_nove(self):
        linha = self.p.uma_linha(9)
        self.assertIn("(10)", linha)  
        self.p.add(10, [6, 6, 6, 6, 6])
        linha_taken = self.p.uma_linha(9)
        self.assertIn("40", linha_taken)  




if __name__ == "__main__":
    unittest.main(verbosity=2)
