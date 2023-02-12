import os
from random import randint

SCREEN_WIDTH = 1600

IMAGE_LIST = [("img/" + filename) for filename in os.listdir('img')]
# print(IMAGE_LIST)

class Object:
    def __init__(self):
        xPos = randint(0, 100)
        yPos = 0
        pass

    def update(self, y, d, t):
        pass