import os
from random import randint

SCREEN_WIDTH = 1600

HAZARD_LIST = [("img/hazard/" + filename) for filename in os.listdir('img/hazard')]
FRUIT_LIST = [("img/fruit/" + filename) for filename in os.listdir('img/fruit')]


class Object:
    image = None
    drift = 0
    name = None

    def __init__(self):
        self.xPos = randint(0, SCREEN_WIDTH)
        self.yPos = 0

    def updatePos(self, vel):
        if self.drift == 0:
            self.yPos -= vel

    def collision(self):
        return 0

    def getImage(self):
        return self.image

    def getName(self):
        return self.name


class Hazard(Object):
    def __init__(self):
        super().__init__()
        self.image = HAZARD_LIST[randint(0, len(HAZARD_LIST)-1)]
        _, _, self.name = self.image.split("/")

    def collision(self):
        return -1


class Fruit(Object):
    def __init__(self):
        super().__init__()
        self.image = FRUIT_LIST[randint(0, len(FRUIT_LIST) - 1)]
        _, _, self.name = self.image.split("/")

    def collision(self):
        return 1
