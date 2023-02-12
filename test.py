from sprites import *
# import time
from pygame.locals import *

screen = pygame.display.set_mode((500, 500))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_1:
                a = Hazard()
                screen.fill((175, 238, 238))
                screen.blit(a.getImage(), (250, 250))
                print(a.getName())

    pygame.display.flip()
pygame.quit()