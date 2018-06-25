#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Map import *
from Archivo.Archivo import *

class BeingMap(Map):

    def __init__(self, start):
        super(BeingMap, self).__init__()
        self.initMap()
        #shadow,inicial,Visitado,Decision,Actual
        self.matrix[start[0]][start[1]][1] = 'i'

    def getMatrix(self):
        return self.matrix

    def setTerrain(self, pos, terrain):
        print("->terrain->"+str(terrain)+"------->"+str(pos))
        if (int(terrain) >= 0 and pos != []):
            self.matrix[pos[0]][pos[1]][0] = terrain
        else: -2

    def getUpTerrain(self, pos):
        return self.matrix[pos[0]][pos[1]-1][0]

    def getDownTerrain(self, pos):
        return self.matrix[pos[0]][pos[1]+1][0]

    def getRightTerrain(self, pos):
        return self.matrix[pos[0]+1][pos[1]][0]

    def getLeftTerrain(self, pos):
        return self.matrix[pos[0]-1][pos[1]][0]

    def getUpPos(self,pos,typ):
        position = [pos[0], pos[1]-1]
        print("getUpPos->"+str(position))
        if(self.valMove(position,typ)):
            return position
        else:
            return []

    def getDownPos(self,pos,typ):
        position = [pos[0], pos[1]+1]
        print("getDownPos->"+str(position))
        if(self.valMove(position,typ)):
            return position
        else:
            return []

    def getLeftPos(self,pos,typ):
        position = [pos[0]-1, pos[1]]
        print("getLeftPos->"+str(position))
        if(self.valMove(position,typ)):
            return position
        else:
            return []

    def getRightPos(self,pos, typ):
        position = [pos[0]+1, pos[1]]
        print("getRightPos->"+str(position)+"/Terrain->"+str(self.getTerrain(position)))
        if(self.valMove(position,typ)):
            return position
        else:
            return []

    def getBesidePos(self,pos,typ):
        BesidePos = list()
        print("getBesidePosUp->"+str(self.valMove(pos,typ)))
        if (self.valMove(pos,typ)): BesidePos.append(self.getUpPos(pos,typ))
        else: BesidePos.append([])
        print("getBesideDownRight->"+str(self.valMove(pos,typ)))
        if (self.valMove(pos,typ)): BesidePos.append(self.getDownPos(pos,typ))
        else: BesidePos.append([])
        print("getBesideleftRight->"+str(self.valMove(pos,typ)))
        if (self.valMove(pos,typ)): BesidePos.append(self.getLeftPos(pos,typ))
        else: BesidePos.append([])
        print("getBesidePosRight->"+str(self.valMove(pos,typ)))
        if (self.valMove(pos,typ)): BesidePos.append(self.getRightPos(pos,typ))
        else: BesidePos.append([])
        print("BesidePos : {}".format(BesidePos))
        return BesidePos

    def setBesideTerrain(self,pos,terrain):
        print("Positions->"+str(pos))
        print("Terrains->"+str(terrain))
        self.setTerrain(pos[0],terrain[0])
        self.setTerrain(pos[1],terrain[1])
        self.setTerrain(pos[2],terrain[2])
        self.setTerrain(pos[3],terrain[3])

    def getBesideTerrain(self,pos):
        BesideTerrain = list()
        BesideTerrain.append(self.getUpTerrain(pos))
        BesideTerrain.append(self.getDownTerrain(pos))
        BesideTerrain.append(self.getLeftTerrain(pos ))
        BesideTerrain.append(self.getRightTerrain(pos))
        print("BesideTerrain : {}".format(BesideTerrain))
        return BesideTerrain

    def initMap(self):
        self.matrix = [[ [-1,0,0,0,0] for j in range(self.dimensions[0])] for i in range(self.dimensions[1])]


    def getTerrain(self, pos):
        print("getTerrainBeingMap->"+str(pos))
        if(pos != []):
            return self.matrix[pos[0]][pos[1]][0]
        else:
            return -2

    def valTerrain(self, pos, tipo):
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("------------------Validando Terreno--------------------------------")
        vals = self.beingInfo.get(tipo)
        print(vals)
        print(pos)
        terrain = int(self.matrix[pos[0]][pos[1]][0])
        print(terrain)
        print(str(vals[terrain])+"!= X:{}".format(vals[terrain] != 'X'))
        #print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        #print("Val Terrain : {}".format(vals[terrain] != 'X'))
        return (vals[terrain] != 'X')

    def valVisited(self, pos):
        print("------------------Validando Visitado--------------------------------")
        print("No Visitado: {}".format(not(self.getVisited(pos) == 'v')))
        return not(self.getVisited(pos) == 'v')

    def valDimesions(self, pos):
        print("------------------Validando Dimensiones--------------------------------")
        print(pos)
        print("pos[x] < dimensions en x : {}".format((int(pos[0])<int(self.dimensions[0]))))
        print("pos[y] < dimensions en y : {}".format((int(pos[1])<int(self.dimensions[1]))))
        print("pos[x] >= 0: {}".format((int(pos[0]))>=0))
        print("pos[y] >= 0: {}".format((int(pos[1]))>=0))
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        return((int(pos[0])<int(self.dimensions[0])) and (int(pos[1])<int(self.dimensions[1])) and (int(pos[0]))>=0 and (int(pos[1]))>=0)

    def valMove(self,pos,type):
        print("ValTerrain: {}".format(self.valTerrain(pos,type)))
        print("ValDimensions: {}".format(self.valDimesions(pos)))
        print("ValTerrain: {}".format(self.valVisited(pos)))
        return (self.valTerrain(pos,type) and (self.valVisited(pos)) and (self.valDimesions(pos)))

    def getVisited(self,pos):
        return self.matrix[pos[0]][pos[1]][2]

    def getDesition(self,pos):
        return self.matrix[pos[0]][pos[1]][3]

    def setDesition(self,pos):
        self.matrix[pos[0]][pos[1]][3] = 'd'

    def getNow(self,pos):
        return self.matrix[pos[0]][pos[1]][4]

    def setNow(self,pos):
        self.matrix[pos[0]][pos[1]][4] = 'a'

    def deleteNow(self,pos):
        self.matrix[pos[0]][pos[1]][4] = '0'
