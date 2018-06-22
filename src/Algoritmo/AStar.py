#!/usr/bin/env python
# -*- coding: utf-8 -*-

class AStar(object):

    def __init__(self):
        self.__openNode = list()
        self.__closeNode = list()

    def DistanceToFinal(self,posNow,posFinal):
        return abs(posFinal[0] - posNow[0]) + abs(posFinal[1] - posNow[1])

    def openNode(self,Nodes):
        for i in Nodes:
            self.__openNode.append(i)

    def closeNode(self,Node):
        self.__openNode.remove(Node)
        self.__closeNode.append(Node)


    def BestNode(self):
        nodoF = self.__openNode[0]
        min = int(str(nodoF).split("/")[-1].split(",")[-1].split("'")[0])
        for nodo in self.__openNode:
            actual = int(str(nodo).split("/")[-1].split(",")[-1].split("'")[0])
            if(actual == min):
                XA = int(str(nodo).split("->")[-1].split(",")[0])
                YA = int(str(nodo).split("->")[-1].split(",")[1].split("'")[0])
                dA = YA - XA
                XF = int(str(nodoF).split("->")[-1].split(",")[0])
                YF = int(str(nodoF).split("->")[-1].split(",")[1].split("'")[0])
                dF = YF - XF
                if(dA == dF):
                    pass
                elif(dA < dF):
                    nodoF = nodo
            elif(actual < min):
                nodoF = nodo
                min = actual
        return nodoF
