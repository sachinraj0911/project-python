import pygame
from MyPygame.Mario.settings import *

pygame.init()


win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mario-lev1")

walkRight = [pygame.image.load('game/R1.png'), pygame.image.load('game/R2.png'), pygame.image.load('game/R3.png'),
             pygame.image.load('game/R4.png'), pygame.image.load('game/R5.png'), pygame.image.load('game/R6.png'),
             pygame.image.load('game/R7.png'), pygame.image.load('game/R8.png'), pygame.image.load('game/R9.png')]
walkLeft = [pygame.image.load('game/L1.png'), pygame.image.load('game/L2.png'), pygame.image.load('game/L3.png'),
            pygame.image.load('game/L4.png'), pygame.image.load('game/L5.png'), pygame.image.load('game/L6.png'),
            pygame.image.load('game/L7.png'), pygame.image.load('game/L8.png'), pygame.image.load('game/L9.png')]
bg = pygame.image.load('game/bg.jpg')
char = pygame.image.load('game/standing.png')
bulletSound = pygame.mixer.music.load('game/bullet.mp3')
hitSound = pygame.mixer.music.load('game/hit.mp3')
music = pygame.mixer.music.load('game/music.mp3')
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()


class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = True
        self.walkCount = 0
        self.standing = True
        self.hitBox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not self.standing:
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))

        self.hitBox = (self.x + 17, self.y + 11, 29, 52)
        #pygame.draw.rect(win, (255, 0, 0), self.hitBox, 2)

    def hit(self):
        #reseting the man position
        self.isJump = False
        self.jumpCount = 10
        self.x = 10
        self.y = 410
        self.walkCount = 0
        # reseting the enemy position
        enemy.x = 410
        enemy.y = 410
        enemy.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('Game Over', 1, RED)
        win.blit(text, (250 - (text.get_width() / 2), 200))
        pygame.display.update()
        i = 0
        while i < 200:
            pygame.time.delay(5)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 201
                    pygame.quit()


class Bullets:
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.facing = facing
        self.vel = 8*facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


class Enemy:
    walkRight = [pygame.image.load('game/R1E.png'), pygame.image.load('game/R2E.png'), pygame.image.load('game/R3E.png'),
                 pygame.image.load('game/R4E.png'), pygame.image.load('game/R5E.png'), pygame.image.load('game/R6E.png'),
                 pygame.image.load('game/R7E.png'), pygame.image.load('game/R8E.png'), pygame.image.load('game/R9E.png'),
                 pygame.image.load('game/R10E.png'), pygame.image.load('game/R11E.png')]
    walkLeft = [pygame.image.load('game/L1E.png'), pygame.image.load('game/L2E.png'), pygame.image.load('game/L3E.png'),
                pygame.image.load('game/L4E.png'), pygame.image.load('game/L5E.png'), pygame.image.load('game/L6E.png'),
                pygame.image.load('game/L7E.png'), pygame.image.load('game/L8E.png'), pygame.image.load('game/L9E.png'),
                pygame.image.load('game/L10E.png'), pygame.image.load('game/L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.vel = 3
        self.walkCount = 0
        self.path = [self.x, self.end]
        self.hitBox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win, RED, (self.hitBox[0], self.hitBox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0, 128, 0), (self.hitBox[0], self.hitBox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitBox = (self.x + 17, self.y + 2, 31, 57)
            #pygame.draw.rect(win, (255, 0, 0), self.hitBox, 2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False


def redrawGameWindow():
    win.blit(bg, (0, 0))
    text = font.render('Score: ' + str(score), 1, BLACK)
    win.blit(text, (350, 10))
    man.draw(win)
    enemy.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


##Main loop
font = pygame.font.SysFont('comicsans', 30, True)
bullets = []
man = Player(10, 410, 64, 64)
enemy = Enemy(50, 410, 64, 64, 450)
shootLoop = 0
run = True
while run:
    clock.tick(27)

    if enemy.visible:
        if man.hitBox[1] < enemy.hitBox[1] + enemy.hitBox[3] and man.hitBox[1] + man.hitBox[3] > enemy.hitBox[1]:
            if man.hitBox[0] + man.hitBox[2] > enemy.hitBox[0] and man.hitBox[0] < enemy.hitBox[0] + enemy.hitBox[2]:
                man.hit()
                score = 0
                #hitCount += 1

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if enemy.visible:
            if bullet.y - bullet.radius < enemy.hitBox[1] + enemy.hitBox[3] and bullet.y + bullet.radius > enemy.hitBox[1]:
                if bullet.x + bullet.radius > enemy.hitBox[0] and bullet.x - bullet.radius < enemy.hitBox[0] + enemy.hitBox[2]:
                    #hitSound.play()
                    enemy.hit()
                    score += 1
                    bullets.pop(bullets.index(bullet))

        if 0 < bullet.x < 500:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    ### Keys movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        #bulletSound.play()
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(Bullets(round(man.x + man.width//2), round(man.y + man.height//2), 6, (255, 0, 0), facing))

        shootLoop = 1
    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0
    if not man.isJump:
        if keys[pygame.K_UP]:
            man.isJump = True
            man.walkCount = 0

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
