# -*- coding: utf-8 -*-
"""
@author: Alexandra, Andreia, Catarina, Daniela
"""

'''@package docstring
Implementação de grafos
'''


"""
Class: MyGraph
"""


class MyGraph:
    """
    Classe MyGraph implementa funções para a construção de grafos, que são estruturas matemáticas compostas por vértices e arcos, que são as ligações entre esses mesmos vértices
    
    """
    def __init__(self, g: list = {}):
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
    
    ## get basic info
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
            for d in self.graph[v]:
                edges.append((v, d))
        return edges

    def size(self) -> tuple:
        """
        Função retorna o tamanho do grafo: nº de vértices e nº de arcos
        
        """
        return len(self.get_nodes()), len(self.get_edges())

    ## add nodes and edges

    def add_vertex(self, v: int) -> list:
        """
        Função adiciona vértices ao grafo se este não existir

        Parameters
        ----------
        :param v: vértice a ser adicionado
        
        """
        if v not in self.graph.keys():
            self.graph[v] = []

    def add_edge(self, o: int, d: int) -> list:
        """
        Função adiciona arco ao grafo se este não existir

        Parameters
        ----------
        :param o: vértice o
        
        :param d: vértice d

        """
        if o not in self.graph.keys():
            self.add_vertex(o)
        if d not in self.graph.keys():
            self.add_vertex(d) 
        if d not in self.graph[o]:
            self.graph[o].append(d) 

    ## successors, predecessors, adjacent nodes

    def get_successors(self, v: int) -> list:
        """
        Função devolve uma lista dos vértices sucessores ao vértice v

        Parameters
        ----------
        :param v: vértice v

        """
        return list(
            self.graph[v])

    def get_predecessors(self, v: int) -> list:
        """
        Função devolve uma lista dos vértices antecessores ao vértice v

        Parameters
        ----------
        :param v: vértice v

        """
        pre = []
        for k in self.graph.keys():
            if v in self.graph[k]:
                pre.append(k)
        return pre

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

    ## degrees

    def out_degree(self, v: int) -> int:
        """
        Função calcula o grau de saída de v

        Parameters
        ----------
        :param v: vértice v

        """
        return len(self.graph[v])

    def in_degree(self, v: int) -> int:
        """
        Função calcula o grau de entrada de v

        Parameters
        ----------
        :param v: vértice v

        """
        return len(self.get_predecessors(v))

    def degree(self, v: int) -> int: 
        """
        Função calcula o grau do vértice v (todos os nós adjacentes, quer percursores quer sucessores)

        Parameters
        ----------
        :param v: vértice v

        """
        return len(self.get_adjacents(v))

    def mean_degree(self, deg_type: str = "inout") -> float:  
        '''Função que permite o cálculo da média dos graus de entrada e saída (ou ambos) para todos
        os nós da rede.

        Parameters
        ----------
        :param deg_type: Tipo de grau, "in", "out", ou "inout" 
        '''   
        degs = self.all_degrees(deg_type)
        return sum(degs.values()) / float(len(degs))

    def prob_degree(self, deg_type: str = "inout") -> dict:          
        '''Função que permite obter a distribuição dos graus dos nodos, permitindo estimar P(k), 
        probabilidade de um nodo ter um grau k, pelas frequências na rede
        
        Parameters
        ----------
        :param deg_type: Tipo de grau, "in", "out", ou "inout" 
        '''
        degs = self.all_degrees(deg_type)
        res = {}
        for k in degs.keys():
            if degs[k] in res.keys():
                res[degs[k]] += 1
            else:
                res[degs[k]] = 1
        for k in res.keys():
            res[k] /= float(len(degs))
        return res

    def all_degrees(self, deg_type: str = "inout") -> dict:
        """
        Função permite o cálculo de graus de entrada e saída (ou ambos) para todos os nós da rede.
        deg_type can be "in", "out", or "inout" 
        """
        degs = {}
        for v in self.graph.keys():
            if deg_type == "out" or deg_type == "inout":
                degs[v] = len(self.graph[v])
            else:
                degs[v] = 0
        if deg_type == "in" or deg_type == "inout":
            for v in self.graph.keys():
                for d in self.graph[v]:
                    if deg_type == "in" or v not in self.graph[d]:
                        degs[d] = degs[d] + 1 
        return degs

    ## BFS and DFS searches

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
            if node != v: res.append(node)
            for elem in self.graph[node]:
                if elem not in res and elem not in l and elem != node:
                    l.append(elem)
        return res

    def reachable_dfs(self,  v: int) -> list:
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
            if node != v: res.append(node)
            s = 0
            for elem in self.graph[node]:
                if elem not in res and elem not in l:
                    l.insert(s, elem)
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
        if s == d: return 0
        l = [(s, 0)]
        visited = [s]
        while len(l) > 0:
            node, dist = l.pop(0)
            for elem in self.graph[node]:
                if elem == d:
                    return dist + 1
                elif elem not in visited:
                    l.append((elem, dist + 1))
                    visited.append(elem)
        return None

    def shortest_path(self, s: int, d: int) -> int:
        """
        Função retorna o caminho mais curto entre o vértice s e d (lista de vértices por onde passa)

        Parameters
        ----------
        :param s: vértice s

        :param d: vértice d

        """
        if s == d: return 0
        l = [(s, [])]
        visited = [s]
        while len(l) > 0:
            node, preds = l.pop(0)
            for elem in self.graph[node]:
                if elem == d:
                    return preds + [node, elem]
                elif elem not in visited:
                    l.append((elem, preds + [node]))
                    visited.append(elem)
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
            node, dist = l.pop(0)
            if node != s:
                res.append((node, dist))
            for elem in self.graph[node]: 
                if not is_in_tuple_list(l, elem) and not is_in_tuple_list(res, elem):
                    l.append((elem, dist + 1))
        return res

