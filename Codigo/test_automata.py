# -*- coding: utf-8 -*-
"""
@author: Alexandra,Andreia,Catarina,Daniela
"""

'''@package docstring
Testes automatos finitos
'''


"""
Class: Testes
"""

import unittest
from automata import Automata, overlap



class Testes(unittest.TestCase):
    def setUp(self):
        self.t1 = Automata("AC", "ACA")
        self.t2 = Automata("ACGT", "GTT")
        self.t3 = Automata("ACGT", "TACT")
        self.t4 = Automata("ACTG","TC")
    def test_applySeq(self):
        self.assertEqual(self.t1.applySeq("CACAACAA"),[0, 0, 1, 2, 3, 1, 2, 3, 1])
        self.assertEqual(self.t2.applySeq("GAACTGATGTT"),[0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 2, 3])
        self.assertEqual(self.t3.applySeq("TAGGTTACTGGAATACTGT"),[0, 1, 2, 0, 0, 1, 1, 2, 3, 4, 0, 0, 0, 0, 1, 2, 3, 4, 0, 1])
        self.assertEqual(self.t4.applySeq("GATCACTCGTGTCT"),[0, 0, 0, 1, 2, 0, 0, 1, 2, 0, 1, 0, 1, 2, 1])
    def test_ocurrencesPattern(self):
        self.assertEqual(self.t1.occurencesPattern("CACAACAA"),[1,4])
        self.assertEqual(self.t2.occurencesPattern("GAACTGATGTT"),[8])
        self.assertEqual(self.t3.occurencesPattern("TAGGTTACTGGAATACTGT"),[5,13])
        self.assertEqual(self.t4.occurencesPattern("GATCACTCGTGTCT"),[2, 6, 11])
    def test_overlap(self):
        self.assertEqual(overlap("ATA","ATATAT"),3)
        self.assertEqual(overlap("ATT","ATATAT"),0)
        self.assertEqual(overlap("AGTC","AGTCTACGTAGTTTC"),4)
        self.assertEqual(overlap("AGATTTC","TCAGAGGTA"),2)
        self.assertEqual(overlap("GGTTTACG","GTATA"),1)


       


if __name__ == '__main__':
    unittest.main()



