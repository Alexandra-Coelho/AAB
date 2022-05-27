# -*- coding: utf-8 -*-
"""
@author: Alexandra,Andreia,Catarina,Daniela
"""

'''@package docstring
Teste Metabolic Network
'''


"""
Class: Testes
"""


import unittest
from metabolicnetwork import MetabolicNetwork
from mygraph import MyGraph


class Testes(unittest.TestCase):
    def setUp(self):
        self.t1 = MetabolicNetwork('metabolite-reaction')
        self.t2 = MetabolicNetwork("metabolite-metabolite")
        self.t3 = MetabolicNetwork("reaction-reaction")
        self.t4 = MetabolicNetwork("metabolite-reaction", True)
        self.t5 = MetabolicNetwork("reaction-reaction", True) 
        self.t4.load_from_file("reactions.txt")
    def test_addnodes_type(self):
        self.t1.add_vertex_type("R1", "reaction")
        self.t1.add_vertex_type("R2", "reaction")
        self.t1.add_vertex_type("R3", "reaction")
        self.t1.add_vertex_type("M1", "metabolite")
        self.t1.add_vertex_type("M2", "metabolite")
        self.t1.add_vertex_type("M3", "metabolite")
        self.t1.add_vertex_type("M4", "metabolite")
        self.t1.add_vertex_type("M5", "metabolite")
        self.t1.add_vertex_type("M6", "metabolite")
        self.assertEqual(self.t1.get_nodes_type("reaction"),['R1', 'R2', 'R3'])
        self.assertEqual(self.t1.get_nodes_type("metabolite"), ['M1', 'M2', 'M3', 'M4', 'M5', 'M6'])
    def test_load_from_file(self):
        self.t1.load_from_file("reactions.txt")
        self.assertEqual(self.t1.get_nodes_type("reaction"),['R1', 'R2', 'R3'])
        self.assertEqual(self.t1.get_nodes_type("metabolite"), ['M1', 'M2', 'M3', 'M4', 'M6', 'M5'])
        self.assertEqual(self.t1.get_nodes(), ['R1', 'M1', 'M2', 'M3', 'M4', 'R2', 'M6', 'R3', 'M5'])
        self.t2.load_from_file("reactions.txt")
        self.assertEqual(self.t2.get_nodes(),['M1', 'M3', 'M4', 'M2', 'M5', 'M6'])
        self.t3.load_from_file("reactions.txt")
        self.assertEqual(self.t3.get_nodes(),['R1', 'R2', 'R3'])
        self.t4.load_from_file("reactions.txt")
        self.assertEqual(self.t4.get_nodes_type("reaction"),['R1', 'R2', 'R3', 'R3_b', 'R3_b'])
        self.assertEqual(self.t4.get_nodes_type("metabolite"), ['M1', 'M2', 'M3', 'M4', 'M6', 'M5'])
        self.assertEqual(self.t4.get_nodes(),['R1', 'M1', 'M2', 'M3', 'M4', 'R2', 'M6', 'R3', 'R3_b', 'M5'])
        self.t5.load_from_file("reactions.txt")
        self.assertEqual(self.t5.get_nodes(),['R1', 'R2', 'R3', 'R3_b'])
    def test_active_reactions(self):
        self.assertEqual(self.t4.active_reactions(["M1","M2"]),['R1'])
    def test_produced_metabolites(self):
        self.assertEqual(self.t4.produced_metabolites(["R1"]),['M3', 'M4'])
    def test_all_produced_metabolites(self):
        self.assertEqual(self.t4.all_produced_metabolites(["M1","M2"]),['M1', 'M2', 'M3', 'M4'])
        self.assertEqual(self.t4.all_produced_metabolites(["M6"]),['M6', 'M4', 'M5', 'M3'])
    def test_final_metabolites(self):
        self.assertEqual(self.t4.final_metabolites(),['M3'])
    def test_shortest_path_product(self):
        self.assertEqual(self.t4.shortest_path_product(["M1","M2"], "M4"),['R1'])
        self.assertEqual(self.t4.shortest_path_product(["M6"], "M3"),['R3_b', 'R2'])
       

if __name__ == '__main__':
    unittest.main()