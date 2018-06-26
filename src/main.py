#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from Window.Window import *


def randomPoint(win, tipo):
    dim = win.getDimensions()
    while True:
        start = list()

        start.append(random.randrange(dim[0]))
        start.append(random.randrange(dim[1]))
        #print (start)
        if win.valTerrain(start, tipo):
            break

    return start

def main():
    win = Window()
    #tipo = ["Human","Octopus", "Monkey"]
    tipo = ["Human"]
    players = list()
    for t in tipo:
        posStart = randomPoint(win, t)
        posFinal = randomPoint(win, t)
        #posStart = [8,9]
        #posFinal = [10,9]
        players.append([t, posStart, [posFinal]])
        print("Player: {}".format(players))
        print("Tipo: {}\tInicio: {}\tFinal: {}".format(t, posStart, posFinal))
    win.setPlayers(players)

    win.loop()

if __name__ == '__main__':
    main()
