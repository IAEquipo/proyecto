#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Archivo.Archivo import *

class Map(object):

    def __init__(self):
        file = Archivo()
        self.__dimensions = list()
        self.__matrix = file.read('lab2.txt')
        self.__dimensions.append(len(self.__matrix))
        self.__dimensions.append(len(self.__matrix[0]))
        self.__beingInfo = {}
        file = Archivo()
        being_info = file.read('beings.txt')
        for line in being_info:
            self.__beingInfo[line[0]] = line[1:]
        #self.__darkside = [[-1 for j in range(self.__dimensions[0])] for i in range(self.__dimensions[1])]

    @property
    def getDimensions(self):
        return self.__dimensions

    @property
    def getMatrix(self):
        return self.__matrix

    @property
    def getDarkSide(self):
        return self.__darkside

    def getUp(self, pos):
        return self.__matrix[pos[0]][pos[1]-1]

    def getDown(self, pos):
        return self.__matrix[pos[0]][pos[1]+1]

    def getRight(self, pos):
        return self.__matrix[pos[0]+1][pos[1]]

    def getLeft(self, pos):
        return self.__matrix[pos[0]-1][pos[1]]

    def valTerrain(self, pos, tipo):
        vals = self.__beingInfo.get(tipo)
        terrain = int(self.__matrix[pos[0]][pos[1]])
        return (vals[terrain] != 'X')
