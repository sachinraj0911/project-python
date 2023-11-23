import pygame

pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("My First Game")


x = 0
y = 440
width = 40
height = 60

vel = 5


run = True

while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    ### Keys movement and boundries
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - width:
        x += vel
    win.fill((0, 0, 0))
    pygame.draw.circle(win, (255, 0, 0), (x , y), 6, 1)
    if keys[pygame.K_SPACE]:
        for i in range(100):
            x += vel
            pygame.draw.circle(win, (255, 0, 0), (x, y), 10, 1)
    pygame.display.update()

pygame.quit()
