# -- coding: utf-8 --
"""
@author: Alexandra, Andreia, Catarina, Daniela
"""

'''@package docstring
Implementação de testes às tries
'''


"""
Class: TestTrie
"""

import unittest
from trie import Trie

class TestTrie(unittest.TestCase):
    
    def setUp(self):
        self.t1 = Trie(["AGAGAT", "AGC", "AGTCC", "CAGAT", "CCTA", "GAGAT", "GAT", "TC"])
        self.t2 = Trie(["AA", "A", "ACG", "ACT"])
        self.t3 = Trie(["AA", "A", "ACG", "ACT"])
        self.t4 = Trie(["AGAGAT", "AGC", "AGTCC", "CAGAT", "CCTA", "GAGAT", "GAT", "TC"])
        self.t5 = Trie(["AGAGAT", "AGC", "AGTCC", "CAGAT", "CCTA", "GAGAT", "GAT", "TC"])
    
    def test_matches(self):
        self.assertEqual(self.t1.matches("GAGATCCTA"), (False))
        self.assertEqual(self.t2.matches("GAGATCCTA"), (False))
        self.assertEqual(self.t3.matches("ACG"), (True))
        self.assertEqual(self.t4.matches("AGC"), (True))
        self.assertEqual(self.t5.matches("AGC"), (True))
        

    def test_prefix_trie_match(self):
        self.assertEqual(self.t1.prefix_trie_match("GAGATCCTA"), ['GAGAT'])
        self.assertEqual(self.t2.prefix_trie_match("GAGATCCTA"), [])
        self.assertEqual(self.t3.prefix_trie_match("ACG"), ['A', 'ACG'])
        self.assertEqual(self.t4.prefix_trie_match("TGAGTAGCTAGCTAGCAGCCCATCATC"), [])
        self.assertEqual(self.t5.prefix_trie_match("CCTAAGCTAGCTAGCACATC"), ['CCTA'])

    def test_trie_matchesh(self):
        self.assertEqual(self.t1.trie_matches("GAGATCCTA"), [('GAGAT', 0), ('GAT', 2), ('TC', 4), ('CCTA', 5)])
        self.assertEqual(self.t2.trie_matches("GAGATCCTA"), [('A', 1), ('A', 3), ('A', 8)])
        self.assertEqual(self.t3.trie_matches("ACG"), [('A', 0), ('ACG', 0)])
        self.assertEqual(self.t4.trie_matches("TGAGTAGCTAGCTAGCAGCCCATCATC"), [('AGC', 5), ('AGC', 9), ('AGC', 13), ('AGC', 16), ('TC', 22), ('TC', 25)])
        self.assertEqual(self.t5.trie_matches("CCTAAGCTAGCTAGCACATC"), [('CCTA', 0), ('AGC', 4), ('AGC', 8), ('AGC', 12), ('TC', 18)])
   
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit = False)