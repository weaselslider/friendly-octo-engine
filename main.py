#from player import Player
#from hazard import Hazard
#from fruit  import Fruit


import pygame
import json


def main():
    clock = pygame.time.Clock()
    imgs = [];
    args = {}
    #with file.open("settings.json","r") as f:
    #    args = json.loads(f.read())

    bg1 = pygame.image.load("Beach1.png")
    bg1 = pygame.transform.scale(bg1, (1600,900))
    bg2 = pygame.image.load("Beach2.png")
    bg2 = pygame.transform.scale(bg2, (1600,900))
    bg=[bg1,bg2]
    screen = pygame.display.set_mode((1600,900))

    dude = pygame.image.load("./img/other/front_facing_crab.png")
    dude = pygame.transform.scale(dude,(536,224))

    backgroundCounter = 0;

    bgAlpha = 0

    while True:
        #background, crab, title
        #210 frames per fruit
        screen.fill((255, 255, 255))
        bgAlpha=0
        for i in range(0,20):

            pygame.event.pump()
            print(bgAlpha)
            clock.tick(30)
            screen.fill((0, 0, 0))
            bg[0].set_alpha(bgAlpha)
            screen.blit(bg[0],(0,0))
            pygame.display.flip()
            backgroundCounter+=1
            bgAlpha+=12.75
            if(backgroundCounter%10==0):
                bg = [bg[1],bg[0]]
                backgroundCounter=0
        bg[0].set_alpha(255)
        bg[1].set_alpha(255)
        screen.blit(bg[0],(800,450))

        #now, the CRAB!
        crabPos= -600
        crabVel= 75
        crabAccel = -2
        for i in range(0,35):
            pygame.event.pump()
            clock.tick(30)
            screen.fill((0, 0, 0))
            screen.blit(bg[0],(0,0))
            screen.blit(dude,(crabPos,500))
            crabPos+=crabVel
            crabVel+=crabAccel
            pygame.display.flip()
            backgroundCounter+=1
            if(backgroundCounter%10==0):
                bg = [bg[1],bg[0]]
                backgroundCounter=0

        #Dude and Bro
        #start: enter
        #quit: esc
        while(True):
            clock.tick(30)
            bre=False
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        quit()
                    if event.key == pygame.K_RETURN:
                        bre = True
                        break

            if(bre):break
            screen.blit(bg[0],(0,0))
            screen.blit(dude,(crabPos,500))
            print("somethin")
            backgroundCounter+=1
            if(backgroundCounter%10==0):
                bg = [bg[1],bg[0]]
                backgroundCounter=0
            pygame.display.flip()




        #crab out


        for i in range(0,45):
            pygame.event.pump()
            clock.tick(30)
            screen.fill((0, 0, 0))
            screen.blit(bg[0],(0,0))
            screen.blit(dude,(crabPos,500))
            crabPos+=crabVel
            crabVel+=crabAccel
            pygame.display.flip()
            backgroundCounter+=1
            if(backgroundCounter%10==0):
                bg = [bg[1],bg[0]]
                backgroundCounter=0


        #loading screen
        #wait for enter? esc to quit
        #wipe loading screen & load game
        #game()

#def game(screen,clock ):
#    points = 0
#    player = new Player();
#    #delta t
#    while True:
#        clock.tick(30)
#        screen.fill((255, 255, 255))


main()
