#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from multiprocessing import Process
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

def run(inicio, fin):
    win = Window()
    global tipo
    for t in tipo:
        players.append([t, inicio, fin])
        print("Tipo: {}\tInicio: {}\tFinal: {}".format(t, posStart, posFinal))
    win.setPlayers(players)

    win.loop()

def main():
    win = Window()
    tipo = ["Human"]
    players = list()
    for t in tipo:
        #posStart = randomPoint(win, t)
        #posFinal = randomPoint(win, t)
        posStart = [8,9]
        posFinal = [10,14]
        players.append([t, posStart, posFinal])
        #print("Player: {}".format(players))
        print("Tipo: {}\tInicio: {}\tFinal: {}".format(t, posStart, posFinal))
    win.setPlayers(players)

    win.loop()

if __name__ == '__main__':
    main()
"""
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
    tipo = ["Human","Octopus", "Monkey"]
    players = list()
    print("{}\tInicio: {}\tFinal: {}".format(name, inicio, final))
    for t in tipo:
        players.append([t, inicio, final])
    win.setPlayers(players)

    win.loop()

def main():
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


if __name__ == '__main__':
    main()
"""
