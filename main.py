from player import Player
#from hazard import Hazard
#from fruit  import Fruit


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

    while True:
        #background, crab, title
        #210 frames per fruit
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
        game(screen,clock,waves,s,crabOnDolphin)


        #loading screen
        #wait for enter? esc to quit
        #wipe loading screen & load game
        #game()

def game(screen,clock,waves,s,crab):
    points = 0
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
    while True:
        pygame.event.pump()
        delta_t = clock.tick(30)/1000
        screen.fill((255, 255, 255))
        screen.blit(waves[0],(0,0))
        screen.blit(crab, player.get_pos())
        pygame.display.flip()
        wavesCounter+=1
        if(wavesCounter>=10):
            waves = [waves[1],waves[0]]
            wavesCounter%=10

        hazardCounter+=hazardAdder
        if(hazardCounter>=15):
            hazards.push(Hazard())
            hazards%=15
            hazardAdder+=.05

        keys = pygame.key.get_pressed()
        y_vel = player.player_move(delta_t, keys[pygame.K_LEFT], keys[pygame.K_RIGHT])

main()