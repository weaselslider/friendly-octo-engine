import os
from random import randint
import pygame

INITIAL_SCREEN_WIDTH = 1600
INITIAL_SCREEN_HEIGHT = 900

HAZARD_FILE_PATHS = [("img/hazard/" + filename) for filename in os.listdir('img/hazard')]
FRUIT_FILE_PATHS = [("img/fruit/" + filename) for filename in os.listdir('img/fruit')]

HAZARD_IMAGES = [pygame.transform.scale(pygame.image.load("img/hazard/" + filename), (75, 75)) for filename in os.listdir('img/hazard')]
FRUIT_IMAGES = [pygame.transform.scale(pygame.image.load("img/fruit/" + filename), (75, 75)) for filename in os.listdir('img/fruit')]


# abstract object/sprite class
# stores name, image file path, position of sprite, and drift attributes
class Sprite:
    imageIndex = None
    drift = randint(0, 40)
    name = None

    def __init__(self):
        self.xPos = randint(0, INITIAL_SCREEN_WIDTH)
        self.yPos = 0
        self.startSide = 'l' if (self.xPos < INITIAL_SCREEN_WIDTH/2) else 'r'

    def __del__(self):
        return

    # update sprite position
    def updatePos(self, vel, dt=1):
        self.yPos += vel*dt
        if self.drift != 0:
            if self.startSide == 'l':
                self.xPos += self.drift*dt
            else:
                self.xPos -= self.drift*dt

        if not (0 <= self.xPos <= INITIAL_SCREEN_WIDTH and 0 <= self.yPos <= INITIAL_SCREEN_HEIGHT):
            del self

    def collision(self):
        return 0

    # getter function for image
    def getImage(self):
        return

    # getter function for name
    def getName(self):
        return self.name


# hazard class -> when instantiated, object is assigned jpg of random hazard
class Hazard(Sprite):
    def __init__(self):
        super().__init__()
        self.imageIndex = randint(0, len(HAZARD_FILE_PATHS) - 1)
        _, _, self.name = HAZARD_FILE_PATHS[self.imageIndex].split("/")

    def getImage(self):
        return HAZARD_IMAGES[self.imageIndex]

    def getName(self):
        name, _ = self.name.split(".")
        return name

    def collision(self):
        return -1   # death / end of game


# fruit class -> when instantiated, object is assigned jpg of random fruit
class Fruit(Sprite):
    def __init__(self):
        super().__init__()
        self.imageIndex = randint(0, len(FRUIT_FILE_PATHS) - 1)
        _, _, self.name = FRUIT_FILE_PATHS[self.imageIndex].split("/")

    def getImage(self):
        return FRUIT_IMAGES[self.imageIndex].split(".")

    def getName(self):
        name, _ = self.name.split(".")
        return name

    # depending on the fruit that the player collides with, a different number of points are added to the score
    def collision(self):
        if self.name == "pineapple":
            return 5
        elif self.name == "bananas":
            return 3
        elif self.name == "coconut1" or self.name == "coconut2":
            return 1
