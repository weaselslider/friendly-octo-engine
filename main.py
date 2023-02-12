from player import Player
from sprites import *


import pygame
import json


def main():
    pygame.font.init()
    clock = pygame.time.Clock()
    imgs = [];
    args = {}
    #with file.open("settings.json","r") as f:
    #    args = json.loads(f.read())

    wave1 = pygame.image.load("wave1.png")
    wave1 = pygame.transform.scale(wave1,(1600,900))
    wave2 = pygame.image.load("wave2.png")
    wave2 = pygame.transform.scale(wave2,(1600,900))
    waves = [wave1,wave2]

    bg1 = pygame.image.load("Beach1.png")
    bg1 = pygame.transform.scale(bg1, (1600,900))
    bg2 = pygame.image.load("Beach2.png")
    bg2 = pygame.transform.scale(bg2, (1600,900))
    bg=[bg1,bg2]
    screen = pygame.display.set_mode((1600,900))

    dude = pygame.image.load("./img/other/front_facing_crab.png")
    dude = pygame.transform.scale(dude,(536,224))

    CrabFont =     pygame.font.SysFont("Comic Sans MS", 150)
    MiniCrabFont = pygame.font.SysFont("Comic Sans MS", 15)

    TitleLabel = CrabFont.render("Dood & Bro", 1, (50,50,50))
    SubLabel = MiniCrabFont.render("start: enter & exit: esc", 1, (50,50,50))

    crabOnDolphin = pygame.image.load("./img/other/crab_on_dolphin.png")

    backgroundCounter = 0;

    bgAlpha = 0

    bgAlpha=0
    for i in range(0,20):

        pygame.event.pump()
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
    while True:
        #background, crab, title
        #210 frames per fruit


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
        pygame.event.get()

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
            #blit the text!
            screen.blit(TitleLabel,(600,150))
            screen.blit(SubLabel,(350,600))
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
            screen.blit(TitleLabel,(600,150))
            crabPos+=crabVel
            crabVel+=crabAccel
            pygame.display.flip()
            backgroundCounter+=1
            if(backgroundCounter%10==0):
                bg = [bg[1],bg[0]]
                backgroundCounter=0

        fadAlpha = 0;
        s = pygame.Surface((1600,900))
        s.fill((0,0,0))
        for i in range(0,20):
            clock.tick(30)
            screen.fill((0, 0, 0))
            screen.blit(bg[0],(0,0))
            screen.blit(TitleLabel,(600,150))
            s.set_alpha(fadAlpha)
            screen.blit(s,(0,0))
            fadAlpha+=12.5
            pygame.display.flip()
            backgroundCounter+=1
            if(backgroundCounter>=10):
                bg = [bg[1],bg[0]]
                backgroundCounter=0

        screen.fill((0,0,0));
        pygame.display.flip()
        time,fruit = game(screen,clock,waves,s,crabOnDolphin,MiniCrabFont)

        #scoarboard
        a = CrabFont.render("Time : "+str(time),1, (50,50,50))
        b = CrabFont.render("Fruit: "+str(fruit),1, (50,50,50))
        c = CrabFont.render("SCORE: "+str(time+fruit),1, (50,50,50))

        #fade into start
        opacity = 255
        for i in range(0,20):
            pygame.event.pump()
            clock.tick(30)
            opacity-=12.75
            screen.fill((0,0,0))
            screen.blit(bg[0],(0,0))
            backgroundCounter+=1
            if(backgroundCounter%10==0):
                bg = [bg[1],bg[0]]
                backgroundCounter=0
            screen.blit(a, (400,150))
            screen.blit(b, (400,350))
            screen.blit(c, (400,550))
            s.set_alpha(opacity)
            screen.blit(s,(0,0))
            pygame.display.flip()

        while(True):
            pygame.event.pump()
            clock.tick(30)
            bre = False
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        quit()
                    if event.key == pygame.K_RETURN:
                        bre = True
                        break

            if(bre):break





        #loading screen
        #wait for enter? esc to quit
        #wipe loading screen & load game
        #game()

