"""
@author: Alexandra, Andreia, Catarina, Daniela
"""

'''@package docstring
Implementação de testes a grafos de sobreposição
'''


"""
Class: TestOverlapGraph
"""

import unittest
from overlap_graph import OverlapGraph

class TestOverlapGraph(unittest.TestCase):
    
    def setUp(self):
        self.t1 = OverlapGraph(["ACC", "ATA", "CAT", "CCA", "TAA"], False)
        self.t2 = OverlapGraph(["ATA",  "ACC", "ATG", "ATT", "CAT", "CAT", "CAT", "CCA" , "GCA", "GGC", "TAA", "TCA", "TGG", "TTC", "TTT"], True)
        self.t3 = OverlapGraph(["ACC", "ATA", "CAT", "CCA", "TAA"], True)
 
    def test_check_if_valid_path(self):
        self.assertEqual(self.t1.check_if_valid_path(['ACC−2', 'CCA−8', 'CAT−5', 'ATG−3']), False)
        self.assertEqual(self.t2.check_if_valid_path(['ACC-2', 'CCA-8', 'CAT-5', 'ATG-3', 'TGG-13', 'GGC-10', 'GCA-9', 'CAT-6', 'ATT-4', 'TTT-15', 'TTC-14', 'TCA-12', 'CAT-7', 'ATA-1', 'TAA-11']), True)
        self.assertEqual(self.t3.check_if_valid_path(['ACC-1', 'CCA-4', 'CAT-3', 'ATA-2', 'TAA-5']), True)

    def test_check_if_hamiltonian_path(self):
        self.assertEqual(self.t1.check_if_hamiltonian_path(['ACC−2', 'CCA−8', 'CAT−5', 'ATG−3']), False)
        self.assertEqual(self.t2.check_if_hamiltonian_path(['ACC-2', 'CCA-8', 'CAT-5', 'ATG-3', 'TGG-13', 'GGC-10', 'GCA-9', 'CAT-6', 'ATT-4', 'TTT-15', 'TTC-14', 'TCA-12', 'CAT-7', 'ATA-1', 'TAA-11']), True)
        self.assertEqual(self.t1.check_if_hamiltonian_path(['ACC-1', 'CCA-4', 'CAT-3', 'ATA-2', 'TAA-5']), False)

    def test_search_hamiltonian_path(self):
        self.assertEqual(self.t1.search_hamiltonian_path(), ['ACC', 'CCA', 'CAT', 'ATA', 'TAA'])
        self.assertEqual(self.t2.search_hamiltonian_path(), ['ACC-2', 'CCA-8', 'CAT-5', 'ATG-3', 'TGG-13', 'GGC-10', 'GCA-9', 'CAT-6', 'ATT-4', 'TTT-15', 'TTC-14', 'TCA-12', 'CAT-7', 'ATA-1', 'TAA-11'])
        self.assertEqual(self.t3.search_hamiltonian_path(), ['ACC-1', 'CCA-4', 'CAT-3', 'ATA-2', 'TAA-5'])

    def test_seq_from_path(self):
        self.assertEqual(self.t1.seq_from_path(['ACC', 'CCA', 'CAT', 'ATA', 'TAA']), 'ACCATAA')
        self.assertEqual(self.t2.seq_from_path(['ACC-2', 'CCA-8', 'CAT-5', 'ATG-3', 'TGG-13', 'GGC-10', 'GCA-9', 'CAT-6', 'ATT-4', 'TTT-15', 'TTC-14', 'TCA-12', 'CAT-7', 'ATA-1', 'TAA-11']), 'ACCATGGCATTTCATAA')
        self.assertEqual(self.t1.seq_from_path(['ACC-1', 'CCA-4', 'CAT-3', 'ATA-2', 'TAA-5']), None)
   
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit = False)