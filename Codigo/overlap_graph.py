"""
@author: Alexandra, Andreia, Catarina, Daniela
"""

'''@package docstring
Implementação de grafos de sobreposição
'''


"""
Class: OverlapGraph
"""

from mygraph import MyGraph

class OverlapGraph(MyGraph):
    """
    Classe OverlapGraph implementa funções para a construção de grafos de sobreposiçao, que são estruturas matemáticas compostas por vértices e arcos, que são as ligações entre esses mesmos vértices
    
    """
    
    def __init__(self, frags: list, reps=False):
        """
        Construtor que recebe como parametro de entrada uma lista de fragmentos e reps que corresponde se há reptições de fragmentos ou não 
        
        Parameters
        ----------
        :param frags: lista de fragmentos
        :param reps: informa se existe repetições de fragmentos, por default, não existe repetiçao (False)
        
        """
        MyGraph.__init__(self, {})
        if reps:
            self.create_overlap_graph_with_reps(frags)
        else:
            self.create_overlap_graph(frags)
        self.reps = reps

## create overlap graph from list of sequences (fragments)

    def create_overlap_graph(self, frags: list):  
        """Constrói o grafo de sobreposiçao sem repetições de fragmentos a partir de uma lista de fragmentos

        Parameters
        ----------
        :param frags: lista de fragmentos
        """
        frags=sorted(frags)
        for seq in frags: 
            self.add_vertex(seq) 
        for seq in frags: 
            suf = suffix(seq) 
            for seq2 in frags: 
                if prefix(seq2) == suf: 
                    self.add_edge(seq, seq2) 

    def create_overlap_graph_with_reps(self,frags: list):
        """Constrói o grafo de sobreposiçao com repetições de fragmentos a partir de uma lista de fragmentos. 
        No caso de replicas de fragmentos adicionar um identificador numerico aos fragmentos

        Parameters
        ----------
        :param frags: lista de fragmentos
        """
        frags = sorted(frags)
        idnum = 1
        for seq in frags:
            self.add_vertex(seq + "-" + str(idnum))
            idnum = idnum + 1
        idnum = 1
        for seq in frags:
            suf = suffix(seq)
            for seq2 in frags:
                if prefix(seq2) == suf:
                    for x in self.get_instances(seq2): 
                        self.add_edge(seq + "-" + str(idnum), x) 
            idnum = idnum + 1


    def get_instances(self, seq: str) -> list:
        """Procura todos os nodos que contem uma determinada sequencia

        Parameters
        ----------
        :param seq: Sequencia a procurar
        """
        res = []
        for k in self.graph.keys(): 
            if seq in k: res.append(k) 
        return res
    
    def get_seq(self, node: str) -> str:
        """Vai buscar a sequencia/fragmento representada pelo nodo

        Parameters
        ----------
        :param node: nodo a procurar
        """
        if node not in self.graph.keys(): return None 
        if self.reps: return node.split("-")[0] 
        else: return node 
    
    def seq_from_path(self, path: list) -> str:
        """Obtem a sequencia completa do caminho no grafo hamiltoniano, ou seja, retorna a sequencia original que originou os fragmentos

        Parameters
        ----------
        :param path: caminho
        """
        if not self.check_if_hamiltonian_path(path): 
            return None
        seq = self.get_seq(path[0]) 
        for i in range(1, len(path)):
            nxt = self.get_seq(path[i]) 
            seq += nxt[-1]
        return seq


    # auxiliary
def composition(k:int, seq:str) -> list:
    """Esta função representa uma lista de todas as subsequencias de tamanho k da sequencia, possivelmente pode incluir
    subsequencias repetidas e os fragmentos resultantes sao ordenados lexicograficamente

        Parameters
        ----------
        :param k: tamanho k dos fragmentos a obter 
        :param seq: sequencia original
        """
    res = [ ]
    for i in range(len(seq)-k+1):
        res.append(seq[i:i+k])
    res.sort()
    return res
     
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

