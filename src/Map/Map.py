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
        posUP = list()
        posUP.append(pos[0])
        posUP.append(pos[1]-1)
        print("posUp->>>"+str(posUP)+","+str(self.valTerrain(posUP,type)))
        if(self.valTerrain(posUP,type)):
            print("getUpTerrainMap->"+str(self.matrix[posUP[0]][posUP[1]]))
            return self.matrix[posUP[0]][posUP[1]]
        else:
            return -2

    def getDownTerrain(self, pos, type):
        posDOWN = list()
        posDOWN.append(pos[0])
        posDOWN.append(pos[1]+1)
        print("posauxDown->>>"+str(posDOWN)+","+str(self.valTerrain(posDOWN,type)))
        if(self.valTerrain(posDOWN,type)):
            print("getDownTerrainMap->"+str(self.matrix[posDOWN[0]][posDOWN[1]]))
            return self.matrix[posDOWN[0]][posDOWN[1]]
        else:
            return -2

    def getRightTerrain(self, pos, type):
        posRIGHT = list()
        posRIGHT.append(pos[0]+1)
        posRIGHT.append(pos[1])
        print("posauxRight->>>"+str(posRIGHT)+","+str(self.valTerrain(posRIGHT,type)))
        if(self.valTerrain(posRIGHT,type)):
            print("getRightTerrainMap->"+str(self.matrix[posRIGHT[0]][posRIGHT[1]]))
            return self.matrix[posRIGHT[0]][posRIGHT[1]]
        else:
            return -2

    def getLeftTerrain(self, pos, type):
        posLEFT = list()
        posLEFT.append(pos[0]-1)
        posLEFT.append(pos[1])
        print("posauxLeft->>>"+str(posLEFT)+","+str(self.valTerrain(posLEFT,type)))
        if(self.valTerrain(posLEFT,type)):
            print("getLeftTerrainMap->"+str(self.matrix[posLEFT[0]][posLEFT[1]]))
            return self.matrix[posLEFT[0]][posLEFT[1]]
        else:
            return -2

    def valTerrain(self, pos, type):
        vals = self.beingInfo.get(type)
        if((int(pos[0])<int(self.dimensions[0])) and (int(pos[1])<int(self.dimensions[1])) and (int(pos[0]))>=0 and (int(pos[1]))>=0):
            terrain = int(self.matrix[pos[0]][pos[1]])
            return (vals[terrain] != 'X')
