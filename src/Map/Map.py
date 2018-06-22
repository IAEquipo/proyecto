#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Archivo.Archivo import *

class Map(object):

    def __init__(self):
        file = Archivo()
        self.dimensions = list()
        self.matrix = file.read('lab2.txt')
        self.dimensions.append(len(self.matrix))
        self.dimensions.append(len(self.matrix[0]))
        self.beingInfo = {}
        file = Archivo()
        being_info = file.read_being('beings.txt')
        for line in being_info:
            self.beingInfo[line[0]] = line[1:]
        #self.__darkside = [[-1 for j in range(self.dimensions[0])] for i in range(self.dimensions[1])]

    @property
    def getDimensions(self):
        return self.dimensions

    @property
    def getMatrix(self):
        return self.matrix

    def getBeside(self):
        beside = []
        beside.append(self.getUp)
        beside.append(self.getDown)
        beside.append(self.getLeft)
        beside.append(self.getRight)
        return beside

    @property
    def getDarkSide(self):
        return self.__darkside

    def getUp(self, pos):
        return self.matrix[pos[0]][pos[1]-1]

    def getDown(self, pos):
        return self.matrix[pos[0]][pos[1]+1]

    def getRight(self, pos):
        return self.matrix[pos[0]+1][pos[1]]

    def getLeft(self, pos):
        return self.matrix[pos[0]-1][pos[1]]

    def valTerrain(self, pos, tipo):
        vals = self.beingInfo.get(tipo)
        terrain = int(self.matrix[pos[0]][pos[1]])
        return (vals[terrain] != 'X')
