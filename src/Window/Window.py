#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, sys, os

from pygame.locals import *
from Map.Map import *
from Being.Being import *

BLACK = (0, 0, 0)
ORANGE_L = (252, 190, 149)
BLUE = (0, 177, 249)
YELLOW = (255, 190, 65)
GREEN = (146, 209, 101)
PURPLE = (208, 147, 224)
WHITE = (255, 255, 255)


DEFAULT = (123, 244, 180)

COLOR_FINAL = (255, 0, 186)
COLOR_L = (244,110,120)
COLOR_LABEL = (255,0,255)

COLOR_HUMAN = (243, 123, 173)
COLOR_MONKEY = (193, 51, 13)
COLOR_OCTOPUS = (47, 11, 94)
COLOR_CROC = (18, 97, 6)
COLOR_SASQUATCH = (10, 22, 193)
COLOR_WEREWOLF = (77, 76, 76)

PIXEL = 30

#Finished = [0,0,0]
#costo = ""
#ruta = ""


class Window(object):

    def __init__(self):
        global PIXEL
        pygame.init()
        self.__map = Map()
        self.__dim = self.__map.getDimensions
        self.__canvas = pygame.display.set_mode([self.__dim[0]*PIXEL,self.__dim[1]*PIXEL])
        self.__beings = list()
        self.__reloj = pygame.time.Clock()
        pygame.display.set_caption('Artificial Intelligence')

    def loop(self):
        pygame.display.flip()
        self.paint()
        while True:
            if(pygame.mouse.get_pressed()[0] != 0):
                self.ask_terrain()

            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    sys.exit(0)

            if(pygame.mouse.get_pressed()[2] != 0):
                self.change_terrain()
                self.paint()

            for being in self.__beings:
                if not(being.finished()):
                    being.move(self.__map.getBesideTerrain(being.getPos(), being.getType()))
                else:
                    pass
                    #costo = costo + str(being.getCost()) + ','
                    #file.write(costo)
                    #ruta = ruta + str (being.getRoute()) + ','
                    #file.write(ruta)

            #self.createFile()
            pygame.display.flip()
            self.paint()
            self.__reloj.tick(7)

    def paint(self):
        global PIXEL
        x=0
        y=0
        for line in self.__map.getMatrix():
            for value in line:
                if value == '0':
                    global BLACK#Montaña
                    pygame.draw.rect(self.__canvas, BLACK, (x, y, PIXEL, PIXEL), 0)
                elif value == '1':
                    global ORANGE_L#Tierra
                    pygame.draw.rect(self.__canvas, ORANGE_L, (x, y, PIXEL, PIXEL), 0)
                elif value == '2':
                    global BLUE#Agua
                    pygame.draw.rect(self.__canvas, BLUE, (x, y, PIXEL, PIXEL), 0)
                elif value == '3':
                    global YELLOW#Arena
                    pygame.draw.rect(self.__canvas, YELLOW, (x, y, PIXEL, PIXEL), 0)
                elif value == '4':
                    global GREEN#Bosque
                    pygame.draw.rect(self.__canvas, GREEN, (x, y, PIXEL, PIXEL), 0)
                elif value == '5':
                    global PURPLE#Pantano
                    pygame.draw.rect(self.__canvas, GREEN, (x, y, PIXEL, PIXEL), 0)
                elif value == '6':
                    global WHITE#Nieve
                    pygame.draw.rect(self.__canvas, GREEN, (x, y, PIXEL, PIXEL), 0)
                elif value == -1:
                    global GRAY#Sombra
                    pygame.draw.rect(self.__canvas, GRAY, (x, y, PIXEL, PIXEL), 0)
                else:
                    global DEFAULT
                    pygame.draw.rect(self.__canvas, DEFAULT, (x, y, PIXEL, PIXEL), 0)
                y += PIXEL
            x += PIXEL
            y = 0
        global COLOR_FINAL
        for being in self.__beings:
            if being.getType() == "Human":
                global COLOR_HUMAN
                pos = being.getPos()
                pygame.draw.rect(self.__canvas, COLOR_HUMAN, (pos[0]*PIXEL, pos[1]*PIXEL, PIXEL, PIXEL), 0)
            elif being.getType() == "Monkey":
                global COLOR_MONKEY
                pos = being.getPos()
                pygame.draw.rect(self.__canvas, COLOR_MONKEY, (pos[0]*PIXEL, pos[1]*PIXEL, PIXEL, PIXEL), 0)
            elif being.getType() == "Octopus":
                global COLOR_OCTOPUS
                pos = being.getPos()
                pygame.draw.rect(self.__canvas, COLOR_OCTOPUS, (pos[0]*PIXEL, pos[1]*PIXEL, PIXEL, PIXEL), 0)
            elif being.getType() == "Croc":
                global COLOR_CROC
                pos = being.getPos()
                pygame.draw.rect(self.__canvas, COLOR_CROC, (pos[0]*PIXEL, pos[1]*PIXEL, PIXEL, PIXEL), 0)
            elif being.getType() == "Sasquatch":
                global COLOR_SASQUATCH
                pos = being.getPos()
                pygame.draw.rect(self.__canvas, COLOR_SASQUATCH, (pos[0]*PIXEL, pos[1]*PIXEL, PIXEL, PIXEL), 0)
            elif being.getType() == "Werewolf":
                global COLOR_WEREWOLF
                pos = being.getPos()
                pygame.draw.rect(self.__canvas, COLOR_WEREWOLF, (pos[0]*PIXEL, pos[1]*PIXEL, PIXEL, PIXEL), 0)
            final = being.getFinal()
            pygame.draw.rect(self.__canvas, COLOR_FINAL, (final[0]*PIXEL, final[1]*PIXEL, PIXEL, PIXEL), 0)

    def ask_terrain(self):
        global COLOR_L
        pos = pygame.mouse.get_pos()
        num = self.__map.getMatrix()[pos[0]//PIXEL][pos[1]//PIXEL]
        font = pygame.font.SysFont('comicsansms', 30)

        if num == '0':
            label = font.render("Mountain", 1, COLOR_L)
        elif num == '1':
            label = font.render("Earth", 1, COLOR_L)
        elif num == '2':
            label = font.render("Water", 1, COLOR_L)
        elif num == '3':
            label = font.render("Sand", 1, COLOR_L)
        elif num == '4':
            label = font.render("Forest", 1, COLOR_L)
        elif num == '5':
            label = font.render("Swamp", 1, COLOR_L)
        elif num == '6':
            label = font.render("Snow", 1, COLOR_L)

        self.__canvas.blit(label, (pos[0], pos[1]))

    def change_terrain(self):
        posMouse = pygame.mouse.get_pos()

        while True:
            print ("Moutain -> 0\nEarth -> 1\nWater -> 2\nSand -> 3\nForest -> 4\n")
            newTerrain = str(input("Insert the value for change the terrain: "))

            if newTerrain < "5" and newTerrain >= "0":
                break
        pos = list()
        pos.append(posMouse[0]//PIXEL)
        pos.append(posMouse[1]//PIXEL)
        self.__map.setVal(pos, newTerrain)


    def valTerrain(self, pos, tipo):
        return self.__map.valTerrain(pos, tipo)

    def getDimensions(self):
        return self.__dim

    def setPlayers(self, players):
        for player in players:
            aux = Being(player[0], player[1], player[2])
            self.__beings.append(aux)

    def createFile(self):
        file = open(self.filename, "w")
