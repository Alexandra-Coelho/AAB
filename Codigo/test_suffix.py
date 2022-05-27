# -- coding: utf-8 --
"""
@author: Alexandra, Andreia, Catarina, Daniela
"""

'''@package docstring
Implementação de testes a árvore de sufixos
'''


"""
Class: TestSuffixTree
"""

import unittest
from suffix_tree import SuffixTree

class TestSuffixTree(unittest.TestCase):
    
    def setUp(self):
        self.t1 = SuffixTree("TACTAG")
        self.t2 = SuffixTree("TAT")
        self.t3 = SuffixTree("TACTAGCTCAGCAAC")
    
    def test_find_pattern(self):
        self.assertEqual(self.t1.find_pattern("TA"), [0, 3])
        self.assertEqual(self.t2.find_pattern("GC"), False)
        self.assertEqual(self.t3.find_pattern("CT"), [2, 6])
        
    def test_get_leafs_below(self): 
        self.assertEqual(self.t1.get_leafs_below({'A': {'C': {'T': {'A': {'G': {'$': 1}}}}}}), [1])
        self.assertEqual(self.t2.get_leafs_below({'T': {'$': 2}}), [2])
        self.assertEqual(self.t3.get_leafs_below({'T': {'A': {'C': {'T': {'A': {'G': {'C': {'T': {'C': {'A': {'G': {'C': {'A': {'A': {'C': {'$': 0}}}}}}}}}}}}},
             'G': {'C': {'T': {'C': {'A': {'G': {'C': {'A': {'A': {'C': {'$': 3}}}}}}}}}}}}}), [0,3])

               
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit = False)