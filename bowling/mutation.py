#Gabriela Passos de Andrade - 12625142
#Rafael Cunha Bejes Learth -13676367
#Emanuel Percinio Gonçalves de Oliveira - 13676878
import unittest
from placar import Placar


class TestPlacarMutation(unittest.TestCase):
    def setUp(self):
        self.p = Placar()
    def test_estado_inicial_placar_tem_dez_em_todas_posicoes(self):
        for i in range(self.p.POSICOES):
            self.assertEqual(self.p.placar[i], 0)
            self.assertFalse(self.p.getTaken(i))
    
    def testa_str_formato_inicial(self):
        s = str(self.p)
        esperado = ''
        for i in range(3):
            esperado += "({:1d}) ".format(i+1) + "   |   "
            esperado += "({:1d}) ".format(i+7) + "   |  "
            esperado += "({:1d}) ".format(i+4) + "\n-------|----------|-------\n"
        esperado += "       |   " + "({:2d})".format(10)  + "   |"
        esperado += "\n       +----------+\n"
        self.assertEqual(s, esperado)
    
    def test_posicao_fora_do_intervalo_abaixo(self):
       with self.assertRaisesRegex(IndexError, "Valor da posição no placar é ilegal"):
           self.p.add(0, [1, 2, 3, 4, 5])

    def test_add_posicao_ocupada_lanca_ValueError(self):
        self.p.add(4, [1, 1, 1, 1, 1])
        with self.assertRaisesRegex(ValueError, "Posição ocupada no placar"):
            self.p.add(4, [2, 2, 2, 2, 2])
    
    def test_add_posicao_invalida_lanca_IndexError(self):
        with self.assertRaisesRegex(IndexError, "Valor da posição no placar é ilegal"):
            self.p.add(0, [2, 2, 2, 2, 2])  

        with self.assertRaisesRegex(IndexError, "Valor da posição no placar é ilegal"):
            self.p.add(self.p.POSICOES + 1, [2, 2, 2, 2, 2])

    def test_getTaken(self):
        p = Placar()
        p.add(1, [1, 1, 1, 1, 1])
        self.assertTrue(p.getTaken(0))

    def test_full_valido_1(self):
        dados = [2, 2, 2, 5, 5]
        self.assertEqual(self.p.checkFull(dados), 1)

    def test_full_invalido_2(self):
        dados = [1, 2, 5, 5, 5]
        self.assertEqual(self.p.checkFull(dados), 0)
    
    def test_quadra_invalida_1(self):
        dados = [1, 4, 4, 4, 5]
        self.assertEqual(self.p.checkQuadra(dados), 0)

    def test_quina_invalida_1(self):
        dados = [1, 4, 4, 4, 4]
        self.assertEqual(self.p.checkQuina(dados), 0)
    
    def test_quina_invalida_2(self):
        dados = [1, 1, 4, 4, 4]
        self.assertEqual(self.p.checkQuina(dados), 0)
    
    def test_quina_invalida_3(self):
        dados = [4, 4, 4, 5, 4]
        self.assertEqual(self.p.checkQuina(dados), 0)
    
    def test_quadra_valida_1(self):
        dados = [1, 4, 4, 4, 4]
        self.assertEqual(self.p.checkQuadra(dados), 1)
    
    def test_quadra_ivalida_2(self):
        dados = [1, 4, 4, 4, 5]
        self.assertEqual(self.p.checkQuadra(dados), 0)
    
    """ Novos """
    def test_quina_invalida_4(self):
        dados = [4, 4, 4, 4, 5]
        self.assertEqual(self.p.checkQuina(dados), 0)
    
    def test_quina_invalida_5(self):
        dados = [4, 4, 5, 4, 4]
        self.assertEqual(self.p.checkQuina(dados), 0)
    
    def test_quina_invalida_5(self):
        dados = [4, 5, 5, 4, 4]
        self.assertEqual(self.p.checkQuina(dados), 0)
    
    def test_quina_invalida_6(self):
        dados = [4, 4, 4, 5, 5]
        self.assertEqual(self.p.checkQuina(dados), 0)
    
    def test_quina_invalida_6(self):
        dados = [5, 4, 4, 4, 4]
        self.assertEqual(self.p.checkQuina(dados), 0)

    def test_quina_invalida_7(self):
        dados = [5, 5, 4, 4, 4]
        self.assertEqual(self.p.checkQuina(dados), 0)
    
    def test_quina_invalida_8(self):
        dados = [5, 5, 5, 4, 4]
        self.assertEqual(self.p.checkQuina(dados), 0)

    def test_quina_invalida_10(self):
        dados = [1, 1, 1, 2, 2]
        self.assertEqual(self.p.checkQuina(dados), 0)
    
    def test_getScore_com_k(self):
        self.p.add(1, [1, 1, 1, 1, 1])
        self.p.add(2, [2, 2, 2, 2, 2])
        self.assertEqual(self.p.getScore(0), 5)
        self.assertEqual(self.p.getScore(1), 10)

    def test_seqMaior_invalida_1(self):
        dados = [1, 2, 4, 5, 6]
        self.assertEqual(self.p.checkSeqMaior(dados), 0)
    
    def test_seqMaior_invalida_2(self):
        dados = [1, 2, 2, 3, 4]
        self.assertEqual(self.p.checkSeqMaior(dados), 0)
    
    def test_seqMaior_invalida_3(self):
        dados = [1, 2, 3, 3, 4]
        self.assertEqual(self.p.checkSeqMaior(dados), 0)
    
    def test_seqMaior_invalida_4(self):
        dados = [1, 2, 3, 4, 6]
        self.assertEqual(self.p.checkSeqMaior(dados), 0)
    
    def test_taken_invalid(self):
        self.p.add(1, [2, 3, 4, 5, 6])
        self.assertTrue(self.taken[0])

if __name__ == "__main__":
    unittest.main(verbosity=2)