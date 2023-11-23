import pygame

pygame.init()

win = pygame.display.set_mode((500,480))
pygame.display.set_caption("My First Game")

walkRight = [pygame.image.load('game/R1.png'), pygame.image.load('game/R2.png'), pygame.image.load('game/R3.png'),
             pygame.image.load('game/R4.png'), pygame.image.load('game/R5.png'), pygame.image.load('game/R6.png'),
             pygame.image.load('game/R7.png'), pygame.image.load('game/R8.png'), pygame.image.load('game/R9.png')]
walkLeft = [pygame.image.load('game/L1.png'), pygame.image.load('game/L2.png'), pygame.image.load('game/L3.png'),
            pygame.image.load('game/L4.png'), pygame.image.load('game/L5.png'), pygame.image.load('game/L6.png'),
            pygame.image.load('game/L7.png'), pygame.image.load('game/L8.png'), pygame.image.load('game/L9.png')]
bg = pygame.image.load('game/bg.jpg')
char = pygame.image.load('game/standing.png')

clock = pygame.time.Clock()


class Player(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.left:
            win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(char, (self.x, self.y))


man = Player(0, 420, 40, 60)


def redrawGameWindow():
    win.blit(bg, (0, 0))
    man.draw(win)
    pygame.display.update()


##Main loop
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.left = False
        man.right = True
    else:
        man.left = False
        man.right = False
        man.walkCount = 0

    if not man.isJump:
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.left = False
            man.right = False
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
                man.y -= (man.jumpCount ** 2) * 0.5 * neg
                man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()


pygame.quit()
