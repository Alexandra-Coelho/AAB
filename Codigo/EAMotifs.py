# -- coding: utf-8 --
"""
Created on
@author: Alexandra,Andreia,Catarina,Daniela
"""

'''
@package docstring
Implementação do algoritmo evolucionário aplicado
aos motifs
'''


"""
Class: EAMotifsInt
Class: EAMotifsReal
"""

from fileinput import filename

from numpy import vectorize
from EvolAlgorithm import EvolAlgorithm
from Popul import PopulInt, PopulReal
from motiffinding import MotifFinding
from mymotifs import MyMotifs


def createMatZeros(nl: int, nc: int):
	"""
	Função que cria uma matriz de zeros, de tamanho nl linhas por nc colunas.

	Parameters
	----------
	:param nl: Número de linhas
	:param nc: Número de colunas

	"""
	res = []
	for _ in range(0, nl):
		res.append([0]*nc)
	return res


def printMat(mat: list):
	"""
	Função que imprime a matriz criada na função anterior.

	Parameters
	----------
	:param mat: Matriz

	"""
	for i in range(0, len(mat)):
		for j in range(len(mat[i])):
			print(f"{mat[i][j]:.3f}", end=' ')
		print()


class EAMotifsInt(EvolAlgorithm):
	"""
	Classe EAMotifsInt estende a class EvolAlgorithm herdando todos os seus métodos.
	Implementa indivíduos com representações inteiras.
	"""

	def __init__(self, popsize: int, numits: int, noffspring: int, filename: filename):
		"""
		Chama o construtor da classe EvolAlgorithm para representar uma
		população linearmente com N valores inteiros em cada gene.

		Parameters
		----------
		:param popsize: Tamanho da população
		:param numits: Número de iterações a ser realizadas
		:param noffspring: Número de descendentes em cada iteração
		:param filename: Nome do ficheiro que guarda os motifs
		"""
		self.motifs = MotifFinding()
		self.motifs.readFile(filename, "dna")
		indsize = len(self.motifs)
		EvolAlgorithm.__init__(self, popsize, numits, noffspring, indsize)

	def initPopul(self, indsize: int):
		"""
		Função avalia cada indivíduo calculando o score do alinhamento definido pela posições iniciais.

		Parameters
		----------
		:param indsize: Tamanho dos indivíduos

		"""
		maxvalue = self.motifs.seqSize(0) - self.motifs.motifSize
		self.popul = PopulInt(self.popsize, indsize, maxvalue, [])

	def evaluate(self, indivs: int):
		"""
		Função que avalia os valores de aptidão dos individuos.
		Altera a forma como estes são avaliados na classe EvolAlgorithm

		Parameters
		----------
		:param indivs: Indivíduos a ser avaliados

		"""
		for i in range(len(indivs)):
			ind = indivs[i]
			sol = ind.getGenes()
			fit = self.motifs.score(sol)
			ind.setFitness(fit)


class EAMotifsReal (EvolAlgorithm):
	"""
	Classe EAMotifsReal estende a class EvolAlgorithm herdando todos os seus métodos.
	Implementa indivíduos com representações reais.
	"""

	def __init__(self, popsize: float, numits: float, noffspring: float, filename: filename):
		"""
		Chama o construtor da classe EvolAlgorithm para uma representação real
		da população onde se representa diretamente o perfil (a PWM).

		Parameters
		----------
		:param popsize: Tamanho da população
		:param numits: Número de iterações a ser realizadas
		:param noffspring: Número de descendentes em cada iteração
		:param filename: Nome do ficheiro que guarda os motifs

		"""
		self.motifs = MotifFinding()
		self.motifs.readFile(filename, "dna")
		indsize = len(self.motifs.alphabet) * self.motifs.motifSize
		EvolAlgorithm.__init__(self, popsize, numits, noffspring, indsize)

	def initPopul(self, indsize: float):
		"""
		Função procura população obtida na classe PopulReal.

		Parameters
		----------
		:param indsize: Tamanho dos individuos

		"""
		self.popul = PopulReal(self.popsize, indsize, lb=0.0, ub=1.0, indivs=[])

	def vec_to_pwm(self, sol: vectorize):
		"""
		Função calcula os valores de aptidão avaliando a frequência com que os símbolos aparecem nos individuos.

		Parameters
		----------
		:param v: Vetor de sequências

		"""
		n = len(self.motifs.alphabet)
		pwm = createMatZeros(n, self.motifs.motifSize)
		for j in range(0, self.indsize, n):
			coluna = sol[j:(j+n)]
			soma = sum(coluna)
			if soma == 0:
				return None
			col = j//n
			for k in range(n):
				pwm[k][col] = coluna[k]/soma
		return pwm

	def evaluate(self, indivs: float):
		"""
		Função avalia o valor de aptidão dos individuos.
		Altera a forma como estes são avaliados na classe EvolAlgorithm.

		Parameters
		----------
		:param indivs: Indivíduos a ser avaliados

		"""
		mtf = MyMotifs(self.motifs.seqs)
		for i in range(len(indivs)):
			ind = indivs[i]
			pwm = self.vec_to_pwm(ind.getGenes())
			if pwm:
				s = [0] * len(self.motifs.seqs)
				mtf.pwm = pwm
				for j in range(len(self.motifs.seqs)):
					seq = self.motifs.seqs[j]
					best_position = mtf.mostProbableSeq(seq)
					s[j] = best_position
				fit = self.motifs.scoreMult(s, pwm=pwm)
				ind.setFitness(fit)
			else:
				ind.setFitness(0)

	def printBestSolution(self):
		print("Best solution: ", self.bestsol.getGenes())
		print("Best fitness:", self.bestfit)

