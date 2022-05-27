# -*- coding: utf-8 -*-
"""
@author: Grupo 3
"""

'''@package docstring
Implementação do algoritmo heurístico Boyer Moore
'''


"""
Class: BoyerMoore
"""


class BoyerMoore:
    """
    Implementa o algoritmo de Boyer-Moore para a procura de padrões em
    sequências. Baseia-se num pré-processamento do padrão segundo duas regras:
    'Bad Caracter rule' e 'Good Suffix rule'.
    """
    def __init__(self, alphabet:str, pattern:str):
        ''' Guarda o alfabeto e padrão introduzidos e chama o método 'preprocess'
        que realiza as tabelas do pré-processamento BCR e GSR
        
        Parameters
        ----------
        :param alphabet: O alfabeto utilizado no padrão e texto a processar
        
        :param pattern: O padrão a ser procurado no texto
        '''
        self.alphabet = alphabet
        self.pattern = pattern
        self.preprocess()

    def preprocess(self):  
        ''' Realiza as tabelas do pré-processamento BCR e GSR
        '''
        self.process_bcr()
        self.process_gsr()

    def process_bcr(self):
        """Implementa a 'Bad Caracter Rule' e faz um dicionário de deslocações 
        para cada posição do padrão definido
        """
        self.occ = {} 
        for c in self.alphabet:  
            self.occ[c] = -1
        for i in range(len(self.pattern)):
            c = self.pattern[i]  
            self.occ[c] = i 
        return self.occ

    def process_gsr(self):
        """Implementa a 'Good Sufix Rule' e faz uma lista de deslocações
        para cada posição do padrão definido
        """
        self.f = [0] * (len(self.pattern) + 1) 
        self.s = [0] * (len(self.pattern) + 1)
        i = len(self.pattern)
        j = len(self.pattern) + 1  
        self.f[i] = j 
        while i > 0:
            while j <= len(self.pattern) and self.pattern[i - 1] != self.pattern[j - 1]:  
                if self.s[j] == 0:
                    self.s[j] = j - i
                j = self.f[j]
            i -= 1
            j -= 1
            self.f[i] = j
        j = self.f[0]
        for i in range(len(self.pattern)):  
            if self.s[i] == 0: self.s[i] = j
            if i == j: j = self.f[j]
        return self.s

    def search_pattern(self, text:str) -> list:
        '''Identifica as posições de match do padrão numa sequência e retorna uma
        lista de índices do texto onde foram encontradas correspondências 
        exatas do padrão
        
        Parameters
        ----------
        :param text: String onde se pretende procurar ocorrências do padrão
        '''
        res = []
        i = 0  
        while i <= (len(text) - len(self.pattern)):  
            j = len(self.pattern) - 1 
            while j >= 0 and self.pattern[j] == text[j + i]:  
                j -= 1
            if j < 0: 
                res.append(i)
                i = i + self.s[0] 
            else:
                c = text[i + j] 
                i += max(self.s[j + 1], j - self.occ[c])  
        return res