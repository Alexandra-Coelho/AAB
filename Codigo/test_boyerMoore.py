# -*- coding: utf-8 -*-
"""
@author: Alexandra,Andreia,Catarina,Daniela
"""

'''@package docstring
Teste Boyer Moore
'''


"""
Class: Testes
"""

import unittest
from boyer_moore import BoyerMoore



class Testes(unittest.TestCase):
    def setUp(self):
        self.t1 = BoyerMoore("ACTG", "ACCA")
        self.t2 = BoyerMoore("ACTG","TCTA")
        self.t3 = BoyerMoore("ACTG","TCAA")
        self.t4 = BoyerMoore("ACTG","TCAG")
        self.t5 = BoyerMoore("ACTG","TCCFA")
    def test_process_bcr(self):
        self.assertEqual(self.t1.process_bcr(),{'A': 3, 'C': 2, 'T': -1, 'G': -1})
        self.assertEqual(self.t2.process_bcr(),{'A': 3, 'C': 1, 'T': 2, 'G': -1})
        self.assertEqual(self.t3.process_bcr(),{'A': 3, 'C': 1, 'T': 0, 'G': -1})
        self.assertEqual(self.t4.process_bcr(),{'A': 2, 'C': 1, 'T': 0, 'G': 3})
        self.assertEqual(self.t5.process_bcr(),{'A': 4, 'C': 2, 'T': 0, 'G': -1, 'F': 3})
    def test_process_gsr(self):
        self.assertEqual(self.t1.process_gsr(),[3, 3, 3, 3, 1])
        self.assertEqual(self.t2.process_gsr(),[4, 4, 4, 4, 1])
        self.assertEqual(self.t3.process_gsr(),[4, 4, 4, 1, 2])
        self.assertEqual(self.t4.process_gsr(),[4, 4, 4, 4, 1])
        self.assertEqual(self.t5.process_gsr(),[5, 5, 5, 5, 5, 1])
    def test_search_pattern(self):
        self.assertEqual(self.t1.search_pattern("ATAGAACCAATGAACCATGATGAACCATGGATACCCAACCACC"),[5, 13, 23, 37])
        self.assertEqual(self.t2.search_pattern("GCTACGATCTAGAATCTA"),[7, 14])
        self.assertEqual(self.t3.search_pattern("GCTAGCTACCGTATCAATC"),[13])
        self.assertEqual(self.t4.search_pattern("GCTCAGAGTCGGTCAGTAACTCTT"),[2, 12])
        self.assertEqual(self.t4.search_pattern("ATGTTACCCGTACGAAATGGA"),[])
 




if __name__ == '__main__':
    unittest.main()









