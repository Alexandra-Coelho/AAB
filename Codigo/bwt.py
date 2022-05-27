# -- coding: utf-8 --
"""
@author: Alexandra,Andreia,Catarina,Daniela
"""

'''@package docstring
Implementação do algoritmo para transformação
de Burrows-Wheeler
'''

"""
Class: BWT
"""

class BWT:
	"""
	Classe BWT implementa um conjunto de funções que pemitem, a partir de uma sequência inicial, provocar a sua transformação
	de Burrows-Wheeler.
	"""

	def __init__(self, seq="", buildsufarray: bool =False):
		"""
		Realiza a transformação de Burrows-Wheeler usando a função build_bwt que utiliza os parâmetros de construtor.

		Parameters
		----------
		:param seq: Sequência introduida
		:param buildsufarray: Parâmetro que define se é criado um array de sufixos ou não

		"""
		self.bwt = self.build_bwt(seq, buildsufarray)

	def set_bwt(self, bw):
		"""
		Função define matriz que é usada para a transformação de Burrows-Wheeler.

		Parameters
		----------
		:param bw: Sequência introduzida

		"""
		self.bwt = bw

	def build_bwt(self, text, buildsufarray=False):
		"""
		Função permite construir uma matriz que é usada para a transformação de Burrows-Wheeler.

		Parameters
		----------
		:param text: Sequência/texto/string para a criação da tabela/matriz.
		:param buildsufarray: Parâmetro que define se é criado um array de sufixos ou não

		"""
		ls = []
		for i in range(len(text)):
			ls.append(text[i:] + text[:i])
		ls.sort()
		#print(ls)
		res = ""
		for i in range(len(text)):
			res += ls[i][len(text) - 1]
		if buildsufarray:
			self.sa = []
			for i in range(len(ls)):
				stpos = ls[i].index("$")
				self.sa.append(len(text) - stpos - 1)
		return res

	def inverse_bwt(self):
		"""
		Função permite construir uma matriz que é usada para a transformação de Burrows-Wheeler.

		Parameters
		----------
		:param text: Sequência/texto/string para a criação da tabela/matriz.
		:param buildsufarray: Parâmetro que define se é criado um array de sufixos ou não

		"""
		firstcol = self.get_first_col()
		res = ""
		c = "$"
		occ = 1
		for i in range(len(self.bwt)):
			pos = find_ith_occ(self.bwt, c, occ)
			c = firstcol[pos]
			occ = 1
			k = pos - 1
			while firstcol[k] == c and k >= 0:
				occ += 1
				k -= 1
			res += c
		return res

	def get_first_col(self):
		"""
		Função que implementa a recuperação da primeira coluna.

		"""
		firstcol = []
		for c in self.bwt:
			firstcol.append(c)
		firstcol.sort()
		return firstcol

	def last_to_first(self):
		"""
		Função que cria uma tabela com as conversões da última coluna para a primeira.

		"""
		res = []
		firstcol = self.get_first_col()
		for i in range(len(firstcol)):
			c = self.bwt[i]
			ocs = self.bwt[:i].count(c) + 1
			res.append(find_ith_occ(firstcol, c, ocs))
		return res

	def bw_matching(self, patt):
		"""
		Função que permite implementar a procura de padrões através da transformação de Burrows-Wheeler.

		Parameters
		----------
		:param patt: Padrão a encontrar.

		"""
		lf = self.last_to_first()
		res = []
		top = 0
		bottom = len(self.bwt) - 1
		flag = True
		while flag and top <= bottom:
			if patt != "":
				symbol = patt[-1]
				patt = patt[:-1]
				lmat = self.bwt[top:(bottom + 1)]
				if symbol in lmat:
					topIndex = lmat.index(symbol) + top
					bottomIndex = bottom - lmat[::-1].index(symbol)
					top = lf[topIndex]
					bottom = lf[bottomIndex]
				else:
					flag = False
			else:
				for i in range(top, bottom + 1): res.append(i)
				flag = False
		return res

	def bw_matching_pos(self, patt):
		"""
		Função que devolve os índices onde há um match da sequência padrão.

		Parameters
		----------
		:param patt: Padrão a encontrar

		"""
		res = []
		matches = self.bw_matching(patt)
		for m in matches:
			res.append(self.sa[m])
		res.sort()
		return res


# auxiliary

def find_ith_occ(l, elem, index):
	"""
	Função vai buscar a posição da i-ésima ocorrência de um símbolo numa lista (l).

	Parameters
	----------
	:param l: lista de símbolos
	:param elem: símbolo a encontrar
	:param index: índice do símbolo na btw

	"""
	j, k = 0, 0
	while k < index and j < len(l):
		if l[j] == elem:
			k = k + 1
			if k == index: return j
		j += 1
	return -1
