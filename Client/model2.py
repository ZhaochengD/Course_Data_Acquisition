#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 20:34:48 2019

@author: zhaocheng_du
"""

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node(0,pos=(0+17.5,0+75), has_car=0, is_park=1)
G.add_node(0.5,pos=(0+17.5,30+75), has_car=0, is_park=0)
G.add_node(1,pos=(17.5+17.5,30+75), has_car=0, is_park=0)
G.add_node(2,pos=(35+17.5,30+75), has_car=0, is_park=0)
G.add_node(3,pos=(35+17.5,0+75), has_car=0, is_park=1)
G.add_node(4,pos=(70+17.5,30+75), has_car=0, is_park=0)
G.add_node(5,pos=(70+17.5,0+75), has_car=0, is_park=1)
G.add_node(6,pos=(105+17.5,30+75), has_car=0, is_park=0)
G.add_node(7,pos=(105+17.5,0+75), has_car=0, is_park=1)
G.add_node(8,pos=(140+17.5,30+75), has_car=0, is_park=0)
G.add_node(9,pos=(140+17.5,0+75), has_car=0, is_park=1)
G.add_node(10,pos=(175+17.5,30+75), has_car=0, is_park=0)
G.add_node(11,pos=(175+17.5,0+75), has_car=0, is_park=1)
G.add_node(12,pos=(210+17.5,30+75), has_car=0, is_park=0)
G.add_node(13,pos=(210+17.5,0+75), has_car=0, is_park=1)
G.add_node(14,pos=(227.5+17.5,30+75), has_car=0, is_park=0)
G.add_node(15,pos=(245+17.5,30+75), has_car=0, is_park=0)
G.add_node(16,pos=(245+17.5,0+75), has_car=0, is_park=1)
G.add_node(17,pos=(0+17.5,195+75), has_car=0, is_park=1)
G.add_node(18,pos=(0+17.5,165+75), has_car=0, is_park=0)
G.add_node(19,pos=(17.5+17.5,165+75), has_car=0, is_park=0)
G.add_node(20,pos=(35+17.5,165+75), has_car=0, is_park=0)
G.add_node(21,pos=(35+17.5,195+75), has_car=0, is_park=1)
G.add_node(22,pos=(70+17.5,165+75), has_car=0, is_park=0)
G.add_node(23,pos=(70+17.5,135+75), has_car=0, is_park=1)
G.add_node(24,pos=(87.5+17.5,165+75), has_car=0, is_park=0)
G.add_node(25,pos=(87.5+17.5,270+75), has_car=0, is_park=0)
G.add_node(25.5,pos=(105+17.5,165+75), has_car=0, is_park=0)
G.add_node(26,pos=(105+17.5,135+75), has_car=0, is_park=1)
G.add_node(27,pos=(140+17.5,135+75), has_car=0, is_park=1)
G.add_node(28,pos=(140+17.5,165+75), has_car=0, is_park=0)
G.add_node(29,pos=(157.5+17.5,270+75), has_car=0, is_park=0)
G.add_node(29.5,pos=(157.5+17.5,165+75), has_car=0, is_park=0)
G.add_node(30,pos=(175+17.5,165+75), has_car=0, is_park=0)
G.add_node(31,pos=(175+17.5,135+75), has_car=0, is_park=1)
G.add_node(32,pos=(210+17.5,165+75), has_car=0, is_park=0)
G.add_node(33,pos=(210+17.5,195+75), has_car=0, is_park=1)
G.add_node(34,pos=(227.5+17.5,165+75), has_car=0, is_park=0)
G.add_node(35,pos=(245+17.5,165+75), has_car=0, is_park=0)
G.add_node(36,pos=(245+17.5,195+75), has_car=0, is_park=1)

G.add_edges_from([(0,0.5), (0.5,1), (1,2), (2,3), 
                           (2,4), (4,5), (4,6), (6,7), (6,8),
                           (8,9), (8,10), (10,11), (10,12), (12,13),
                           (12,14), (14,15), (15,16), (17,18), (18,19),
                           (19,20), (20,21), (20,22), (22,23), (22,24),
                           (24,25), (24,25.5), (25.5,26), (27,28), (28,29.5),
                           (29.5, 29), (29.5,30), (30,31), (30,32), (32,33),
                           (32,34), (34,35), (35,36), (1,19), (14,34), (25.5,28)])
im = plt.imread("background.png")

#plt.figure(figsize=(280, 345))
#nx.draw(G)
pos=nx.get_node_attributes(G,'pos')
ec = nx.draw_networkx_edges(G, pos, alpha=0.2)
nc = nx.draw_networkx_nodes(G, pos, nodelist=G.nodes(), 
                            node_color=['blue' if G.node[i]['is_park']==0 else 'blue' for i in G.nodes()], 
                            node_size=20)

plt.imshow(im, extent=[0, 280, 0, 345], alpha=0)
#nx.write_gpickle(G,"test.gpickle")