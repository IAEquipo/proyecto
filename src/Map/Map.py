#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Archivo.Archivo import *

class Map(object):

    def __init__(self):
        text = Archivo()
        self.__dimensions = list()
        self.__matrix = text.read('lab2.txt')
        self.__dimensions.append(len(self.__matrix))
        self.__dimensions.append(len(self.__matrix[0]))
        #self.__darkside = [[-1 for j in range(self.__dimensions[0])] for i in range(self.__dimensions[1])]

    def getDimensions(self):
        return self.__dimensions

    def getMatrix(self):
        return self.__matrix

    """def getDarkSide(self):
        return self.__darkside"""

    def setVal(self, pos, val):
        px = pos[0]
        py = pos[1]
        self.__matrix[px][py] = val

    def validate(self, start, tipo):
        return self.__matrix[start[0]][start[1]] != '0'
