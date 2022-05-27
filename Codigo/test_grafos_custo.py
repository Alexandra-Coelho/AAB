# -- coding: utf-8 --
"""
@author: Alexandra,Andreia,Catarina,Daniela
"""

'''@package docstring
Implementação de testes para as funções da Class MyGraph_custo
'''


"""
Class: TestGrafoscustos
"""

import unittest
from mygraph_custos import MyGraph_custo

class TestGrafoscustos (unittest.TestCase):   

    def setUp(self): 
        self.t1 = MyGraph_custo({1: [(2,2)], 2: [(3,4)], 3: [(2,3), (4,2)], 4: [(2,5)]})
        self.t2 = MyGraph_custo()
        self.t3 = MyGraph_custo({1: [(2,2)], 2: [(3,4)], 3: [(2,3), (4,2)], 4: [(2,5)]})
    def test_get_nodes(self):
        self.assertEqual(self.t1.get_nodes(),[1, 2, 3, 4])
    def test_edges(self):
        self.assertEqual(self.t1.get_edges(),[(1, 2, 2), (2, 3, 4), (3, 2, 3), (3, 4, 2), (4, 2, 5)])
    def test_reachable_bfs(self):
        self.assertEqual(self.t1.reachable_bfs(4),[2, 3])
        self.assertEqual(self.t1.reachable_bfs(1),[2, 3, 4])
        self.assertEqual(self.t1.reachable_bfs(2),[3, 4])
        self.assertEqual(self.t1.reachable_bfs(3),[2, 4])
    def test_reachable_dfs(self):
        self.assertEqual(self.t1.reachable_dfs(4),[2, 3])
        self.assertEqual(self.t1.reachable_dfs(1),[2, 3, 4])
        self.assertEqual(self.t1.reachable_dfs(2),[3, 4])
        self.assertEqual(self.t1.reachable_dfs(3),[2, 4])
    def test_distance(self):
        self.assertEqual(self.t1.distance(2,4),6)
        self.assertEqual(self.t1.distance(1,4),8)
        self.assertEqual(self.t1.distance(1,3),6)
        self.assertEqual(self.t1.distance(3,4),2)
    def test_shortest_path(self):
        self.assertEqual(self.t1.shortest_path(2,4),([(2, 3), (3, 4)], 6))
    def test_get_successors(self):
        self.assertEqual(self.t1.get_successors(2),[3])
        self.assertEqual(self.t1.get_successors(3),[2, 4])
        self.assertEqual(self.t1.get_successors(1),[2])
        self.assertEqual(self.t1.get_successors(4),[2])
    def test_dget_predecessors(self):
        self.assertEqual(self.t1.get_predecessors(2),[1, 3, 4])
        self.assertEqual(self.t1.get_predecessors(3),[2])
        self.assertEqual(self.t1.get_predecessors(4),[3])
        self.assertEqual(self.t1.get_predecessors(1),[])
    def test_get_adjacents(self):
        self.assertEqual(self.t1.get_adjacents(2),[1, 3, 4])
        self.assertEqual(self.t1.get_adjacents(3),[2, 4])
        self.assertEqual(self.t1.get_adjacents(4),[3, 2])
        self.assertEqual(self.t1.get_adjacents(1),[2])
    def test_in_degree(self):
        self.assertEqual(self.t1.in_degree(2),3)
    def test_out_degree(self):
        self.assertEqual(self.t1.out_degree(2),1)
    def test_degree(self):
        self.assertEqual(self.t1.degree(2),3)
    def test_reachable_with_dist(self):
        self.assertEqual(self.t1.reachable_with_dist(1),[(2, 2), (3, 6), (4, 8)])
        self.assertEqual(self.t1.reachable_with_dist(4),[(2, 5), (3, 9)])
    def test_has_cycle(self):
        self.assertEqual(self.t1.has_cycle(),True)
    def test_node_has_cycle(self):
        self.assertEqual(self.t1.node_has_cycle(2),True)
        self.assertEqual(self.t1.node_has_cycle(1),False)
        self.assertEqual(self.t1.node_has_cycle(4),True)
        self.assertEqual(self.t1.node_has_cycle(3),True)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit = False)