# -- coding: utf-8 --
"""
Created on
@author: Alexandra,Andreia,Catarina,Daniela
"""

'''
@package docstring
Implementação da classe que implementa populações
'''


"""
Class: Popul
Class: PopulInt
Class: PopulReal
"""

from Indiv import Indiv, IndivInt, IndivReal
from random import random


class Popul:
	"""
	Classe Popul implementa populações de individuos bem como o seu tamanho com representações binárias.
	"""

	def __init__(self, popsize: int, indsize: int, indivs: list =[]):
		"""
		Construtor guarda o número de indivíduos de uma população, o tamanho dos indivíduos
		e os indivíduos.
		Caso não existam indivíduos estes são criados de forma aleatória.

		Parameters
    	----------
		:param posize: Número de individuos da população
		:param indsize: Tamanho dos individuos
		:param indivs: Individuos

		"""
		self.popsize = popsize
		self.indsize = indsize
		if indivs:
			self.indivs = indivs
		else:
			self.initRandomPop()

	def getIndiv(self, index: int):
		"""
		Função seleciona um individuo conforme a sua posição.

		Parameters
    	----------
		:param index: Posição do indivíduo

		"""
		return self.indivs[index]

	def initRandomPop(self):
		"""
		Função gera indivíduos de forma aleatória.

		"""
		self.indivs = []
		for _ in range(self.popsize):
			indiv_i = Indiv(self.indsize, [])
			self.indivs.append(indiv_i)

	def getFitnesses(self, indivs=None):
		"""
		Função seleciona e guarda os valores de aptidão de todos os indivíduos.

		Parameters
    	----------
		:param indivs: Número de indivíduos

		"""
		fitnesses = []
		if not indivs:
			indivs = self.indivs
		for ind in indivs:
			fitnesses.append(ind.getFitness())
		return fitnesses

	def bestFitness(self):
		"""
		Função que devolve o valor de aptidão da melhor solução.

		"""
		return max(self.getFitnesses())

	def bestSolution(self):
		"""
		Função devolve a melhor solução entre os indivíduos.

		"""
		self.indivs.sort(reverse=True)
		return self.indivs[0], self.indivs[0].fitness
		fitnesses = self.getFitnesses()
		bestf = fitnesses[0]
		bestsol = 0
		for i in range(1, len(fitnesses)):
			if fitnesses[i] > bestf:
				bestf = fitnesses[i]
				bestsol = i
		return self.getIndiv(bestsol), bestf

	def selection(self, n, indivs=None):
		"""
		Função que faz a seleção de indivíduos para a reprodução.

		Parameters
    	----------
		:param n: Número de novos descendentes
		:param indivs: Individuos

		"""
		res = []
		fitnesses = list(self.linscaling(self.getFitnesses(indivs)))
		for _ in range(n):
			sel = self.roulette(fitnesses)
			fitnesses[sel] = 0.0
			res.append(sel)
		return res

	def roulette(self, f):
		"""
		Função implementa um método estocástico da roleta para a seleção de indivíduos.

		Parameters
    	----------
		:param f: Lista de indivíduos

		"""
		tot = sum(f)
		val = random()
		acum = 0.0
		ind = 0
		while acum < val:
			acum += (f[ind] / tot)
			ind += 1
		return ind-1

	def linscaling(self, fitnesses):
		"""
		Função faz a normalização dos valores de aptidão entre 0 e 1.

		Parameters
    	----------
		:param fitnesses: Lista com os valores de aptidão

		"""
		mx = max(fitnesses)
		mn = min(fitnesses)
		res = []
		for f in fitnesses:
			val = (f-mn)/(mx-mn)
			res.append(val)
		return res

	def recombination(self, parents, noffspring):
		"""
		Função de recombinação, usa cruzamentos para criar novas soluções e aplica mutações a cada nova solução.

		Parameters
    	----------
		:param parents: Progenitores
		:param noffspring: Novas solucoes a gerar a partir dos progenitores

		"""
		offspring = []
		new_inds = 0
		while new_inds < noffspring:
			parent1 = self.indivs[parents[new_inds]]
			parent2 = self.indivs[parents[new_inds+1]]
			offsp1, offsp2 = parent1.crossover(parent2)
			offsp1.mutation()
			offsp2.mutation()
			offspring.append(offsp1)
			offspring.append(offsp2)
			new_inds += 2
		return offspring

	def reinsertion(self, offspring):
		"""
		Função implementa um mecanismo de reinserção, ou seja, seleciona os indivíduos que vão constituir a nova população
		ou passa à iteração seguinte.

		Parameters
    	----------
		:param noffspring: Número de descendentes

		"""
		tokeep = self.selection(self.popsize-len(offspring))
		ind_offsp = 0
		for i in range(self.popsize):
			if i not in tokeep:
				self.indivs[i] = offspring[ind_offsp]
				ind_offsp += 1


class PopulInt(Popul):
	"""
	Classe PopulReal estende a class Popul herdando todos os seus métodos.
	Implementa indivíduos com representações inteiras.
	"""
	def __init__(self, popsize: int, indsize: int, maxValue: int, indivs: list =[]):
		"""
		Chama o construtor da classe Popul para representar uma população linearmente
		com N valores inteiros em cada gene.
		Guarda o máximo de elementos que podem existir numa população.

		Parameters
		----------
		:param popsize: Tamanho da população.
		:param indsize: Tamanho dos individuos
		:param maxvalue: Máximo de elementos da população
		:param indivs: Lista de indivíduos

		"""
		self.maxValue = maxValue
		Popul.__init__(self, popsize, indsize, indivs)

	def initRandomPop(self):
		"""
		Função gera uma população de forma aleatória.
		Implementa indivíduos com representações inteiras.

		"""
		self.indivs = []
		for _ in range(self.popsize):
			indiv_i = IndivInt(self.indsize, [], 0, self.maxValue)
			self.indivs.append(indiv_i)


class PopulReal(Popul):
	"""
	Classe PopulReal estende a class Popul herdando todos os seus métodos.
	Implementa indivíduos com representações reais.
	"""

	def __init__(self, popsize: int, indsize: int, lb: int =0.0, ub: int =1.0, indivs: list =[]):
		"""
		Chama o construtor da classe EvolAlgorithm para uma representação real
		da população.
		Guarda os limites superiores e inferiores.

		Parameters
		----------
		:param popsize: Tamanho da população
		:param indsize: Tamanho dos individuos
		:param lb: Lower bound, limite inferior para o valor do gene
		:param ub: Upper bound, limite superior para o valor do gene
		:param indivs: Lista de indivíduos

		"""
		self.ub = ub
		self.lb = lb
		Popul.__init__(self, popsize, indsize, indivs)

	def initRandomPop(self):
		"""
		Função gera uma população de forma aleatória.
		Implementa indivíduos com representações reais.

		"""
		self.indivs = []
		for _ in range(self.popsize):
			indiv_i = IndivReal(self.indsize, [], self.lb, self.ub)
			self.indivs.append(indiv_i)
