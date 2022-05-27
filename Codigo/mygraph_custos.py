# -- coding: utf-8 --
"""
@author: Alexandra,Andreia,Catarina,Daniela
"""

'''@package docstring
Implementação de grafos com custos
'''


"""
Class: MyGraph_custo
"""

class MyGraph_custo:
    """
    Classe MyGraph_custo implementa funções para a construção de grafos, que são estruturas matemáticas compostas por vértices e arcos, que são as ligações entre esses mesmos vértices
    
    """
    def __init__(self, g: dict = {}):
        """
        Construtor que recebe como parametro de entrada um dicionário
        
        Parameters
        ----------
        :param g: dicionário, por default, o dicionário é vazio
        
        """
        self.graph = g

    def print_graph(self):
        """
        Função permite imprimir o conteúdo do grafo como uma lista
        
        """
        for v in self.graph.keys(): 
            print(v, " -> ", self.graph[v]) 


    def get_nodes(self) -> list:
        """
        Função retorna uma lista com os vértices do grafo
        
        """
        return list(self.graph.keys())

    def get_edges(self) -> list:
        """
        Função retorna uma lista de pares (tuplos) com os arcos do grafo onde estão presentes a origem, destino e peso
        
        """
        edges = [] 
        for v in self.graph.keys(): 
            for des in self.graph[v]: 
                d, wg = des
                edges.append((v, d, wg)) 
        return edges

    def size(self) -> tuple:
        """
        Função retorna o tamanho do grafo: nº de vértices e nº de arcos
        
        """
        return len(self.get_nodes()), len(self.get_edges())


    def add_vertex(self, v: int) -> list:
        """
        Função adiciona vértices ao grafo se este não existir

        Parameters
        ----------
        :param v: vértice a ser adicionado
        
        """
        if v not in self.graph.keys(): 
            self.graph[v] = [] 

    def add_edge(self, o: int, d: int, wg: int) -> list:
        """
        Função adiciona arco ao grafo se este não existir

        Parameters
        ----------
        :param o: vértice o
        
        :param d: vértice d

        :param wg: peso do arco que liga o a d

        """
        if o not in self.graph.keys():  
            self.add_vertex(o)
        if d not in self.graph.keys(): 
            self.add_vertex(d)
        des = [] 
        for j in self.graph[o]: 
            d, wg = j  
            des.append(d)
        if d not in des:
            self.graph[o].append((d, wg))


    def get_successors(self, v: int) -> list: 
        """
        Função devolve uma lista dos vértices sucessores ao vértice v

        Parameters
        ----------
        :param v: vértice v

        """
        res = []
        for j in self.graph[v]: 
            d, wg = j 
            res.append(d) 
        return res  

    def get_predecessors(self, v: int) -> list: 
        """
        Função devolve uma lista dos vértices antecessores ao vértice v

        Parameters
        ----------
        :param v: vértice v

        """
        lista = []
        for i in self.graph.keys(): 
            for tupls in self.graph[i]: 
                d, wg = tupls 
                if d == v: 
                    lista.append(i)
        return lista

    def get_adjacents(self, v: int) -> list: 
        """
        Função devolve uma lista dos vértices adjacentes ao vértice v

        Parameters
        ----------
        :param v: vértice v

        """
        suc = self.get_successors(v)  
        pred = self.get_predecessors(v)  
        res = pred
        for p in suc:  
            if p not in res:
                res.append(p)
        return res

    def out_degree(self, v: int) -> int:
        """
        Função calcula o grau de saída de v

        Parameters
        ----------
        :param v: vértice v

        """
        li = self.get_successors(v)
        return len(li)

    def in_degree(self, v: int) -> int:
        """
        Função calcula o grau de entrada de v

        Parameters
        ----------
        :param v: vértice v

        """
        li = self.get_predecessors(v)
        return len(li)

    def degree(self, v: int) -> int:
        """
        Função calcula o grau do vértice v (todos os nós adjacentes, quer percursores quer sucessores)

        Parameters
        ----------
        :param v: vértice v

        """
        li = self.get_adjacents(v)
        return len(li)

    def reachable_bfs(self, v: int) -> list:
        """
        Função faz a travessia do grafo em largura (esquerda-direita), começando no vertice de origem v, usando uma queue, first in-first out

        Parameters
        ----------
        :param v: vértice de origem v

        """
        l = [v] 
        res = []  
        while len(l) > 0:  
            node = l.pop(0)  
            if node != v:  
                res.append(node)  
            for elem in self.graph[node]:  
                nwnode, wg = elem
                if nwnode not in res and nwnode not in l and nwnode != node:  
                    l.append(nwnode) 
        return res 

    def reachable_dfs(self, v: int) -> list:
        """
        Função faz a travessia do grafo em profundidade (cima-baixo) começando no vertice de origem v, usando uma stack, last in-first out 

        Parameters
        ----------
        :param v: vértice de origem v

        """
        l = [v]
        res = []
        while len(l) > 0:
            node = l.pop(0) 
            s = 0
            if node != v:  
                res.append(node)  
            for elem in self.graph[node]:
                nwnode, wg = elem 
                if nwnode not in res and nwnode not in l:
                    l.insert(s, nwnode) 
                    s += 1 
        return res

    def distance(self, s: int, d: int) -> int:
        """
        Função retorna a distância entre vértice s e d

        Parameters
        ----------
        :param s: vértice s

        :param d: vértice d

        """
        if s == d:
            return 0
        else:
            l = [(s, 0)] 
            vis = [s]  
            while len(l) > 0:  
                node, swg = l.pop(0) 
                for elem in self.graph[node]:  
                    nwnode, wg = elem 
                    if nwnode == d:  
                        return swg + wg
                    if nwnode not in vis and nwnode not in l and nwnode != node:  
                        l.append((nwnode, swg + wg)) 
                        vis.append(nwnode)
            return None

    def shortest_path(self, s: int, d: int) -> int: 
        """
        Função retorna o caminho mais curto entre o vértice s e d (lista de vértices por onde passa)

        Parameters
        ----------
        :param s: vértice s

        :param d: vértice d

        """
        if s == d: 
            return [s, d]
        else:
            l = [(s, [], 0)]  
            visited = [s]  
            while len(l) > 0:  
                node, path, dist = l.pop(0)  
                custo_min = 999999999
                for elem in self.graph[node]:
                    vertice, custo = elem 
                    if vertice == d: 
                        return path + [(node, vertice)], dist + custo 
                    if custo < custo_min: 
                        custo_min = custo
                        vert_custo_min = vertice 
                if vert_custo_min not in visited:  
                    l.append((vert_custo_min, path + [(node, vert_custo_min)], dist + custo_min))
                    visited.append(vert_custo_min)
            return None

    def reachable_with_dist(self, s: int) -> list:  
        """
        Função retorna uma lista de vértices antingíveis a partir de s com respetiva distância

        Parameters
        ----------
        :param s: vértice s

        """
        res = []
        l = [(s, 0)] 
        while len(l) > 0:
            node, swg = l.pop(0)
            if node != s: 
                 res.append((node, swg))
            for elem in self.graph[node]:
                nwnode, wg = elem 
                if not is_in_tuple_list(l, nwnode) and not is_in_tuple_list(res, nwnode):  
                    l.append((nwnode, swg + wg)) 
        return res

    def node_has_cycle(self, v: int) -> str:
        """
        Função retorna se o vértice acrescentado forma um ciclo no grafo

        Parameters
        ----------
        :param v: vértice v

        """
        l = [v] 
        res = False
        visited = [v] 
        while len(l) > 0: 
            node = l.pop(0) 
            for elem in self.graph[node]: 
                nwnode,wg = elem
                if nwnode == v:
                    return True
                elif nwnode not in visited:
                    l.append(nwnode)
                    visited.append(nwnode)
        return res

    def has_cycle(self) -> str:
        """
        Função retorna se o grafo é ou não ciclico

        """
        res = False
        for v in self.graph.keys(): 
            if self.node_has_cycle(v): 
                return True
        return res


def is_in_tuple_list(tl: list, val: int) -> str:
    """
    Função verifica se val esta na lista de tuplos (tl)

    Parameters
    ----------
    :param tl: lista de tuplos

    :param val: valor

    """
    res = False
    for (x, y) in tl: 
        if val == x: 
            return True
    return res






