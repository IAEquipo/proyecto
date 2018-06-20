#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from Window.Window import *

def randomPoint(win, tipo):
    dim = win.getDimensions()
    while True:
        #start = []
        start = list()
        start.append(random.randrange(dim[0]))
        start.append(random.randrange(dim[1]))

        if win.askStart(start, tipo):
            break

    return start

if __name__ == '__main__':
    win = Window()
    tipo = ["Humano","Octopus", "Monkey"]
    players = list()
    for t in tipo:
        posStart = randomPoint(win, t)
        posFinal = randomPoint(win, t)
        players.append([t, posStart, [posFinal]])
        print("Tipo: {}\tInicio: {}\tFinal: {}".format(t, posStart, posFinal))
    win.setPlayers(players)

    win.loop()
