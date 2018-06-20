#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Being(object):

    def __init__(self, tipo, start, final):
        self.__type = tipo
        self.__pos = start
        self.__final = final

    def getPos(self):
        return self.__pos

    def move(self):
        pass

    def getFinal(self):
        return self.__final
