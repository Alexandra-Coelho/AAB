# -- coding: utf-8 --
"""
@author: Alexandra,Andreia,Catarina,Daniela
"""

'''@package docstring
Implementação da procura de MotifFinding
'''


"""
Class: MotifFinding
"""
from myseq import MySeq
from mymotifs import MyMotifs
from random import randint
from random import random
from os import chdir
chdir(r'c:\Users\Asus\Desktop\Bioinformática\2º Semestre\Algoritmos Avançados de Bioinformática\aula5')

class MotifFinding:
    """
    Classe MotifFinding implementa algoritmos de procura de motifs conservados, dados conjuntos de sequências, 
    i.e. algoritmos de otimização para descoberta/inferência de motifs
    
    """
    def __init__(self, size: int = 8, seqs: str = None):
        """
        Construtor que recebe como parametro de entrada, o tamanho do motif e um conjunto de sequências
        
        Parameters
        ----------
        :param size: tamanho do motif

        :param seqs: conjunto de sequências
        
        """
        self.motifSize = size 
        if (seqs != None):  
            self.seqs = seqs
            self.alphabet = seqs[0].alfabeto()
        else:
            self.seqs = []  

    def __len__(self) -> int: 
        """
        Função devolve nº de elementos na lista de seqs

        """
        return len(self.seqs)  

    def __getitem__(self, n: int) -> str:
        """
        Função vai buscar à lista de seqs a sequencia que corresponde a n

        Parameters
        ----------
        :param n: sequencia n 

        """
        return self.seqs[n

    def seqSize(self, i: int) -> int:
        """
        Função devolve o tamanho da seq que vai buscar à lista de seqs a sequencia que corresponde a i

        Parameters
        ----------
        :param i: sequencia i

        """
        return len(self.seqs[i])  

    def readFile(self, fic: str, t: str) -> str:  
        """
        Função lê um ficheiro e vai adiciona-lo à lista de self.seqs

        Parameters
        ----------
        :param fic: ficheiro a ser lido

        :param t: tipo de sequência

        """
        for s in open(fic, "r"):
            self.seqs.append(MySeq(s.strip().upper(), t))
        self.alphabet = self.seqs[0].alfabeto()

    def createMotifFromIndexes(self, indexes: list):  
        """
        Função cria motifs a partir de uma lista de indices onde começam os motifs nas várias sequências

        Parameters
        ----------
        :param indexes: lista de números que correspondem ao local onde se inicia o motif em cada sequência

        """
        pseqs = []
        for i, ind in enumerate(indexes):
            pseqs.append(MySeq(self.seqs[i][ind:(ind + self.motifSize)], self.seqs[i].tipo))  
        return MyMotifs(pseqs) 


    def score(self, s: list) -> float:
        """
        Função calcula o score do consenso

        Parameters
        ----------
        :param s: lista de números que correspondem ao local onde se inicia o motif em cada sequência

        """
        score = 0
        motif = self.createMotifFromIndexes(s) 
        motif.doCounts()  
        mat = motif.counts  
        for j in range(len(mat[0])):  
            maxcol = mat[0][j]  
            for i in range(1,len(mat)):  
                if mat[i][j] > maxcol: 
                    maxcol = mat[i][j]
            score += maxcol  
        return score

    def scoreMult(self, s: list) -> float:  
        """
        Função calcula o score de cada motif com probabilidades e o score vem em probabilidade sendo calculado por multiplicação

        Parameters
        ----------
        :param s: lista de números que correspondem ao local onde se inicia o motif em cada sequência

        """
        score = 1.0
        motif = self.createMotifFromIndexes(s)
        motif.createPWM()
        mat = motif.pwm
        for j in range(len(mat[0])):
            maxcol = mat[0][j]
            for i in range(1, len(mat)):
                if mat[i][j] > maxcol:
                    maxcol = mat[i][j]
            score *= maxcol 
        return score


    def nextSol(self, s: list) -> list:
        """
        Função permite iterar por todas os n-L+1 (comprimento da sequência - comprimento do motif + 1) valores possíveis para iniciar o motif

        Parameters
        ----------
        :param s: lista de 0 com o numero de seqs presentes na lista self.seqs

        """
        nextS = [0] * len(s)  
        pos = len(s) - 1  
        while pos >= 0 and s[pos] == self.seqSize(pos) - self.motifSize: 
            pos -= 1 
        if (pos < 0): 
            nextS = None  
        else:
            for i in range(pos):  
                nextS[i] = s[i]  
            nextS[pos] = s[pos] + 1 
            for i in range(pos + 1, len(s)):  
                nextS[i] = 0
        return nextS

    def exhaustiveSearch(self) -> list:
        """
        Função devolve uma lista das posições inicias dos motifs da lista de sequências que maximize o score

        """
        melhorScore = -1
        res = []
        s = [0] * len(self.seqs)  
        while (s != None): 
            sc = self.score(s)  
            if (sc > melhorScore):  
                melhorScore = sc
                res = s
            s = self.nextSol(s)  
        return res  

    def nextVertex(self, s: list) -> list:
        """
        Função permite passar ao próximo vertice percorrendo todas as folhas entre os dois

        Parameters
        ----------
        :param s: lista com a posição das sequências está a começar a formação dos motifs

        """
        res = []
        if len(s) < len(self.seqs): 
            for i in range(len(s)):
                res.append(s[i])
            res.append(0)
        else:  
            pos = len(s) - 1
            while pos >= 0 and s[pos] == self.seqSize(pos) - self.motifSize:  
                pos -= 1
            if pos < 0: res = None  
            else:
                for i in range(pos): res.append(s[i])  
                res.append(s[pos] + 1)
        return res

    def bypass(self, s: list) -> list:  
        """
        Função permite saltar à frente dos ramos de um dado nó, quando as folhas de um prefixo não contêm a melhor solução, 
        saltando assim para outro prefixo no mesmo nível

        Parameters
        ----------
        :param s: lista com a posição das sequências está a começar a formação dos motifs

        """
        res = []
        pos = len(s) - 1
        while pos >= 0 and s[pos] == self.seqSize(pos) - self.motifSize:
             pos -= 1
        if pos < 0: res = None
        else:
            for i in range(pos):
                res.append(s[i])
            res.append(s[pos] + 1)
        return res

    def branchAndBound(self) -> list: 
        """
        Função permite fazer a procura de motifs usando árvores de procura (Branch & Bound)

        """
        melhorScore = -1
        melhorMotif = None
        size = len(self.seqs) 
        s = [0] * size  
        while s != None:  
            if len(s) < size:  
                optimScore = self.score(s) + (size - len(s)) * self.motifSize
                if optimScore < melhorScore:
                    s = self.bypass(s) 
                else: 
                    s = self.nextVertex(s)
            else: 
                sc = self.score(s) 
                if sc > melhorScore:  
                    melhorScore = sc
                    melhorMotif = s
                s = self.nextVertex(s)  
        return melhorMotif

    def heuristicConsensus(self) -> list:
        """
        Função permite fazer a procura de motifs partindo das 2 primeiras sequências

        """
        mf = MotifFinding(self.motifSize, self.seqs[:2])  
        s = mf.exhaustiveSearch() 
        for a in range(2, len(self.seqs)):  
            s.append(0) 
            melhorScore = -1
            melhorPosition = 0
            for b in range(self.seqSize(a) - self.motifSize + 1): 
                s[a] = b 
                scoreatual = self.score(s) 
                if scoreatual > melhorScore:
                    melhorScore = scoreatual
                    melhorPosition = b 
                s[a] = melhorPosition 
        return s

    def heuristicStochastic(self) -> list:
        """
        Função obtem motifs usando algoritmos heurísticos estocásticos, que usa segmentos mais prováveis para ajustar as posições iniciais até 
        atingir o melhor perfil, que será o motif

        """
        from random import randint 
        s = [0] * len(self.seqs)  
        for i in range(len(self.seqs)): 
            s[i] = randint(0, self.seqSize(i) - self.motifSize)  
        melhorscore = self.score(s) 
        improve = True
        while improve:
            motif = self.createMotifFromIndexes(s)  
            motif.createPWM()
            for i in range(len(self.seqs)):  
                s[i] = motif.mostProbableSeq(self.seqs[i]) 
            scr = self.score(s) 
            if scr > melhorscore:  
                melhorscore = scr
            else:
                improve = False 
        return s

    def gibbs(self, iterations : int = 1000) -> list:
        """
        Função utiliza o método de Gibbs Sampling para melhorar o algoritmo utilizado anteriormente, utilizando para isso um processo iterativo que vai substituindo um segmento em cada 
        iteração

        """
        s = [] 
        for i in range(len(self.seqs)): 
            s.append(randint(0, len(self.seqs[i]) - self.motifSize - 1)) 
        melhorscore = self.score(s)  
        bests = list(s) 
        for it in range(iterations):
            seq_idx = randint(0, len(self.seqs) - 1)
            seq = self.seqs[seq_idx]  
            s.pop(seq_idx) 
            removed = self.seqs.pop(seq_idx)  
            motif = self.createMotifFromIndexes(s)  
            motif.createPWM()
            self.seqs.insert(seq_idx, removed)  
            r = motif.probAllPositions(seq)  
            pos = self.roulette(r) 
            s.insert(seq_idx, pos)  
            score = self.score(s)  
            if score > melhorscore: 
                melhorscore = score
                bests = list(s)
        return bests  

    def roulette(self, f) -> int:
        """
        Função que cria uma roleta aleatória para escolher de forma estocástica a posição inicial do motif a ser usada no método de Gibbs

        Parameters
        ----------
        :param f: lista da probabilidade de todas as subsequências possiveis

        """
        tot = 0.0
        for x in f: tot += (0.01 + x)
        val = random() * tot
        acum = 0.0
        ind = 0
        while acum < val:
            acum += (f[ind] + 0.01)
            ind += 1
        return ind - 1

