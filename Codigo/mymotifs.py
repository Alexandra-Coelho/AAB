# -- coding: utf-8 --
"""
@author: Alexandra,Andreia,Catarina,Daniela
"""

'''@package docstring
Implementação da procura de Motifs biológicos
'''


"""
Class: MyMotifs
"""

def createMatZeros(nl: int, nc: int):  
    """
    Função cria uma matriz de 0's com nl linhas e nc colunas
        
    Parameters
    ----------
    :param nl: número de linhas
        
    :param nc: número de colunas
    """
    res = []
    for i in range(0, nl):
        res.append([0] * nc)
    return res


def printMat(mat):  
    """
    Função permite imprimir a matriz 
        
    Parameters
    ----------
    :param mat: matriz
        
    """
    for i in range(0, len(mat)): print(mat[i])


class MyMotifs:
    """
    Classe MyMotifs implementa : implementa motifs biológicos, PWMs
    e processos de procura de motifs conhecidos em sequências
    
    """
    def __init__(self, seqs: str):  
        """
        Construtor que recebe como parametro de entrada um conjunto de sequências
        
        Parameters
        ----------
        :param seqs: conjunto de sequências
        
        """
        self.size = len(seqs[0]) 
        self.seqs = seqs  
        self.alphabet = seqs[0].alfabeto()  
        self.doCounts()  
        self.createPWM()  

    def __len__(self) -> int:  
        """
        Função devolve nº de elementos na lista de seqs

        """
        return self.size

    def doCounts(self): 
        """
        Função cria uma matriz de contagem 
        
        """
        self.counts = createMatZeros(len(self.alphabet), self.size)  
        for s in self.seqs: 
            for i in range(self.size):
                lin = self.alphabet.index(s[i]) 
                self.counts[lin][i] += 1 
        
    def createPWM(self):  
        """
        Função cria um perfil probabilístico
        
        """
        if self.counts == None: self.doCounts()  
        self.pwm = createMatZeros(len(self.alphabet), self.size) 
        for i in range(len(self.alphabet)): 
            for j in range(self.size):
                self.pwm[i][j] = float(self.counts[i][j]) / len(self.seqs) 

    def consensus(self) -> str:  
        """
        Função permite obter a região consenso, que é dada, pela letra que mais se repete em cada coluna
        
        """
        res = "" 
        for j in range(self.size): 
            maxcol = self.counts[0][j] 
            maxcoli = 0
            for i in range(1, len(self.alphabet)):
                if self.counts[i][j] > maxcol:
                    maxcol = self.counts[i][j]
                    maxcoli = i
            res += self.alphabet[maxcoli]  
        return res

    def maskedConsensus(self) -> str:  
        """
        Função permite obter a região consenso, mas só com letras  que tem uma incidência maior do que 50%
        
        """
        res = ""
        for j in range(self.size):
            maxcol = self.counts[0][j]
            maxcoli = 0
            for i in range(1, len(self.alphabet)):
                if self.counts[i][j] > maxcol:
                    maxcol = self.counts[i][j]
                    maxcoli = i
            if maxcol > len(self.seqs) / 2: 
                res += self.alphabet[maxcoli]
            else: #senão leva append de -
                res += "-"
        return res

    def probabSeq(self, seq: str) -> float:  
        """
        Função permite obter a probabilidade de uma determinada sequência fazer parte do perfil do motif 

        Parameters
        ----------
        :param seq: sequência
                
        """
        res = 1.0
        for i in range(self.size): 
            lin = self.alphabet.index(seq[i]) 
            res *= self.pwm[lin][i]  
        return res

    def probAllPositions(self, seq: str) -> list:  
        """
        Função devolve uma lista com as probabilidades de acontecer em cada letra da seq
        
        Parameters
        ----------
        :param seq: sequência
                
        """      
        res = []
        for k in range(len(seq) - self.size + 1):
            res.append(self.probabSeq(seq)) 
        return res

    def mostProbableSeq(self, seq: str) -> float:  
        """
        Função devolve a posição inicial da subseq de uma seq de comprimento indefenido
        que encaixa melhor no perfil de motifs das seqs (P)
        Parameters
        ----------
        :param seq: sequência
                
        """ 
        maximo = -1.0
        maxind = -1
        for k in range(len(seq) - self.size):
            p = self.probabSeq(seq[k:k + self.size])
            if (p > maximo):
                maximo = p
                maxind = k
        return maxind
