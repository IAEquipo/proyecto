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
        self.view = BeingMap(self.__pos)
        file = Archivo()
        self.star = AStar()
        self.__beingInfo = {}
        self.__being_values = file.read_being('beings.txt')
        for line in self.__being_values:
            self.__beingInfo[line[0]] = line[1:]
        self.raiz = Node(str(self.__pos[0]) + "," + str(self.__pos[1]) + "->0," + str(self.star.distanceToFinal(self.__pos,self.__final)))
        self.__padre = self.raiz
        self.star.setOpenNode(self.__pos)

    @property
    def getParent(self):
        return self.__padre

    def getType(self):
        return self.__type

    def getPos(self):
        return self.__pos

    @property
    def getBeingValues(self):
        return self.__beingInfo


    def setPos(self,pos,beside):
        if(self.view.valTerrain(pos,self.__type)):
            self.__pos = pos
        else:
            return False

    def getFinal(self):
        return self.__final

    def setFinal(self,pos):
        self.__pos = pos

    def getCost(self):
        return self.costT

    def setCost(self,pos):
        self.costT = int(valor)

    def askUP(self):
        return (view.valTerrain(self.__pos[1]-1, self.__type))

    def askDOWN(self, map, flag):
        return (view.valTerrain(self.__pos[1]+1, self.__type))

    def askRIGHT(self, map, flag):
        return (view.valTerrain(self.__pos[0]+1, self.__type))

    def askLEFT(self, map, flag):
        return (view.valTerrain(self.__pos[0]-1, self.__type))

    def terrainCost(self, pos):
        print("TerrainCostPos->"+str(pos))
        vals = self.__beingInfo.get(self.getType())
        print("valsXVaños->"+str(vals))
        for i in range(len(vals)):
            if int(self.view.getTerrain(pos)) == i:
                return int(vals[i])

    def openNode(self,nodes):
        nodes_aux = list()
        for i in nodes:
            print(i)
            print(self.view.getTerrain(i))
            if(self.view.getTerrain(i) != -2):
                nodes_aux.append(i)


        self.star.openNode(nodes_aux)
        for i in nodes:
            if (i != []):
                Node(str(i[0]) + "," + str(i[1]) + "->" + str(self.getCost) + "," + str(self.star.distanceToFinal(i,self.__final)), parent=self.__padre)

    def closeNode(self,node):
        self.star.closeNode(node)

    def move(self,beside): #window nos  manda beside
        self.view.setNow(self.__pos)
        self.view.setBesideTerrain(self.view.getBesidePos(self.__pos,self.__type),beside)
        self.openNode(self.view.getBesidePos(self.__pos,self.__type))
        print("->>"+str(self.view.getBesidePos(self.__pos,self.__type)))
        self.closeNode(self.__pos)
        best = self.star.bestNode(self.__final)
        print("El mejor nodo: {}".format(best))
        print("nose que poner aqui->"+str(self.view.getBesideTerrain(self.__pos)))
        print ("TerrainCost: {}".format(self.terrainCost(best)))
        self.setPos(best,beside)
        self.costT = self.costT + int(self.terrainCost(best))
        assignNode = (str(best[0]) + "," +str(best[1]) + "->" + str(self.costT) + ',' + str(self.star.distanceToFinal(best,self.__final)))
        print(assignNode)
        self.__padre = Node(assignNode, parent = self.__padre)
        self.view.deleteNow(self.__pos)
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

    def finished(self):
        if (self.__pos == self.__final):
            return True
        else:
            return False
