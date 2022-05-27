# -- coding: utf-8 --
"""
Created on
@author: Alexandra,Andreia,Catarina,Daniela
"""

'''
@package docstring
Implementação da classe que implementa indivíduos
'''


"""
Class: Indiv
"""

from random import randint, random, shuffle
from abc import ABC, abstractmethod


class Indiv():
	"""
	Classe Indiv implementa indivíduos com representações binárias.
	"""

	def __init__(self, size: int, genes: str =[], lb: int =0, ub: int =1):
		"""
		Construtor guarda o limite superior, o limite inferior e os genes.
		Caso não haja genes para guardar estes são criados de forma aleatória
		tendo em conta o tamanho da população.

		Parameters
		----------
		:param size: Tamanho da população
		:param genes: Genome, conjunto de genes, lista de genes
		:param lb: Lower bound, limite inferior para o valor do gene
		:param ub: Upper bound, limite superior para o valor do gene

		"""
		self.lb = lb
		self.ub = ub
		self.genes = genes
		if not self.genes:
			self.initRandom(size)

	def __eq__(self, solution: list):
		"""
		Função compara se valores de aptidão e soluções são iguais.

		Parameters
		----------
		:param solution: lista de genes

		"""
		if isinstance(solution, self.__class__):
			return self.genes.sort() == solution.genes.sort()
		return False

	def __gt__(self, solution: list):
		"""
		Função compara se valores de aptidão são superiores às soluções.

		Parameters
		----------
		:param solution: lista de genes

		"""
		if isinstance(solution, self.__class__):
			return self.fitness > solution.fitness
		return False

	def __lt__(self, solution: list):
		"""
		Função compara se valores de aptidão são inferiores às soluções.

		Parameters
		----------
		:param solution: lista de genes

		"""
		if isinstance(solution, self.__class__):
			return self.fitness < solution.fitness
		return False

	def __ge__(self, solution: list):
		"""
		Função compara se valores de aptidão Superiores ou iguais às soluções.

		Parameters
		----------
		:param solution: lista de genes

		"""
		if isinstance(solution, self.__class__):
			return self.fitness >= solution.fitness
		return False

	def __le__(self, solution: list):
		"""
		Função compara se valores de aptidão são inferiores ou iguais às soluções.

		Parameters
		----------
		:param solution: lista de genes

		"""
		if isinstance(solution, self.__class__):
			return self.fitness <= solution.fitness
		return False

	def setFitness(self, fit :int):
		"""
		Função define os valores de aptidão.

		Parameters
		----------
		:param fit: valor de aptidão

		"""
		self.fitness = fit

	def getFitness(self):
		"""
		Função vai buscar os valores de aptidão.

		"""
		return self.fitness

	def getGenes(self):
		"""
		Função vai buscar os genes do indivíduo.

		"""
		return self.genes

	def initRandom(self, size: int):
		"""
		Função permite gerar indivíduos de forma aleatória.

		Parameters
		----------
		:param size: Tamanho da população
		"""
		self.genes = []
		for _ in range(size):
			self.genes.append(randint(0, 1))

	def mutation(self):
		"""
		Função que permite a inserção de mutações em vetores binários, de forma aleatória.

		"""
		s = len(self.genes)
		pos = randint(0, s-1)
		if self.genes[pos] == 0:
			self.genes[pos] = 1
		else:
			self.genes[pos] = 0

	def crossover(self, indiv2: int):
		"""
		Função retorna o resultado obtido do cruzamento entre indivíduos num ponto.

		"""
		return self.one_pt_crossover(indiv2)

	def one_pt_crossover(self, indiv2: int):
		"""
		Função que implementa cruzamento entre individuos num ponto, de onde resultam descendentes misturados.

		Parameters
		----------
		:param indiv2: Individuo necessário ao cruzamento

		"""
		offsp1 = []
		offsp2 = []
		s = len(self.genes)
		pos = randint(0, s-1)
		for i in range(pos):
			offsp1.append(self.genes[i])
			offsp2.append(indiv2.genes[i])
		for i in range(pos, s):
			offsp2.append(self.genes[i])
			offsp1.append(indiv2.genes[i])
		return self.__class__(s, offsp1, self.lb, self.ub), self.__class__(s, offsp2, self.lb, self.ub)


class IndivInt (Indiv):
	"""
	Classe IndivInt estende a class Indiv herdando todos os seus métodos.
	Implementa indivíduos com representações inteiras.

	"""
	def initRandom(self, size: int):
		"""
		Construtor gera indivìduos de forma aleatória.

		Parameters
		----------
		:param size: Tamanho da população

		"""
		self.genes = []
		for _ in range(size):
			self.genes.append(randint(0, self.ub))

	def mutation(self):
		"""
		Função insere de mutações numa posição aleatória.

		"""
		s = len(self.genes)
		pos = randint(0, s-1)
		self.genes[pos] = randint(0, self.ub)


class IndivReal (Indiv):
	"""
	Classe IndivReal estende a class Indiv herdando todos os seus métodos.
	Implementa individuos com representações reais.

	"""
	def initRandom(self, size: int):
		"""
		Construtor gera indivìduos de forma aleatória.

		Parameters
		----------
		:param size: Tamanho da população

		"""
		self.genes = []
		for _ in range(size):
			delta = self.ub-self.lb
			self.genes.append(random()*delta+self.lb)

	def mutation(self):
		"""
		Função insere de mutações numa posição aleatória.

		"""
		s = len(self.genes)
		pos = randint(0, s-1)
		delta = self.ub-self.lb
		self.genes[pos] = random()*delta+self.lb
