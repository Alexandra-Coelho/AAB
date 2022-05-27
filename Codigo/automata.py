# -*- coding: utf-8 -*-
"""
@author: Alexandra,Andreia,Catarina,Daniela
"""

'''@package docstring
Implementação de autómatos finitos
'''


"""
Class: Automata
"""


class Automata:  
    """
    Implementa um Autómato finito para a procura de ocorrências do padrão
    usado para o construir
    """
    def __init__(self, alphabet:str, pattern:str):    
        """
        Guarda o alfabeto, o número de estados e chama o método 'buildTransitionTable' 
        onde é construída a tabela de transições

        Parameters
        ----------
        :param alphabet: O alfabeto utilizado no padrão e texto a processar
        
        :param pattern: O padrão a ser procurado no texto
        """
        self.numstates = len(pattern) + 1 
        self.alphabet = alphabet
        self.transitionTable = {}
        self.buildTransitionTable(pattern)

    def buildTransitionTable(self, pattern:str):
        '''Constrói a tabela de transições a partir do padrão 
        
        Parameters
        ----------
        :param pattern: O padrão a ser procurado no texto
        '''
        for q in range(self.numstates): 
            for a in self.alphabet: 
                prefixo = pattern[:q] + a  
                p = overlap(prefixo, pattern)
                self.transitionTable[(q, a)] = p  

    def printAutomata(self):  
        '''Imprime a informação retirada da classe: Número de estados,
        alfabeto e tabela de transição
        '''
        print("States: ", self.numstates)
        print("Alphabet: ", self.alphabet)
        print("Transition table:")
        for k in self.transitionTable.keys():
            print(k[0], ",", k[1], " -> ", self.transitionTable[k])

    def nextState(self, current:int, symbol:str) -> int:
        '''Identifica o estado para o qual deve avançar
        
        Parameters
        ----------
        :param current: Estado atual
        :param symbol: Caractér a analisar da sequência
        '''
        return self.transitionTable[(current, symbol)]  

    def applySeq(self, seq:str) -> list:
        '''Aplica o autómato finito a uma sequência dando como resultado a lista de estados
        encontrados
        
        Parameters
        ----------
        :param seq: String onde se pretende procurar ocorrências do padrão
        '''
        q = 0  
        res = [q]
        for c in seq:
            q = self.nextState(q, c) 
            res.append(q)  
        return res

    def occurencesPattern(self, text:str) -> list:
        """
        Identifica as posições de match do padrão representado pelo Autómato finito
        numa string e retorna uma lista de índices do texto onde foram encontradas 
        correspondências exatas do padrão
        
        Parameters
        ----------
        :param text: String onde se pretende procurar ocorrências do padrão
        """
        q = 0
        res = []
        for i in range(len(text)):
            q = self.nextState(q, text[i]) 
            if q == self.numstates - 1: res.append(i - self.numstates + 2)  
        return res 


def overlap(s1:str, s2:str) -> int:
    '''Identifica a sobreposição máxima entre duas sequências:
    maior sufixo de s1 que pode ser prefixo de s2 e retorna 
    o número de sobreposição
    
    Parameters
    ----------
    :param s1: Sequência 1

    :param s2: Sequência 2
    '''
    maxov = min(len(s1), len(s2))  
    for i in range(maxov, 0, -1):   
        if s1[-i:] == s2[:i]: return i  
    return 0
