#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 20:50:42 2019

@author: zhaocheng_du
"""

import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
import time

im = plt.imread("background.png")
G = nx.read_gpickle("test.gpickle")

class Planner():
    def __init__(self, G, img):
        self.G   = G
        self.img = img
    
    def set_empty(self, parking_idx):
        if type(parking_idx) == list:
            for i in parking_idx:
                self.G.node[i]['has_car'] = 0
        else:
            self.G.node[parking_idx]['has_car'] = 0
        
    def set_taken(self, parking_idx):
        if type(parking_idx) == list:
            for i in parking_idx:
                self.G.node[i]['has_car'] = 1
        else:
            self.G.node[parking_idx]['has_car'] = 1
        
    def get_state(self, parking_idx):
        try:
            return self.G.node[parking_idx]['has_car']
        except:
            return "stop"

    def find_nearest(self):
        candidate, dis = [], []
        for i in self.G.nodes():
            if self.G.node[i]['has_car'] == 0 and self.G.node[i]['is_park'] == 1:
                candidate.append(i)
                dis.append(nx.shortest_path_length(self.G, source=25, target=i))
        if not dis:
            return 99
        return candidate[dis.index(min(dis))]
        
    def model_plot(self):
        pos=nx.get_node_attributes(self.G,'pos')
        nx.draw_networkx_edges(self.G, pos, alpha=0.01)
        nx.draw_networkx_nodes(self.G, pos, nodelist=G.nodes(), 
                            node_color=['blue' if self.G.node[i]['has_car']==0 else 'orange' for i in G.nodes()], 
                            node_size=[20 * (self.G.node[i]['has_car'] + 1) * (self.G.node[i]['is_park']) for i in self.G.nodes()], 
                            alpha=0.5, with_labels = True)
        plt.imshow(self.img, extent=[0, 280, 0, 345], alpha=0.7)

    def route_plan(self, D):
        try:
            pos_list = nx.shortest_path(self.G, source=25, target=D)
            x_li, y_li = [], []
    
            for i in pos_list:
                x_li.append(self.G.node[i]['pos'][0])
                y_li.append(self.G.node[i]['pos'][1])
                self.model_plot()
            plt.plot(x_li, y_li, '--')
            plt.arrow(87.5+17.5, 270+75, 0, -90, shape='full', 
                      lw=0.01, length_includes_head=False, head_width=7)
            plt.scatter(x_li[-1], y_li[-1], marker='*')
        except:
            self.model_plot()

    
    def target(self):
        '''
        When detect a car come
        use this function do the planning.
        '''
        D = self.find_nearest()
        self.route_plan(D)
    
    def update(self):
        self.target()    
    
if __name__ == "__main__":
    Planner = Planner(G, im)
    Planner.set_taken([26, 23, 21, 26, 27])
    Planner.target()
    plt.pause(5)
    plt.clf()
    #plt.close()
    Planner.set_taken(17)
    Planner.target()
    #i = 0
