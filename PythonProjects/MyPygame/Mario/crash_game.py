import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('A bit Racey')

clock = pygame.time.Clock()

crashed = False
x = 50
y = 50


while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True


    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()