def game(screen,clock,waves,s,crab,font):
    timePoints = 0
    fruitPoints = 0
    player = Player(800-43,700,1);
    wavesCounter = 0;
    fadAlpha=255
    for i in range(0,20):
        pygame.event.pump()
        clock.tick(30)
        screen.fill((0, 0, 0))
        screen.blit(waves[0],(0,0))
        screen.blit(crab, player.get_pos())
        s.set_alpha(fadAlpha)
        screen.blit(s,(0,0))
        fadAlpha-=12.5
        pygame.display.flip()
        wavesCounter+=1
        if(wavesCounter>=10):
            waves = [waves[1],waves[0]]
            wavesCounter%=10

    #delta t
    #fade in
    hazards = []
    fruits = []
    hazardCounter = 0
    hazardAdder = 1
    fruitCounter = 0
    pointCounter = 0
    center = (0,0)
    while True:
        pygame.event.pump()
        delta_t = clock.tick(30)/1000
        screen.fill((255, 255, 255))
        screen.blit(waves[0],(0,0))
        crabRect = screen.blit(crab, player.get_pos())


        wavesCounter+=1
        if(wavesCounter>=10):
            waves = [waves[1],waves[0]]
            wavesCounter%=10

        hazardCounter+=hazardAdder
        if(hazardCounter>=25):
            hazards.append(Hazard())
            hazardCounter%=15
            hazardAdder+=.05

        fruitCounter+=1
        if(fruitCounter>=210):
            fruits.append(Fruit())
            fruitCounter = 0

        pointCounter+=1
        if(pointCounter>=30):
            timePoints+=1
            pointCounter%=30

        keys = pygame.key.get_pressed()
        y_vel = player.player_move(delta_t, keys[pygame.K_LEFT], keys[pygame.K_RIGHT])

        #draw, update fruits & hazards
        #also, collision checks
        mid = crabRect.center
        collisionRect = crabRect.copy()
        collisionRect.width/=2
        collisionRect.height/=2
        collisionRect.center = mid

        for i in range(len(fruits)-1,-1,-1):
            #do stuff
            pos = (fruits[i].xPos,fruits[i].yPos)
            img = fruits[i].getImage()
            fruit_rect = screen.blit(img, pos)
            fruits[i].updatePos(y_vel,delta_t)
            if collisionRect.colliderect(fruit_rect):
                fruitPoints+=fruits[i].collision()
                fruits.pop(i)

        brek = False
        for i in range(len(hazards)-1,-1,-1):
            #do stuff
            pos = (hazards[i].xPos,hazards[i].yPos)
            img = hazards[i].getImage()
            hazard_rect = screen.blit(img, pos)
            hazards[i].updatePos(y_vel,delta_t)
            if collisionRect.colliderect(hazard_rect):
                brek=True
                break
            #do stuff



        #display points here?
        ScoreLabel = font.render(str(timePoints+fruitPoints), 1, (50,50,50))
        screen.blit(ScoreLabel,(800,100))

        pygame.display.flip()
        if(brek):
            center = mid
            break
    #outtro here.


    print(timePoints)
    print(fruitPoints)
    degree = 0;
    center = (center[0],center[1]-150)
    for i in range(0,16):
        clock.tick(30)
        screen.fill((255, 255, 255))
        screen.blit(waves[0],(0,0))
        wavesCounter+=1
        if(wavesCounter>=10):
            waves = [waves[1],waves[0]]
            wavesCounter%=10
        for i in fruits:
            screen.blit(i.getImage(),(i.xPos,i.yPos))
        for i in hazards:
            screen.blit(i.getImage(),(i.xPos,i.yPos))
        rat = pygame.transform.rotate(crab,degree)
        #do the rat
        screen.blit(rat,center)
        degree+=20


        pygame.display.flip()
    opacity = 0
    for i in range(0,15):
        clock.tick(30)
        screen.fill((255, 255, 255))
        screen.blit(waves[0],(0,0))
        wavesCounter+=1
        if(wavesCounter>=10):
            waves = [waves[1],waves[0]]
            wavesCounter%=10
        for i in fruits:
            screen.blit(i.getImage(),(i.xPos,i.yPos))
        for i in hazards:
            screen.blit(i.getImage(),(i.xPos,i.yPos))
        rat = pygame.transform.rotate(crab,degree)
        #do the rat
        screen.blit(rat,center)
        degree+=20
        s.set_alpha(opacity)
        screen.blit(s,(0,0))
        opacity+=16
        pygame.display.flip()

    clock.tick(30)
    s.set_alpha(255)
    screen.blit(s,(0,0))
    pygame.display.flip()
    clock.tick(30)




    return (timePoints, fruitPoints)

main()
