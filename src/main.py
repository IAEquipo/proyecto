#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from multiprocessing import Process
from Window.Window import *

win = Window()

def randomPoint(tipo):
    global win
    while True:
        start = list()
        start.append(random.randrange(win.getDimensions()[0]))
        start.append(random.randrange(win.getDimensions()[1]))
        #print (start)
        if win.valTerrain(start, tipo):
            break
    return start

def run(inicio, final, name):
    win = Window()
    tipo = ["Human", "Monkey", "Octopus"]
    players = list()
    print("{}\tInicio: {}\tFinal: {}".format(name, inicio, final))
    for t in tipo:
        players.append([t, inicio, final])
    win.setPlayers(players)

    win.loop()

def main():
    files = list()
    start = randomPoint("Human")
    darkTemple = randomPoint("Human")
    magicStones = randomPoint("Human")
    key = randomPoint("Human")
    portal = randomPoint("Human")

    darkTempleT = Process(target=run , args=(start,darkTemple,"darkTempleT",))
    darkTempleToPortalT = Process(target=run , args=(darkTemple,portal,"darkTempleToPortalT",))


    magicStonesT = Process(target=run , args=(start,magicStones,"magicStonesT",))
    magicStonesToPortalT = Process(target=run , args=(magicStones,portal,"magicStonesToPortalT",))

    keyT = Process(target=run , args=(start,key,"keyT",))
    keyToPortalT = Process(target=run , args=(key,portal,"keyToPortalT",))

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

    files.append(str(start[0]) + str(start[1]) + "_" + str(darkTemple[0]) + str(darkTemple[1]) + ".txt")
    files.append(str(darkTemple[0]) + str(darkTemple[1]) + "_" + str(portal[0]) + str(portal[1]) + ".txt")
    files.append(str(start[0]) + str(start[1]) + "_" + str(magicStones[0]) + str(magicStones[1]) + ".txt")
    files.append(str(magicStones[0]) + str(magicStones[1]) + "_" + str(portal[0]) + str(portal[1]) + ".txt")
    files.append(str(start[0]) + str(start[1]) + "_" + str(key[0]) + str(key[1]) + ".txt")
    files.append(str(key[0]) + str(key[1]) + "_" + str(portal[0]) + str(portal[1]) + ".txt")

    aux = Archivo()
    costos = list()
    for file in files:
        costos.append(aux.readOut(file)[0])

    for costo in costos:
        print(costo)

if __name__ == '__main__':
    main()
