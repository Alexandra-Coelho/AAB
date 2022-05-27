# -- coding: utf-8 --
"""
Created on
@author: Alexandra,Andreia,Catarina,Daniela
"""

'''
@package docstring
Implementação do algoritmo evolucionário
'''


"""
Class: EvolAlgorithm
"""

from numpy import int8
from Popul import Popul


class EvolAlgorithm:
	"""
	Classe EvalAlgorithm implementa algoritmos evolucionários com representações binárias.

	"""

	def __init__(self, popsize: int, numits: int, noffspring: int, indsize: int):
		"""
		Construtor guarda o tamanho da população, o número de iterações realizadas,
		o número de descendentes e o tamanho dos indivíduos.

		Parameters
		----------
		:param popsize: Tamanho da população
		:param numits: Número de iterações a fazer
		:param noffspring: Número de descendentes em cada iteração/geração
		:param indsize: Tamanho dos indivíduos

		"""
		self.popsize = popsize
		self.numits = numits
		self.noffspring = noffspring
		self.indsize = indsize

	def initPopul(self, indsize: int):
		"""
		Função procura população obtida na classe Popul.

		Parameters
    	----------
		:param indsize: Tamanho dos indivíduos

		"""
		self.popul = Popul(self.popsize, indsize)

	def iteration(self):
		"""
		Função que implementa iterações, ou seja, cria gerações de indivíduos (offsprings)
		a partir dos indivíduos da população inicial.

		"""
		parents = self.popul.selection(self.noffspring)
		offspring = self.popul.recombination(parents, self.noffspring)
		self.evaluate(offspring)
		self.popul.reinsertion(offspring)

	def evaluate(self, indivs: int):
		"""
		Função avalia o valor de aptidão dos individuos.

		Parameters
    	----------
		:param indivs: Indivíduos a ser avaliados

		"""
		for i in range(len(indivs)):
			ind = indivs[i]
			fit = 0.0
			for x in ind.getGenes():
				if x == 1:
					fit += 1.0
			ind.setFitness(fit)
		return None

	def run(self):
		"""
		Função corre o algoritmo devolvendo a iteração e a melhor solução para esta.

		"""
		self.initPopul(self.indsize)
		self.evaluate(self.popul.indivs)
		self.bestsol = []
		self.bestfit = 0.0
		for i in range(self.numits+1):
			self.iteration()
			bs, bf = self.popul.bestSolution()
			if bf > self.bestfit:
				self.bestfit = bf
				self.bestsol = bs
			print("Iteration:", i, " ", "Best: ", self.popul.bestFitness())
		#self.bestsol, self.bestfit = self.popul.bestSolution()

	def printBestSolution(self):
		"""
		Função imprime a melhor solução possível bem como o melhor valor de aptidão.

		"""
		print("Best solution: ", self.bestsol.getGenes())
		print("Best fitness:", self.bestfit)

