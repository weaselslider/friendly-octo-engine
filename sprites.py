import os
from random import randint

INITIAL_SCREEN_WIDTH = 1600
INITIAL_SCREEN_HEIGHT = 900

HAZARD_LIST = [("img/hazard/" + filename) for filename in os.listdir('img/hazard')]
FRUIT_LIST = [("img/fruit/" + filename) for filename in os.listdir('img/fruit')]


# abstract object/sprite class
# stores name, image file path, position of sprite, and drift attributes
class Sprite:
    image = None
    drift = randint(0, 40)
    name = None

    def __init__(self):
        self.xPos = randint(0, INITIAL_SCREEN_WIDTH)
        self.yPos = 0
        self.startSide = 'l' if (self.xPos < INITIAL_SCREEN_WIDTH) else 'r'

    # update sprite position
    def updatePos(self, vel):
        self.yPos -= vel
        if self.drift != 0:
            if self.startSide == 'l':
                self.xPos += self.drift
            else:
                self.xPos -= self.drift

    def collision(self):
        return 0

    # getter function for image
    def getImage(self):
        return self.image

    # getter function for name
    def getName(self):
        return self.name


# hazard class -> when instantiated, object is assigned jpg of random hazard
class Hazard(Sprite):
    def __init__(self):
        super().__init__()
        self.image = HAZARD_LIST[randint(0, len(HAZARD_LIST)-1)]
        _, _, self.name = self.image.split("/")

    def collision(self):
        return -1   # death / end of game


# fruit class -> when instantiated, object is assigned jpg of random fruit
class Fruit(Sprite):
    def __init__(self):
        super().__init__()
        self.image = FRUIT_LIST[randint(0, len(FRUIT_LIST) - 1)]
        _, _, self.name = self.image.split("/")

    # depending on the fruit that the player collides with, a different number of points are added to the score
    def collision(self):
        if self.name == "pineapple":
            return 5
        elif self.name == "bananas":
            return 3
        elif self.name == "coconut":
            return 1
