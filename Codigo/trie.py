# -- coding: utf-8 --
"""
@author: Alexandra, Andreia, Catarina, Daniela
"""

'''@package docstring
Implementação de tries
'''


"""
Class: Trie
"""

from io import StringIO
import pprint

class Trie:
    """
    Representa uma árvore como sendo uma série de dicionários uns dentro dos outros,
    tendo em consideração padrões inseridos para a procura de padrões em sequências
    """

    def __init__(self, seqs:list):
        """
        Guarda a árvore e os padrões inseridos
        
        Parameters
        ----------
        :param seqs: Uma lista de padrões que serão inseridos na árvore
        """
        self.trie = {}
        for seq in seqs:
            self.insert(seq)

    def __repr__(self) -> str:
        """
        Imprime a árvore num formato apropriado
        """
        sio = StringIO()
        pprint.pprint(self.trie, width = 1, stream = sio)
        return sio.getvalue()

    def insert(self, pat:str):
        """
        Insere um ou uma lista de padrões na árvore
        
        Parameters
        ----------
        :param pat: Um padrão ou lista de padrões que serão inseridos na árvore
        """
        t = self.trie 
        for x in pat: 
            if x not in t:
                t[x] = {}
            t = t[x]
        t['#$#'] = 0
    
    def matches(self, seq:str) -> bool:
        """
        Verifica se a sequência pertence à árvore (retorna True) ou não (retorna False), ou seja,
        procura a ocorrência de um dos padrões como prefixo da sequencia
        
        Parameters
        ----------
        :param seq: Padrão a ser procurado na árvore
        """
        t = self.trie
        for x in seq:
            if x not in t: return False
            t = t[x]
        return '#$#' in t

    def prefix_trie_match(self, text:str) -> list:
        """
        Devolve uma lista com a ocorrência de prefixos da sequência pertencente à árvore
        e procura se um padrão representado é prefixo da sequência
        
        Parameters
        ----------
        :param text: Sequência que irá ser processada por sufixos pertencentes à árvore
        """
        all_prefix = []
        for i in range(len(text)+1):
            all_prefix.append(text[0:i])
        res = []
        for pref in all_prefix:
            if self.matches(pref):
                res.append(pref)
        return res

    def trie_matches(self, text:str) -> list:
        """
        Devolve uma lista de tuplos incluindo as subsequências da sequência fornecida
        que pertencem à árvore bem como os respetivos índices na sequência
        
        Parameters
        ----------
        :param text: Sequência a ser processada por subsequências pertencentes à árvore
        """
        suffix = []
        for i in range(len(text)):
            suffix.append(text[i:])
        result = []
        for i, sfx in enumerate(suffix):
            for res in self.prefix_trie_match(sfx):
                result.append((res, i))
        return result
