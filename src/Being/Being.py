#!/usr/bin/env python
# -*- coding: utf-8 -*-
from anytree import Node, RenderTree
from anytree.search import *
from anytree.exporter import DotExporter

from Map.BeingMap import *
from Archivo.Archivo import *
from Algoritmo.AStar import *


class Being(object):

    costT = 0

    def __init__(self, tipo, start, final):
        self.__type = tipo
        self.__pos = start
        self.__final = final
        self.view = BeingMap()
        file = Archivo()
        star = AStar()
        self.__beingInfo = {}
        self.__being_values = file.read_being('beings.txt')
        for line in self.__being_values:
            self.__beingInfo[line[0]] = line[1:]
        raiz = Node(str(self.__pos[0]) + "," + str(self.__pos[1]) + "->0," + str(star.DistanceToFinal(self.__pos,self.__final)))
        self.__padre = raiz

    @property
    def getParent(self):
        return self.__padre
        
    @property
    def getType(self):
        return self.__type

    @property
    def getPos(self):
        return self.__pos

    @property
    def getBeingValues(self):
        return self.__beingInfo

    def setPos(self,pos,beside,Node):
        if(view.valTerrain(pos,self.__type)):
            self.__pos = pos
            view.setUp(self.__pos,beside[0])
            view.setDown(self.__pos,beside[1])
            view.setLeft(self.__pos,beside[2])
            view.setRight(self.__pos,beside[3])
            self.costT = self.costT + self.terrainCost()
            self.__padre = Node
        else:
            return False

    @property
    def getFinal(self):
        return self.__final

    def setFinal(self,pos):
        self.__pos = pos

    @property
    def getCost(self):
        return self.costT

    def setCost(self,pos):
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

    def terrainCost(self):
        vals = self.__beingInfo.get(self.getType)
        for i in range(len(vals)):
            if int(self.view.getTerrain(self.__pos)[0]) == i :
                return int(vals[i])

    def openNode(self,Parent,nodes):
        self.star.openNode(nodes)
        for i in Nodes:
            Node(str(i[0]) + "," + str(i[1]) + "->" + str(self.CostT) + "," + str(self.star.DistanceToFinal(i,self.__final), parent=Parent))

    def closeNode(self,Node):
        self.star.closeNode(Node)
