# -*- coding: utf-8 -*-
"""
@author: Alexandra,Andreia,Catarina,Daniela
"""

'''@package docstring
Implementação de redes biológicas
'''


"""
Class: Metabolic Network 
"""

from mygraph import MyGraph


class MetabolicNetwork(MyGraph): 
    '''É uma subclasse da classe MyGraph. Implementa uma rede metabólica que representa o metabolismo-
    conjunto de reações químicas e os compostos envolvidos (metabolitos)
    '''
    def __init__(self, network_type: str = "metabolite-reaction", split_rev: bool = False):
        '''Chama o construtor da classe MyGraph para construir e guardar o grafo.
        Guarda o tipo de rede e o tipo de nós. Se tiver reações reversíveis pode dividí-las em duas reações distintas.

        Parameters
        ----------
        :param network_type: Guarda o tipo de rede a ser construída, por default é 'metabolite-reaction'
        :param split_rev: Define se as reações irreversíveis são ou não separadas em duas reações distintas,
        por default é 'False' - não divide em duas reações
        '''
        MyGraph.__init__(self,{}) 
        self.net_type = network_type 
        self.node_types = {}  
        if network_type == "metabolite-reaction":  
            self.node_types["metabolite"] = [] 
            self.node_types["reaction"] = []  
        self.split_rev = split_rev

    def add_vertex_type(self, v: str, nodetype: str): 
        '''Adiciona um novo nó ao grafo

        Parameters
        ----------
        :param v: Nome do nó- ex: 'R1'
        :param nodetype: Tipo do nó adicionado- ex: 'reaction'
        '''
        self.add_vertex(v) 
        self.node_types[nodetype].append(v)  
    def get_nodes_type(self, node_type: str) -> list: 
        ''' Retorna uma lista com os nós de um certo tipo, se não existir nós desse tipo retorna None

        Parameters
        ----------
        :param nodetype: Tipo do nó- ex: 'reaction'
        '''
        if node_type in self.node_types: 
            return self.node_types[node_type]  
        else:
            return None

    def load_from_file(self, filename: str): 
        '''Carrega um ficheiro com reações para criar uma rede 'metabolite-reaction'.
        Se for para criar outro tipo de rede, esta é convertida a partir da rede 'metabolite-reaction'

         Parameters
        ----------
        :param filename: Nome do ficheiro que quero carregar que contém as reações
        '''
        rf = open(filename)
        gmr = MetabolicNetwork("metabolite-reaction")  
        for line in rf:  
            if ":" in line:
                tokens = line.split(":")
                reac_id = tokens[0].strip()
                gmr.add_vertex_type(reac_id, "reaction")
                rline = tokens[1]
            else:
                raise Exception("Invalid line:")
            if "<=>" in rline:
                left, right = rline.split("<=>")
                mets_left = left.split("+")
                for met in mets_left:
                    met_id = met.strip()
                    if met_id not in gmr.graph:
                        gmr.add_vertex_type(met_id, "metabolite")
                    if self.split_rev:
                        gmr.add_vertex_type(reac_id + "_b", "reaction")
                        gmr.add_edge(met_id, reac_id)
                        gmr.add_edge(reac_id + "_b", met_id)
                    else:
                        gmr.add_edge(met_id, reac_id)
                        gmr.add_edge(reac_id, met_id)
                mets_right = right.split("+")
                for met in mets_right:
                    met_id = met.strip()
                    if met_id not in gmr.graph:
                        gmr.add_vertex_type(met_id, "metabolite")
                    if self.split_rev:
                        gmr.add_edge(met_id, reac_id + "_b")
                        gmr.add_edge(reac_id, met_id)
                    else:
                        gmr.add_edge(met_id, reac_id)
                        gmr.add_edge(reac_id, met_id)
            elif "=>" in line:
                left, right = rline.split("=>")  
                mets_left = left.split("+")
                for met in mets_left:
                    met_id = met.strip()
                    if met_id not in gmr.graph:
                        gmr.add_vertex_type(met_id, "metabolite")
                    gmr.add_edge(met_id, reac_id)
                mets_right = right.split("+")
                for met in mets_right:
                    met_id = met.strip()
                    if met_id not in gmr.graph:
                        gmr.add_vertex_type(met_id, "metabolite")
                    gmr.add_edge(reac_id, met_id)
            else:
                raise Exception("Invalid line:")
        if self.net_type == "metabolite-reaction": 
            self.graph = gmr.graph 
            self.node_types = gmr.node_types
        elif self.net_type == "metabolite-metabolite":
            self.convert_metabolite_net(gmr) 
        elif self.net_type == "reaction-reaction":
            self.convert_reaction_graph(gmr) 
        else:
            self.graph = {}
        rf.close()

    def convert_metabolite_net(self, gmr: dict): 
        '''Conversão da rede 'metabolite-reaction' em rede 'metabolite-metabolite'

        Parameters
        ----------
        :param gmr: Grafo que contém a rede 'metabolite-reaction' a converter
        '''
        for m in gmr.node_types["metabolite"]: 
            self.add_vertex(m)
            sucs = gmr.get_successors(m)  
            for s in sucs: 
                sucs_r = gmr.get_successors(s)  
                for s2 in sucs_r: 
                    if m != s2: 
                        self.add_edge(m, s2)

    def convert_reaction_graph(self, gmr: dict): 
        '''Conversão da rede 'metabolite-reaction' em rede 'reaction-reaction'

        Parameters
        ----------
        :param gmr: Grafo que contém a rede 'metabolite-reaction' a converter
        '''
        for r in gmr.node_types["reaction"]:  
            self.add_vertex(r) 
            sucs = gmr.get_successors(r)  
            for s in sucs:  
                sucs_r = gmr.get_successors(s)  
                for s1 in sucs_r: 
                    if r != s1: 
                        self.add_edge(r, s1)  

    def active_reactions(self, active_metabolites: list) -> list:
        '''Determina todas as reações ativas- reações em que todos os substratos
        estão na lista

        Parameters
        ----------
        :param active_metabolites: lista de metabolitos ativos existentes
        '''
        if self.net_type != "metabolite-reaction" or not self.split_rev:
            return None
        res = []
        for v in self.node_types['reaction']:
            preds = set(self.get_predecessors(v))
            if len(preds)>0 and preds.issubset(set(active_metabolites)):
                res.append(v)
        return res
    
    def produced_metabolites(self, active_reactions: list) -> list:
        ''' Determina os metabolitos que podem ser produzidos- produtos das
        reações ativas

        Parameters
        ----------
        :param active_reactions: lista de reações ativas existentes
        '''
        res = []
        for r in active_reactions:
            sucs = self.get_successors(r)
            for s in sucs:
                if s not in res: res.append(s)
        return res

    def all_produced_metabolites(self, initial_metabolites: list) -> list:
        ''' Calcula todos os metabolitos 'finais' que poderão ser produzidos

        Parameters
        ----------
        :param initial_metabolites: lista de metabolitos iniciais
        '''
        mets = initial_metabolites
        cont = True
        while cont:
            cont = False
            reacs = self.active_reactions(mets)
            new_mets = self.produced_metabolites(reacs)
            for nm in new_mets: 
                if nm not in mets: 
                    mets.append(nm)
                    cont = True
        return mets

    def final_metabolites(self):
        '''Detecta o conjunto de metabolitos “finais”- metabolitos que são produzidos
        por pelo menos uma reação, mas não são consumidos por nenhuma reação na rede
        '''
        res = []
        for v in self.graph.keys():
            if v[0] == "M":
                if len(self.get_predecessors(v) ) > 0:
                    if self.get_successors(v) == []:
                        res.append(v)
        return res

    def shortest_path_product(self, initial_metabolites: list, target_product: str) -> list:
        '''Encontra o caminho mais curto, lista mais curta de reações ativadas,para produzir um metabolito alvo. 
        Retorna 'None' se o metabolito alvo não puder ser produzido a partir da lista de metabolitos iniciais
        Observação: as reações na lista só são válidas se puderem ser ativas na ordem dada (todos os seus substratos
        existirem)

        Parameters
        ----------
        :param initial_metabolites: lista de metabolitos iniciais
        :param target_product: metabolito alvo
        '''
        if target_product in initial_metabolites: 
            return []
        metabs = {}
        for m in initial_metabolites: 
            metabs[m] = []
        reacs = self.active_reactions(initial_metabolites)
        cont = True
        while cont:
            cont = False
            for r in reacs:
                sucs = self.get_successors(r)
                preds = self.get_predecessors(r)
                for s in sucs:
                    if s not in metabs: 
                        previous = []
                        for p in preds:
                            for rr in metabs[p]:
                                if rr not in previous: previous.append(rr)
                        metabs[s] = previous + [r]
                        if s == target_product: 
                            return metabs[s]
                        cont = True
            if cont: 
                reacs = self.active_reactions(metabs.keys())
        return None