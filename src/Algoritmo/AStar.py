#!/usr/bin/env python
# -*- coding: utf-8 -*-

class AStar(object):

    def __init__(self):
        self.__openNode = list()
        self.__closeNode = list()
        self.__posFinal = list()

    def distanceToFinal(self,posNow,posFinal):
        if (posNow != [] ):
            return abs(posFinal[0] - posNow[0]) + abs(posFinal[1] - posNow[1])

    def setOpenNode(self,Node):
        self.__openNode.append(Node)

    def setPosFinal(self, final):
        self.__posFinal = final

    def valOpenNode(self, Node):
        for nodo in self.__openNode:
            if Node[:2] == nodo[:2]:
                print("{} == {}".format(Node[:2], nodo[:2]))
                return True
            else: False

    def regresaNode(self, Node):
        for nodo in self.__openNode:
            if Node[:2] == nodo[:2]:
                return nodo

    def replaceNode(self, NodeA, NodeB):
        new = self.bestValNode(NodeA, NodeB) #Tenemos duda aqu ahorita regresamos
        print("El mejor de {} y {} es {}".format(NodeA, NodeB, new))
        if (new == NodeA):
            print("{} != {}".format(new, NodeA))
            print("if->>>Voy a quitar a {} de los abiertos".format(NodeA))
            self.removeNode(NodeA)
            return new
        else:
            print("{} != {}".format(new, NodeB))
            print("else->>Voy a quitar a {} de los abiertos".format(NodeA))
            self.removeNode(NodeA)
            return new


    def openNode(self,Nodes):
        print("----------------abriendo nodos")
        print("openNode/Nodes--->"+str(Nodes))
        for i in Nodes:
            if (i != []):
                if(self.valOpenNode(i)):
                    print("Encontré un nodo abierto igual: {}".format(i[:2]))
                    self.__openNode.append(self.replaceNode(self.regresaNode(i), i))
                else:
                    print("No encontré un nodo igual a este: {}".format(i))
                    self.__openNode.append(i)
        print("->>>openNode:"+str(self.__openNode))

    def removeNode(self,Node):
        print("Removi de los abiertos: {}".format(Node))
        #for nodo in self.__openNode:
            #if Node[:2] == nodo [:2]:
                #print("{} == {}".format(Node[:2], nodo[:2]))
        self.__openNode.remove(Node)

    def closeNode(self,Node):
        #print("-------------------Cerrando Nodos")
        #print("before->CloseNodes/openNode->"+str(self.__openNode))
        #print("before->CloseNodes/closeNode->"+str(self.__closeNode))
        #print("--------------WA quitar->"+str(Node))
        self.__openNode.remove(Node)
        self.__closeNode.append(Node)
        #for node in self.__openNode:
        #print("after->CloseNodes/openNode->"+str(self.__openNode))
        #print("after->CloseNodes/closeNode->"+str(self.__closeNode))

    def bestNode(self,posFinal):
        auxNode = self.__openNode[0]
        menores = []
        menores.append(auxNode)
        Total = ((self.distanceToFinal(auxNode[:2],posFinal)) + (auxNode[2]))
        print("-------------->"+str(Total)+" /Nodo->"+str(auxNode)+" / Distancia"+str(self.distanceToFinal(auxNode,posFinal))+"soy el primero prro")
        for nodo in self.__openNode[1:]:
            print("-------------->"+str(int(self.distanceToFinal(nodo[:2],posFinal))+(nodo[2]))+"Nodo->"+str(nodo)+" / Distancia"+str(self.distanceToFinal(nodo,posFinal)))
            if(Total>(int(self.distanceToFinal(nodo[:2],posFinal)) + (nodo[2]))):#Se cambio <

                #distance_aux = self.distanceToFinal(nodo,posFinal)
                #node_aux = nodo"""
                Total = ((self.distanceToFinal(nodo[:2],posFinal)) + (nodo[2]))
                auxNode = nodo
                menores = []
                menores.append(auxNode)
            elif (Total == (int(self.distanceToFinal(nodo[:2],posFinal)) + (nodo[2]))):
                menores.append(nodo)
                #print("ward")
        #print("Best-->"+str(Total)+"Nodo->"+str(auxNode)+" / Distancia"+str(self.distanceToFinal(auxNode,posFinal)))

        print("en esta iteracion tengo ->>"+str(menores))
        return self.minDistance(menores)

    def minDistance(self, nodes):
        print("-------------entre a Min Distance----------")
        print("-------------->Distancia :"+str(self.distanceToFinal(nodes[0],self.__posFinal))+"  /soy el primero prro")
        aux_menor = self.distanceToFinal(nodes[0][:2],self.__posFinal)
        auxNode = nodes[0]
        for nodo in nodes[1:]:
            #print("-------------->Distancia :"+str(self.distanceToFinal(nodo,self.__posFinal)))
            if(aux_menor > self.distanceToFinal(nodo[:2],self.__posFinal)):
                aux_menor = self.distanceToFinal(nodo[:2],self.__posFinal)
                auxNode = nodo

        print("el mas chidoliro minDistance es:"+str(auxNode)+" / Con ->"+str(aux_menor))
        return auxNode

    def bestValNode(self,NodeA,NodeB):
        if(((self.distanceToFinal(NodeA[:2],self.__posFinal)) + (NodeA[2])) > ((self.distanceToFinal(NodeB[:2],self.__posFinal)) + (NodeB[2]))):
            return NodeB
        else:
            return NodeA
