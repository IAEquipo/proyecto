#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Map import *

class BeingMap(Map):

    def __init__(self):
        super(BeingMap, self).__init__()
        self.initMap()

    def getMatrix(self):
        return self.matrix

    def setUp(self, pos, terrain):
        self.matrix[pos[0]][pos[1]-1][0] = terrain

    def setDown(self, pos, terrain):
        self.matrix[pos[0]][pos[1]+1][0] = terrain

    def setRight(self, pos, terrain):
        self.matrix[pos[0]+1][pos[1]][0] = terrain

    def setLeft(self, pos, terrain):
        self.matrix[pos[0]-1][pos[1]][0] = terrain

    def initMap(self):
        self.matrix = [[ [-1,0,0,0,0] for j in range(self.dimensions[0])] for i in range(self.dimensions[1])]

    def getTerrain(self, pos):
        return self.matrix[pos[0]][pos[1]]

    def valTerrain(self, pos, tipo):
        vals = self.beingInfo.get(tipo)
        terrain = int(self.matrix[pos[0]][pos[1]][0])
        return (vals[terrain] != 'X')
