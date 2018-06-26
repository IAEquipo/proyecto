#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from threading import Thread
from Window.Window import *

tipo = ["Human","Octopus", "Monkey"]

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

def run(inicio, fin):
    win = Window()
    global tipo
    for t in tipo:
        players.append([t, inicio, fin])
        print("Tipo: {}\tInicio: {}\tFinal: {}".format(t, posStart, posFinal))
    win.setPlayers(players)

    win.loop()

def main():
    """
    start = randomPoint(win, t)
    darkTemple = randomPoint(win, t)
    magicStones = randomPoint(win, t)
    key = randomPoint(win, t)
    portal = randomPoint(win, t)

    darkTempleT = Thread(target=run , args(start,darkTemple,))
    darkTempleToPortalT = Thread(target=run , args(darkTemple,portal,))

    magicStonesT = Thread(target=run , args(start,magicStones,))
    magicStonesToPortalT = Thread(target=run , args(magicStones,portal,))

    keyT = Thread(target=run , args(start,key,))
    keyToPortalT = Thread(target=run , args(key,portal,))

    darkTempleT.start()
    darkTempleToPortalT.start()
    magicStonesT.start()
    magicStonesToPortalT.start()
    keyT.start()
    keyToPortalT.start()

    darkTempleT.join()
    darkTempleToPortalT.join()
    magicStonesT.join()
    magicStonesToPortalT.join()
    keyT.join()
    keyToPortalT.join()
    """
    global tipo
    win = Window()
    start = randomPoint(win, tipo[0])
    darkTemple = randomPoint(win, tipo[0])
    darkTempleT = Thread(target=run , args=(start,darkTemple,))
    darkTempleT.start()
    darkTempleT.join()
    """
    win = Window()
    tipo = ["Human"]
    players = list()
    for t in tipo:
        #posStart = randomPoint(win, t)
        #posFinal = randomPoint(win, t)
        posStart = [8,9]
        posFinal = [10,9]
        players.append([t, posStart, posFinal])
        #print("Player: {}".format(players))
        print("Tipo: {}\tInicio: {}\tFinal: {}".format(t, posStart, posFinal))
    win.setPlayers(players)

    win.loop()
    """

if __name__ == '__main__':
    main()
