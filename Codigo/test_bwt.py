# -- coding: utf-8 --
"""
@author: Alexandra,Andreia,Catarina,Daniela
"""

'''@package docstring
Implementação de testes ao algoritmo para transformação
de Burrows-Wheeler
'''

"""
Class: BWT
"""

import unittest
from bwt import BWT

bw1 = BWT("ctttaaacc$")
bw2 = BWT("ACG$GTAAAAC")
bw3 = BWT("TAGACAGAGA$")
bw4 = BWT("ctttaaacc$", True)
bw5 = BWT("ACG$GTAAAAC", True)
bw6 = BWT("TAGACAGAGA$", True)

class BWT (unittest.TestCase):

	def test_bwt(self):
		self.assertEqual(bw1.bwt, 'ctaaca$ttc')
		self.assertEqual(bw2.bwt, 'GTAAACAAC$G')
		self.assertEqual(bw3.bwt, 'AGGGTCAAAA$')

	def test_last_to_first(self):
		self.assertEqual(bw1.last_to_first(), [4, 7, 1, 2, 5, 3, 0, 8, 9, 6])
		self.assertEqual(bw2.last_to_first(), [8, 10, 1, 2, 3, 6, 4, 5, 7, 0, 9])
		self.assertEqual(bw3.last_to_first(), [1, 7, 8, 9, 10, 6, 2, 3, 4, 5, 0])

	def test_bw_matching(self):
		self.assertEqual(bw1.bw_matching("AGA"), [])
		self.assertEqual(bw2.bw_matching("AGA"), [])
		self.assertEqual(bw3.bw_matching("AGA"), [3, 4, 5])

	def test_bw_matching_pos(self):
		self.assertEqual(bw4.bw_matching_pos("AGA"), [])
		self.assertEqual(bw5.bw_matching_pos("AGA"), [])
		self.assertEqual(bw6.bw_matching_pos("AGA"), [1, 5, 7])

if __name__ == '__main__':
	unittest.main()