## cycles
    def node_has_cycle (self, v: int) -> str:
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
                if elem == v: return True
                elif elem not in visited:
                    l.append(elem)
                    visited.append(elem)
        return res

    def has_cycle(self) -> str:
        """
        Função retorna se o grafo é ou não ciclico

        """
        res = False
        for v in self.graph.keys():
            if self.node_has_cycle(v): return True
        return res

    def clustering_coef(self, v: int) -> float:     
        '''Mede até que ponto cada nó está inserido num grupo coeso

        Parameters
        ----------
        :param v: Nó a analisar
        '''
        adjs = self.get_adjacents(v)
        if len(adjs) <=1: return 0.0
        ligs = 0
        for i in adjs:
            for j in adjs:
                if i != j:
                    if j in self.graph[i] or i in self.graph[j]: 
                        ligs = ligs + 1
        return float(ligs)/(len(adjs)*(len(adjs)-1))
        
    def all_clustering_coefs(self) -> dict:        
        ''' Calcula todos os coefiecientes de clustering
        '''
        ccs = {}
        for k in self.graph.keys():
            ccs[k] = self.clustering_coef(k)
        return ccs
        
    def mean_clustering_coef(self) -> float:        
        '''Calcula a média global dos coeficientes na rede
        '''
        ccs = self.all_clustering_coefs()
        return sum(ccs.values()) / float(len(ccs))
            
    def mean_clustering_perdegree(self, deg_type: str = "inout") -> dict:    
        '''Calcula valores para C(k) para todos os nós
        
        Parameters
        ----------
        :param deg_type: Tipo de grau, "in", "out", ou "inout" 
        '''
        degs = self.all_degrees(deg_type)
        ccs = self.all_clustering_coefs()
        degs_k = {}
        for k in degs.keys():
            if degs[k] in degs_k.keys(): degs_k[degs[k]].append(k)
            else: degs_k[degs[k]] = [k]
        ck = {}
        for k in degs_k.keys():
            tot = 0
            for v in degs_k[k]: tot += ccs[v]
            ck[k] = float(tot) / len(degs_k[k])
        return ck

    ## mean distances ignoring unreachable nodes

    def mean_distances(self) -> tuple:           
        ''' Calcula o comprimento médio dos caminhos mais curtos <L>  sobre todos os pares 
        de nós e a percentagem desses pares (conectados) sobre todos os pares na rede
        '''
        tot = 0
        num_reachable = 0
        for k in self.graph.keys():
            distsk = self.reachable_with_dist(k)
            for _, dist in distsk:
                tot += dist
            num_reachable += len(distsk)
        meandist = float(tot) / num_reachable
        n = len(self.get_nodes())
        return meandist, float(num_reachable) / (( n - 1) * n)  

    def isClique(self, listNodes: list) -> str:
        for node in listNodes:
            lista = self.get_adjacents(node)
            for i in listNodes:
                if i != node:
                    if i not in lista:
                        return False
        return True

    def eIsolado(self, idNo: int) -> str:
        res = self.get_adjacents(idNo)
        if res != None:
            return False
        else:
            return True

    def nosIsolados(self) -> list:
        ress = []
        for nodes in self.graph.keys():
            res = self.eIsolado(nodes)
            if res == True:
                ress.append(nodes)

    ## Hamiltonian

    def check_if_valid_path(self, p: list) -> bool:
        '''Verifica se um caminho é valido, para tal tem de conter todos os nodos do grafo e nao pode ter nodos repetidos
        
        Parameters
        ----------
        :param p: Lista com fragmentos constituintes do caminho 
        '''
        if p[0] not in self.graph.keys(): return False
        for i in range(1,len(p)):
            if p[i] not in self.graph.keys() or p[i] not in self.graph[p[i-1]]:
                return False
        return True
        
    def check_if_hamiltonian_path(self, p: list) -> bool:
        '''Verifica se o caminho é hamiltoniano, para tal tem de ser um caminho válido, 
        passa por todos os nodos do grafo e cada nodo so pode ser visitado uma vez
        
        Parameters
        ----------
        :param p: Lista com fragmentos constituintes do caminho
        '''
        if not self.check_if_valid_path(p): 
            return False
        to_visit = list(self.get_nodes())
        if len(p) != len(to_visit): 
            return False
        for i in range(len(p)):
            if p[i] in to_visit: 
                to_visit.remove(p[i])
            else: 
                return False
        if not to_visit: 
            return True
        else: 
            return False
    
    def search_hamiltonian_path(self) -> list:
        '''Procura caminhos hamiltonianos em todo o grafo e retorna uma lista com os nodos/fragmentos ordenados que constituem o caminho'''
        for ke in self.graph.keys():
            p = self.search_hamiltonian_path_from_node(ke) 
            if p != None:
                return p
        return None
    
    def search_hamiltonian_path_from_node(self, start: str) -> list:
        '''Implementa uma arvore de procura atraves da manutençao do nodo atual a ser processado, o caminho atual a ser construido
        e o estado dos nodos. Constroi um caminho que começa num nodo e que percorre todos os outros nodos

        Parameters
        ----------
        :param start: Nodo inicial
        '''
        current = start
        visited = {start:0}
        path = [start]
        while len(path) < len(self.get_nodes()):
            nxt_index = visited[current]
            if len(self.graph[current]) > nxt_index:
                nxtnode = self.graph[current][nxt_index]
                visited[current] += 1
                if nxtnode not in path:
                    path.append(nxtnode)
                    visited[nxtnode] = 0                    
                    current = nxtnode      
            else: 
                if len(path) > 1: 
                    rmvnode = path.pop()
                    del visited[rmvnode]
                    current = path[-1]
                else: return None
        return path

    # Eulerian

    def check_balanced_node(self,node: str) -> bool:  
        '''Verifica se um nodo é balanceado'''
        return self.in_degree(node) == self.out_degree(node)

    def check_balanced_graph(self) -> bool:  
        '''Verifica se um grafo é balanceado, ou seja, todos os nodos tem de ser balanceados'''
        for n in self.graph.keys():
            if not self.check_balanced_node(n): return False
        return True

    def check_nearly_balanced_graph(self) -> tuple: 
        '''Verifica se um grafo é nearly balanceado. Um grafo direcionado e fortemente conetado tem um circuito euleriano se for nearly balanceado'''
        res = None, None  
        for n in self.graph.keys():
            indeg = self.in_degree(n)
            outdeg = self.out_degree(n)
            if indeg - outdeg == 1 and res[1] is None:
                res = res[0], n
            elif indeg - outdeg == -1 and res[0] is None:
                res = n, res[1]
            elif indeg == outdeg:
                pass
            else:
                return None, None
        return res

    def is_connected(self) -> bool:
        '''Verifica se todos os nodos do grafo estão conetados a partir de qualquer nodo'''
        total = len(self.graph.keys()) - 1
        for v in self.graph.keys():
            reachable_v = self.reachable_bfs(v)
            if (len(reachable_v) < total): return False
        return True

    def eulerian_cycle(self) -> list:
        '''Procura ciclos eulerianos para grafos que contém pelo menos um'''
        from random import randint
        if not self.is_connected() or not self.check_balanced_graph(): return None
        edges_visit = list(self.get_edges())
        vi = edges_visit[randint(0,len(edges_visit)-1)]
        res = [vi] 
        edges_visit.pop(edges_visit.index(vi)) 
        match = False 
        while edges_visit:
            for i in edges_visit: 
                if i[0] == vi[1]: 
                    vi = i
                    res.append(vi)
                    edges_visit.pop(edges_visit.index(vi))
                    break
            for h in edges_visit:
                if vi[1] == h[0]:
                    match = False
                    break
                else:
                    match = True
            if match == True and edges_visit != []: 
                for j in edges_visit:
                    for m in res:
                        if j[0] == m[0]:
                            pos = res.index(m)
                            newpath = res[pos:]
                            newpath.extend(res[:pos])
                            res = newpath
                            vi = res[len(res)-1]
                            match = False
                            break
        path = [] 
        for k in res:
            path.append(k[0]) 
        path.append(res[-1][1]) 
        return path

    def eulerian_path(self) -> list:  
        '''Transforma um grafo nearly balanceado num balanceado atraves da adiçao de um arco que coneta os 2 semi balanceados nodos para torna-los balanceados.
        Retorna o circuito euleriano do grafo original'''
        unb = self.check_nearly_balanced_graph()
        if unb[0] is None or unb[1] is None: return None
        self.graph[unb[1]].append(unb[0])  
        cycle = self.eulerian_cycle()
        for i in range(len(cycle) - 1):
            if cycle[i] == unb[1] and cycle[i + 1] == unb[0]:
                break
        path = cycle[i+1:] + cycle[1:i+1]
        return path


def is_in_tuple_list(tl: list, val: int) -> str:
    """
    Função verifica se val esta na lista de tuplos (tl)

    Parameters
    ----------
    :param tl: lista de tuplos

    :param val: valor

    """
    res = False
    for (x,y) in tl:
        if val == x: return True
    return res


    