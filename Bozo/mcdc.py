import unittest
from placar import Placar



class TestPlacarFuncional(unittest.TestCase):
    def setUp(self):
        self.p = Placar()
        
    #PARTE ADICIONADA APOS O MCDC
    #FULL
    def test_full_mcdc_caso4(self):
        self.p = Placar()
        self.p.add(7, [1,1,2,1,1])   
        self.assertEqual(self.p.getScore(), 0)

    def test_full_mcdc_caso6(self):
        self.p = Placar()
        self.p.add(7, [1,2,2,3,3])
        self.assertEqual(self.p.getScore(), 0)

    def test_full_mcdc_caso7(self):
        self.p = Placar()
        self.p.add(7, [1,1,2,3,3])
        self.assertEqual(self.p.getScore(), 0)

    def test_full_mcdc_caso11(self):
        self.p = Placar()
        self.p.add(7, [3, 3, 3, 3, 3]) 
        self.assertEqual(self.p.getScore(), 15)

    def test_seq_mcdc_caso1(self):
        self.p = Placar()
        self.p.add(8, [1, 2, 3, 4, 4])
        self.assertEqual(self.p.getScore(), 0)

    def test_seq_mcdc_caso2(self):
        self.p = Placar()
        self.p.add(8, [1, 2, 3, 5, 6])
        self.assertEqual(self.p.getScore(), 0)

    def test_seq_mcdc_caso3(self):
        self.p = Placar()
        self.p.add(8, [1, 3, 4, 5, 6])
        self.assertEqual(self.p.getScore(), 0)
    
    def test_quadra_mcdc_tresrepetidos(self):
        self.p = Placar()
        self.p.add(9, [4,4,4,1,2])
        self.assertEqual(self.p.getScore(), 0)

    def test_quadra_mcdc_normal(self):
        self.p = Placar()
        self.p.add(9, [1,1,1,1,2])
        self.assertEqual(self.p.getScore(), 30)

    def test_quadra_mcdc_tresrepetidos1(self):
        self.p = Placar()
        self.p.add(9, [1, 1, 1, 4, 4])
        self.assertEqual(self.p.getScore(), 0)

    def test_general_mcdc_quebra1(self):
        self.p = Placar()
        self.p.add(10, [6,6,6,1,6])
        self.assertEqual(self.p.getScore(), 0)

    def test_general_mcdc_quebra2(self):
        self.p = Placar()
        self.p.add(10, [6,6,1,6,6])
        self.assertEqual(self.p.getScore(), 0)

    def test_general_mcdc_quebra3(self):
        self.p = Placar()
        self.p.add(10, [6,1,6,6,6])
        self.assertEqual(self.p.getScore(), 0)



if __name__ == "__main__":
    unittest.main(verbosity=2)
