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
        #print("Position: {}".format(position))
        #print("valMove: {}".format(self.valMove(position,typ)))
        #if(self.valMove(position,typ)):
        return position
        #else:
            #return []

    def getDownPos(self,pos,typ):
        position = [pos[0], pos[1]+1]
        #if(self.valMove(position,typ)):
        return position
        #else:
            #return []

    def getLeftPos(self,pos,typ):
        position = [pos[0]-1, pos[1]]
        #if(self.valMove(position,typ)):
        return position
        #else:
            #return []

    def getRightPos(self,pos, typ):
        position = [pos[0]+1, pos[1]]
        #if(self.valMove(position,typ)):
        return position
        #else:
            #return []

    def getBesidePos(self,pos,typ):#Aquimodificamos
        BesidePos = list()
        print("entre ∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫")
        print("getUpPos: {}".format(self.getUpPos(pos,typ)))
        print("getDownPos: {}".format(self.getDownPos(pos,typ)))
        print("getRightPos: {}".format(self.getRightPos(pos,typ)))
        print("getLeftPos: {}".format(self.getLeftPos(pos,typ)))
        #print(self.valMove(self.getUpPos(pos,typ),typ))
        #print(self.valMove(self.getDownPos(pos,typ),typ))
        #print(self.valMove(self.getLeftPos(pos,typ),typ))
        #print(self.valMove(self.getRightPos(pos,typ),typ))
        if (self.valMove(self.getUpPos(pos,typ),typ)): BesidePos.append(self.getUpPos(pos,typ))
        else: BesidePos.append([])
        if (self.valMove(self.getDownPos(pos,typ),typ)): BesidePos.append(self.getDownPos(pos,typ))
        else: BesidePos.append([])
        if (self.valMove(self.getLeftPos(pos,typ),typ)): BesidePos.append(self.getLeftPos(pos,typ))
        else: BesidePos.append([])
        if (self.valMove(self.getRightPos(pos,typ),typ)): BesidePos.append(self.getRightPos(pos,typ))
        else: BesidePos.append([])
        print("BesidePos : {}".format(BesidePos))
        return BesidePos

    def setBesideTerrain(self,pos,terrain):
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
        #print("BesideTerrain : {}".format(BesideTerrain))
        return BesideTerrain

    def initMap(self):
        self.matrix = [[ [-1,0,0,0,0] for j in range(self.dimensions[0])] for i in range(self.dimensions[1])]


    def getTerrain(self, pos):
        if(pos != []):
            return self.matrix[pos[0]][pos[1]][0]
        else:
            return -2

    def valTerrain(self, pos, tipo):
        #print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("------------------Validando Terreno--------------------------------")
        vals = self.beingInfo.get(tipo)
        #print(vals)
        print("pos en valTerrain: {}".format(pos))
        terrain = int(self.matrix[pos[0]][pos[1]][0])
        print(terrain)
        #print(str(vals[terrain])+"!= X:{}".format(vals[terrain] != 'X'))
        #print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        #print("Val Terrain : {}".format(vals[terrain] != 'X'))
        return (vals[terrain] != 'X')

    def valVisited(self, pos): ####Funcionando no tocar
        #print("------------------Validando Visitado--------------------------------")
        #print("position:"+str(pos)+" No Visitado: {}".format(not(self.getVisited(pos) == 'v')))
        return not(self.getVisited(pos) == 'v')

    def valDimesions(self, pos): ####Funcionando no tocar
        #print("------------------Validando Dimensiones--------------------------------")
        #print(pos)
        #print("pos[x] < dimensions en x : {}".format((int(pos[0])<int(self.dimensions[0]))))
        #print("pos[y] < dimensions en y : {}".format((int(pos[1])<int(self.dimensions[1]))))
        #print("pos[x] >= 0: {}".format((int(pos[0]))>=0))
        #print("pos[y] >= 0: {}".format((int(pos[1]))>=0))
        return((int(pos[0])<int(self.dimensions[0])) and (int(pos[1])<int(self.dimensions[1])) and (int(pos[0]))>=0 and (int(pos[1]))>=0)

    def valMove(self,pos,type):
        #print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("Recibo la {} pos para validar: ".format(pos))
        #print("La pos {} esta dentro de la dimensions de la ventana: {}".format(pos,self.valDimesions(pos)))
        if(self.valDimesions(pos)):
            #print("la posicion es valida")
            return (self.valTerrain(pos,type) and (self.valVisited(pos)))
        else:
            return False

    def getVisited(self,pos):
        return self.matrix[pos[0]][pos[1]][2]

    def setVisited(self,pos):
        self.matrix[pos[0]][pos[1]][2] = 'v'

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
