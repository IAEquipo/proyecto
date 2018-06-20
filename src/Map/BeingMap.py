#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Map import *

class BeingMap(Map):

    def __init__(self):
        super(Map, self).__init__()
        self.initMap()

    @property
    def getBeside(self):
        beside = []
        beside.append(self.getUp)
        beside.append(self.getDown)
        beside.append(self.getLeft)
        beside.append(self.getRight)
        return beside

    def setUp(self, pos, terrain):
        self.__matrix[pos[0]][pos[1]-1] = terrain

    def setDown(self, pos, terrain):
        self.__matrix[pos[0]][pos[1]+1] = terrain

    def setRight(self, pos, terrain):
        self.__matrix[pos[0]+1][pos[1]] = terrain

    def setLeft(self, pos, terrain):
        self.__matrix[pos[0]-1][pos[1]] = terrain

    def initMap(self):
        self.__matrix = [[ [-1,0,0,0,0] for j in range(self.__dimensions[0])] for i in range(self.__dimensions[1])]

    def getTerrain(self, pos):
        return self.__matrix[pos[0]][pos[1]]
