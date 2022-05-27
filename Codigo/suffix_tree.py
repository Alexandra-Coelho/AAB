# -- coding: utf-8 --
"""
@author: Alexandra, Andreia, Catarina, Daniela
"""

'''@package docstring
Implementação da árvore de sufixos
'''


"""
Class: SuffixTree
"""

from io import StringIO
import pprint
sio = StringIO()

class SuffixTree:
    """
    Constrói uma árvore de sufixos a partir de um dado padrão para ser possível a sua procura em sequências
    """
    def __init__(self, pat:str = ""):
        """
        Cria a árvore de sufixos com base no padrão fornecido
        
        Parameters
        ----------
        :param pat: Padrão utilizado para criar a árvore de sufixos
        """
        self.tree = {}
        self.insert(pat)

    def __repr__(self) -> str:
        """
        Imprime de forma mais apresentável a árvore de sufixos
        """
        pprint.pprint(self.tree, width = 1, stream = sio)
        return sio.getvalue()
        
    def insert(self, pat:str):
        """
        A partir do padrão fornecido cria a árvore de sufixos
        
        Parameters
        ----------
        :param pat: Padrão a partir do qual irá ser construída a árvore de sufixos
        """
        root = self.tree
        trees = []
        for i, x in enumerate(pat): 
            trees.append((i, root))
            new_trees = []
            while trees: 
                I, t = trees.pop()
                if x not in t:
                    t[x] = {}
                new_trees.append((I, t[x])) 
            trees = new_trees
        for i, t in trees:
            t['$'] = i 
    
    def find_pattern(self, seq:str) -> list:
        """
        Retorna uma lista de índices correspondentes à posição da sequência fornecida no padrão,
        caso não se verifique retorna 'False'
        
        Parameters
        ----------
        :param seq: Uma sequência a ser procurada no padrão
        """
        tree = self.tree
        for s in seq: 
            if s not in tree: 
                return False
            tree = tree[s] 
        return self.get_leafs_below(tree)
    
    def get_leafs_below(self, tree:dict) -> list: 
        """
        Função auxiliar que retorna uma coleção das folhas abaixo de um determinado nodo
        lista de todos os índices abaixo do nodo especificado da árvore
        Coleta as folhas abaixo de um dado nodo
        
        Parameters
        ----------
        :param tree: Nodo da árvore (parte do dicionário principal)
        """
        res = []
        for k in tree.keys(): 
            if k == "$": 
                res = [*res, tree["$"]] 
            else:
                res = [*res, *self.get_leafs_below(tree[k])]
        return res


