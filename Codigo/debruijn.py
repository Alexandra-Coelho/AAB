"""
@author: Alexandra, Andreia, Catarina, Daniela
"""

'''@package docstring
Implementação do grafo DeBruijn
'''


"""
Class: DeBruijnGraph
"""

from mygraph import MyGraph

class DeBruijnGraph (MyGraph):
    """
    Classe DeBruijnGraph implementa funções para a construção de grafos de DeBruijn, que são estruturas matemáticas compostas por vértices e arcos, que são as ligações entre esses mesmos vértices
    Os fragmentos representam arcos, o caminho pelo grafo contem todos os arcos somente uma vez. Enquanto que os nodos contem sequencias que correspondem a prefixo ou sufixo de um dos fragmentos
    """
    
    def __init__(self, frags: list):
        """
        Construtor que recebe como parametro de entrada uma lista de fragmentos
        
        Parameters
        ----------
        :param frags: lista de fragmentos
        
        """
        MyGraph.__init__(self, {})
        self.frags = frags
        self.create_deBruijn_graph(frags)

    def add_edge(self, o: int, d: int) -> list:
        """
        Função adiciona arco ao grafo se este não existir. Permite arcos repetidos entre o mesmo par de nodos.

        Parameters
        ----------
        :param o: vértice o
        
        :param d: vértice d
        """
        if o not in self.graph.keys():
            self.add_vertex(o)
        if d not in self.graph.keys():
            self.add_vertex(d)
        self.graph[o].append(d)

    def in_degree(self, v: int) -> int:
        """
        Função calcula o grau de entrada de v, tendo em consideração a possibilidade de multiplos arcos com a mesma origem e sucessor

        Parameters
        ----------
        :param v: vértice v
        """
        res = 0
        for k in self.graph.keys():
            if v in self.graph[k]:
                res += self.graph[k].count(v)
        return res

    def create_deBruijn_graph(self, frags: list):
        """
        Função implementa a criaçao do grafo de Debruijn, em que os arcos representam os fragmentos e os nodos sao o prefixo e sufixo de um fragmento

        Parameters
        ----------
        :param frags: lista de fragmentos
        """
        for seq in frags:
            suf = suffix(seq) 
            self.add_vertex(suf)
            pref = prefix(seq)
            self.add_vertex(pref)
            self.add_edge(pref, suf)
            

    def seq_from_path(self, path: list) -> str:
        """
        Função que retorna a sequencia original que originou os fragmentos a partir do caminho
        
        Parameters
        ----------
        :param path: caminho
        """
        seq = path[0]
        for i in range(1,len(path)):
            nxt = path[i]
            seq += nxt[-1]
        return seq

def suffix (seq: str) -> str:
    """Retorna o sufixo de uma sequencia

        Parameters
        ----------
        :param seq: sequencia
        """ 
    return seq[1:]

    
def prefix(seq: str) -> str:
    """Retorna o prefixo de uma sequencia

        Parameters
        ----------
        :param seq: sequencia
        """
    return seq[:-1]

def composition(k:int, seq:str) -> list:
    """Esta função representa uma lista de todas as subsequencias de tamanho k da sequencia, possivelmente pode incluir
    subsequencias repetidas e os fragmentos resultantes sao ordenados lexicograficamente

        Parameters
        ----------
        :param k: tamanho k dos fragmentos a obter 
        :param seq: sequencia original
        """
    res = []
    for i in range(len(seq)-k+1):
        res.append(seq[i:i+k])
    res.sort()
    return res