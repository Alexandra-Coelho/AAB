# -- coding: utf-8 --
"""
@author: Alexandra,Andreia,Catarina,Daniela
"""

'''@package docstring
Implementação de testes para as funções da Class MotifFinding
'''


"""
Class: TestMotifs
"""

import unittest
from myseq import MySeq
from mymotifs import MyMotifs
from motiffinding import MotifFinding
from os import chdir
chdir(r'c:\Users\Asus\Desktop\Bioinformática\2º Semestre\Algoritmos Avançados de Bioinformática\aula5')

class TestMotifs(unittest.TestCase):   

    def setUp(self): 
        self.t1 = MotifFinding(3, [MySeq("ATAGAGCTGA", "dna"), MySeq("ACGTAGATGA", "dna"), MySeq("AAGATAGGGG", "dna")])
        self.t2 = MotifFinding()
        self.t2.readFile('exemploMotifs.txt', 'dna')
        self.t4 = MotifFinding(6, [MySeq("ATAGAGCTGA", "dna"), MySeq("ACGTAGATGA", "dna"), MySeq("AAGATAGGGG", "dna")])
        self.t5 = MotifFinding(4, [MySeq("ACCTGACGTCGAACTG", "dna"), MySeq("AATGCGTCGTGAAAC", "dna"), MySeq("TTCGAACGACTTGAT", "dna")])
    def test_createMotifFromIndexes(self):
        self.assertEqual(self.t1.createMotifFromIndexes(self.t1.exhaustiveSearch()).consensus(),'TAG')
        self.assertEqual(self.t1.createMotifFromIndexes(self.t1.branchAndBound()).consensus(),'TAG')
        self.assertEqual(self.t2.createMotifFromIndexes(self.t2.branchAndBound()).consensus(),'CTGATGTA')
        self.assertEqual(self.t4.createMotifFromIndexes(self.t4.exhaustiveSearch()).consensus(),'ATAGAG')
        self.assertEqual(self.t5.createMotifFromIndexes(self.t5.exhaustiveSearch()).consensus(),'CGTC')
    def test_scoreMult(self):
        self.assertEqual(self.t2.scoreMult([25, 20, 2, 55, 59]),0.08847360000000001)
        self.assertEqual(self.t2.scoreMult([3, 5, 9, 2, 5]),0.0009830400000000003)
    def test_score(self):
        self.assertEqual(self.t2.score([25, 20, 2, 55, 59]),30)
        self.assertEqual(self.t2.score([3, 5, 9, 2, 5]),17)
        self.assertEqual(self.t1.score(self.t1.exhaustiveSearch()),9)
        self.assertEqual(self.t1.score(self.t1.branchAndBound()),9)
        self.assertEqual(self.t1.score(self.t1.heuristicConsensus()),9)
        self.assertEqual(self.t1.score(self.t1.gibbs()),9)
        self.assertEqual(self.t2.score(self.t2.branchAndBound()),34)
        self.assertEqual(self.t2.score(self.t2.heuristicConsensus()),30)
        self.assertEqual(self.t4.score(self.t4.exhaustiveSearch()),15)
        self.assertEqual(self.t4.score(self.t4.branchAndBound()),15)
        self.assertEqual(self.t4.score(self.t4.heuristicConsensus()),15)
        self.assertEqual(self.t5.score(self.t5.exhaustiveSearch()),11)
        self.assertEqual(self.t5.score(self.t5.branchAndBound()),11)
        self.assertEqual(self.t5.score(self.t5.heuristicConsensus()),11)
    def test_branchAndBound(self):
        self.assertEqual(self.t1.branchAndBound(),[1, 3, 4])
        self.assertEqual(self.t2.branchAndBound(),[1, 4, 45, 5, 0])
        self.assertEqual(self.t4.branchAndBound(),[0, 2, 3])
        self.assertEqual(self.t5.branchAndBound(),[6, 4, 6])
    def test_exhaustiveSearch(self):
        self.assertEqual(self.t1.exhaustiveSearch(),[1, 3, 4])
        self.assertEqual(self.t4.exhaustiveSearch(),[0, 2, 3])
        self.assertEqual(self.t5.exhaustiveSearch(),[6, 4, 6])
    def test_heuristicConsensus(self):
        self.assertEqual(self.t1.heuristicConsensus(),[1, 3, 4])
        self.assertEqual(self.t2.heuristicConsensus(),[0, 38, 14, 33, 1])
        self.assertEqual(self.t4.heuristicConsensus(),[4, 4, 1])
        self.assertEqual(self.t5.heuristicConsensus(),[6, 4, 6])

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit = False)