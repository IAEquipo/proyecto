#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Map.BeingMap import *
from Archivo.Archivo import *

class Being(object):

    costT = 0

    def __init__(self, tipo, start, final):
        self.__type = tipo
        self.__pos = start
        self.__final = final
        view = BeingMap()
        file = Archivo()
        self.__being_values = file.read('beings.txt')
        for line in being_info:
            self.__beingInfo[line[0]] = line[1:]
        #personaje,montaña,tierra,agua,arena,bosque, pantano,nieve

    @property
    def getPos(self):
        return self.__pos

    def setPos(self,pos,beside):
        if(view.valTerrain(pos,self.__type)):
            self.__pos = pos
            view.setUp(self.__pos,beside[0])
            view.setDown(self.__pos,beside[0])
            view.setRight(self.__pos,beside[0])
            view.setUp(self.__pos,beside[0])
            self.costT = self.costT + self.terrainCost()
        else:
            return False

    @property
    def getFinal(self):
        return self.__final

    def setFinal(self,pos):
        self.__pos = pos

    @property
    def getcost(self):
        return self.costT

    def setcost(self,pos):
        self.costT = int(valor)

    def move(self):
        pass

    def askUP(self):
        return (view.valTerrain(self.__pos[1]-1, self.__type))

    def askDOWN(self, map, flag):
        return (view.valTerrain(self.__pos[1]+1, self.__type))

    def askRIGHT(self, map, flag):
        return (view.valTerrain(self.__pos[0]+1, self.__type))

    def askLEFT(self, map, flag):
        return (view.valTerrain(self.__pos[0]-1, self.__type))

    def terrainCost():
        vals = self.__beingInfo.get(tipo)
        for i in range(len(vals)):
            if valTerrain(self,self.__pos, self.__type):
                if int(view.getTerrain(self.__pos)) == i :
                    return int(vals[i])
