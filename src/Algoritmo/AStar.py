#!/usr/bin/env python
# -*- coding: utf-8 -*-

class AStar(object):

    def __init__(self):
        self.__openNode = list()
        self.__closeNode = list()

    def distanceToFinal(self,posNow,posFinal):
        if (posNow != [] ):
            return abs(posFinal[0] - posNow[0]) + abs(posFinal[1] - posNow[1])

    def setOpenNode(self,Node):
        self.__openNode.append(Node)

    def openNode(self,Nodes):
        for i in Nodes:
            if (i != []):
                self.__openNode.append(i)

        print("final openNode:"+str(self.__openNode))

    def closeNode(self,Node):
        print(self.__openNode)
        print(self.__closeNode)
        self.__openNode.remove(Node)
        self.__closeNode.append(Node)
        print("--------------")
        print(self.__openNode)
        print(self.__closeNode)

    def bestNode(self,posFinal):
        distance_aux = self.distanceToFinal(self.__openNode[0],posFinal)
        node_aux = self.__openNode[0]
        openNode_aux = self.__openNode[:]
        openNode_aux.pop(0)
        for nodo in openNode_aux:
            if(distance_aux>self.distanceToFinal(nodo,posFinal)):
                distance_aux = self.distanceToFinal(nodo,posFinal)
                node_aux = nodo
        return node_aux



"""
    def bestNode(self):
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
        return nodoF"""
