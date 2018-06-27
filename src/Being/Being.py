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
        self.raiz = Node(str(self.__pos[0]) + "," + str(self.__pos[1]))
        self.__padre = self.raiz
        self.star.setOpenNode(self.getNodeFormat(self.__pos,0))
        self.star.setPosFinal(self.__final)
        self.filename = str(self.__pos[0]) + str(self.__pos[1]) + "_" + str(self.__final[0]) + str(self.__final[1]) + ".txt"
        print(self.filename)
        self.file = open(self.filename, "w")

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

    def getNodeFormat(self,pos,cost):
        auxF = list()
        auxF.append(pos[0])
        auxF.append(pos[1])
        auxF.append(cost)
        #print("Format->>"+str(auxF))
        return auxF

    def setPos(self,pos,beside):

        #self.view.setVisited(self.__pos)
        print("setPos-> pos"+str(pos)+" / beside"+str(beside)+"/ me puedo mover"+str(self.view.valMove(pos,self.__type)))
        if(self.view.valMove(pos,self.__type)):
            self.view.setVisited(self.__pos)
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
        return (view.valMove(self.__pos[1]-1, self.__type))

    def askDOWN(self, map, flag):
        return (view.valMove(self.__pos[1]+1, self.__type))

    def askRIGHT(self, map, flag):
        return (view.valMove(self.__pos[0]+1, self.__type))

    def askLEFT(self, map, flag):
        return (view.valMove(self.__pos[0]-1, self.__type))

    def terrainCost(self, pos):
        vals = self.__beingInfo.get(self.getType())
        for i in range(len(vals)):
            if int(self.view.getTerrain(pos)) == i:
                return int(vals[i])
        return 0

    def openNode(self,nodes,cost):
        auxNode =list()
        nodes_aux = nodes[:]
        for i in range(len(nodes)):
            #print(self.view.getTerrain(nodes[i]))
            if(self.view.getTerrain(nodes[i]) != -2):
                nodes[i].append(cost[i])

        self.star.openNode(nodes)
        for i in nodes_aux:
            if (i != []):
                Node(str(i[0]) + "," + str(i[1]), parent=self.__padre)

    def closeNode(self,node):
        self.star.closeNode(node)

    def getCostBeside(self,pos):
        BesideCost = list()
        BesideCost.append(self.costT+(int(self.terrainCost(pos[0]))))
        BesideCost.append(self.costT+(int(self.terrainCost(pos[1]))))
        BesideCost.append(self.costT+(int(self.terrainCost(pos[2]))))
        BesideCost.append(self.costT+(int(self.terrainCost(pos[3]))))
        print("CostosBeside->"+str(BesideCost))
        return BesideCost

    def move(self,beside): #window nos  manda beside
        #nodeToClose = list()
        print("∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫Inicio Move∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫")
        self.view.setNow(self.__pos)
        self.view.setBesideTerrain(self.__pos,beside)
        nodes = self.view.getBesidePos(self.__pos,self.__type)
        self.openNode(nodes, self.getCostBeside(nodes))
        self.closeNode(self.getNodeFormat(self.__pos,self.costT))
        best = self.star.bestNode(self.__final)
        print("El mejor nodo: {}".format(best))
        #print ("TerrainCost: {}".format(self.terrainCost(best)))
        self.setPos(best[:2],beside)
        #self.costT = self.costT + int(self.terrainCost(best[2]))
        #print("before--Mi Costo->"+str(self.costT))
        self.costT = best[2]
        #print("after--Mi Costo->"+str(self.costT))
        assignNode = (str(best[0]) + "," +str(best[1]))
        #print(assignNode)
        self.__padre = Node(assignNode, parent = self.__padre)
        self.view.deleteNow(self.__pos)

    def finished(self):
        if (self.__pos == self.__final):
            return self.costT
        else:
            return False

    def getFile(self):
        return self.filename
