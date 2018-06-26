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
        self.beingInfo = dict()
        file = Archivo()
        being_info = file.read_being('beings.txt')
        for line in being_info:
            self.beingInfo[line[0]] = line[1:]
        #self.__darkside = [[-1 for j in range(self.dimensions[0])] for i in range(self.dimensions[1])]

    @property
    def getDimensions(self):
        return self.dimensions

    def getMatrix(self):
        return self.matrix

    def getBesideTerrain(self,pos,type):
        print("entré a getBesideTerrain")
        beside = []
        beside.append(self.getUpTerrain(pos))
        beside.append(self.getDownTerrain(pos))
        beside.append(self.getLeftTerrain(pos))
        beside.append(self.getRightTerrain(pos))
        print("Estoy en la posicion {} y los valores de mis lados".format(pos))
        print("Estoy desde getBesideTerrain: {}".format(beside))
        return beside

    @property
    def getDarkSide(self):
        return self.__darkside

    def getUpTerrain(self, pos):
        print(pos)
        posUP = list()
        posUP.append(pos[0])
        posUP.append(pos[1]-1)
        print("UP: {}".format(posUP))
        if(self.valDimensions(posUP)):
            return self.matrix[posUP[0]][posUP[1]]
        else:
            return -2

    def getDownTerrain(self, pos):
        print(pos)
        posDOWN = list()
        posDOWN.append(pos[0])
        posDOWN.append(pos[1]+1)
        print("DOWN: {}".format(posDOWN))
        if(self.valDimensions(posDOWN)):
            return self.matrix[posDOWN[0]][posDOWN[1]]
        else:
            return -2

    def getRightTerrain(self, pos):
        print(pos)
        posRIGHT = list()
        posRIGHT.append(pos[0]+1)
        posRIGHT.append(pos[1])
        print("RIGHT: {}".format(posRIGHT))
        if(self.valDimensions(posRIGHT)):
            return self.matrix[posRIGHT[0]][posRIGHT[1]]
        else:
            return -2

    def getLeftTerrain(self, pos):
        print(pos)
        posLEFT = list()
        posLEFT.append(pos[0]-1)
        posLEFT.append(pos[1])
        print("LEFT: {}".format(posLEFT))
        if(self.valDimensions(posLEFT)):
            return self.matrix[posLEFT[0]][posLEFT[1]]
        else:
            return -2

    def valDimensions(self, pos):
        return ((int(pos[0])<int(self.dimensions[0])) and (int(pos[1])<int(self.dimensions[1])) and (int(pos[0]))>=0 and (int(pos[1]))>=0)

    def valTerrain(self, pos, type):
        vals = self.beingInfo.get(type)
        terrain = int(self.matrix[pos[0]][pos[1]])
        print("valido que el terreno de los lados en map, se pueda accesar para {} y esto es {} para la {}: ".format(type, vals[terrain] != 'X',pos))
        return (vals[terrain] != 'X')
