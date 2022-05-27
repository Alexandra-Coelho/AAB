"""
@author: Alexandra, Andreia, Catarina, Daniela
"""

'''@package docstring
Implementação de testes a grafos DeBruijn
'''


"""
Class: TestMyGraph
"""

import unittest
from debruijn import DeBruijnGraph

class TestMyGraph(unittest.TestCase):
    
    def setUp(self):
        self.t1 = DeBruijnGraph([ "ATA", "ACC", "ATG", "ATT", "CAT", "CAT", "CAT", "CCA", "GCA", "GGC", "TAA", "TCA", "TGG", "TTC", "TTT"])
        self.t2 = DeBruijnGraph(['AAT', 'ATG', 'ATG', 'CAA', 'CTG', 'GCA', 'GGT', 'GTC', 'TCT', 'TGC', 'TGG'])
 
    def test_check_nearly_balanced_graph(self):
        self.assertEqual(self.t1.check_nearly_balanced_graph(), ('AC', 'AA'))
        self.assertEqual(self.t2.check_nearly_balanced_graph(), ('AT', 'TG'))

    def test_eulerian_path(self):
        self.assertEqual(self.t2.eulerian_path(), ['AT', 'TG', 'GG', 'GT', 'TC', 'CT', 'TG', 'GC', 'CA', 'AA', 'AT', 'TG'])

    def test_seq_from_path(self):
        self.assertEqual(self.t1.seq_from_path(['AC', 'CC', 'CA', 'AT', 'TG', 'GG', 'GC', 'CA', 'AT', 'TT', 'TT', 'TC', 'CA', 'AT', 'TA', 'AA']), 'ACCATGGCATTTCATAA')
        self.assertEqual(self.t2.seq_from_path(['AT', 'TG', 'GC', 'CA', 'AA', 'AT', 'TG', 'GG', 'GT', 'TC', 'CT', 'TG']), 'ATGCAATGGTCTG')

    def test_is_connected(self):
        self.assertEqual(self.t1.is_connected(), False)
        self.assertEqual(self.t2.is_connected(), True)

   
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit = False)