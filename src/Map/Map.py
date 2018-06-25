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
        #print(self.beingInfo)

    @property
    def getDimensions(self):
        return self.dimensions

    def getMatrix(self):
        return self.matrix

    def getBesideTerrain(self,pos,type):
        beside = []
        beside.append(self.getUpTerrain(pos,type))
        beside.append(self.getDownTerrain(pos,type))
        beside.append(self.getLeftTerrain(pos,type))
        beside.append(self.getRightTerrain(pos,type))
        return beside

    @property
    def getDarkSide(self):
        return self.__darkside

    def getUpTerrain(self, pos, type):
        pos_aux = list()
        pos_aux.append(pos[0])
        pos_aux.append(pos[1]-1)
        print("posaux:"+str(pos_aux))
        if(self.valTerrain(pos_aux,type)):
            print("getUpTerrainMap->"+str(self.matrix[pos[0]][pos[1]-1]))
            return self.matrix[pos[0]][pos[1]-1]
        else:
            return -2

    def getDownTerrain(self, pos, type):
        pos_aux = list()
        pos_aux.append(pos[0])
        pos_aux.append(pos[1]+1)
        print("posaux:"+str(pos_aux))
        if(self.valTerrain(pos_aux,type)):
            print("getDownTerrainMap->"+str(self.matrix[pos[0]][pos[1]-1]))
            return self.matrix[pos[0]][pos[1]+1]
        else:
            return -2

    def getRightTerrain(self, pos, type):
        pos_aux = list()
        pos_aux.append(pos[0]+1)
        pos_aux.append(pos[1])
        print("posaux:"+str(pos_aux))
        if(self.valTerrain(pos_aux,type)):
            print("getRightTerrainMap->"+str(self.matrix[pos[0]][pos[1]-1]))
            return self.matrix[pos[0]+1][pos[1]]
        else:
            return -2

    def getLeftTerrain(self, pos, type):
        pos_aux = list()
        pos_aux.append(pos[0]-1)
        pos_aux.append(pos[1])
        print("posaux:"+str(pos_aux))
        if(self.valTerrain(pos_aux,type)):
            print("getLeftTerrainMap->"+str(self.matrix[pos[0]][pos[1]-1]))
            return self.matrix[pos[0]-1][pos[1]]
        else:
            return -2

    def valTerrain(self, pos, tipo):
        vals = self.beingInfo.get(tipo)
        if((int(pos[0])<int(self.dimensions[0])) and (int(pos[1])<int(self.dimensions[1])) and (int(pos[0]))>=0 and (int(pos[1]))>=0):
            terrain = int(self.matrix[pos[0]][pos[1]])
            return (vals[terrain] != 'X')
