import pygame
import random

WIDTH = 1360
HEIGHT = 725
FPS = 60
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

pygame.init()
pygame.mixer.init()

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shamup!")
clock = pygame.time.Clock()

bg_img = pygame.image.load('Background-4.png')
bg_rect = bg_img.get_rect()
bullet_img = pygame.image.load('laserRed16.png')
meteor_img = pygame.image.load('meteorBrown_med1.png')
player_img = pygame.image.load('player_img.png')


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speedx = -10
        if keys[pygame.K_RIGHT]:
            self.speedx = 10

        self.rect.x += self.speedx
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites_list.add(bullet)
        bullets.add(bullet)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = meteor_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


# for all player and mobs to check collision
all_sprites_list = pygame.sprite.Group()

# for mobs only
mobs = pygame.sprite.Group()

# bullets only
bullets = pygame.sprite.Group()

player = Player()

all_sprites_list.add(player)

for i in range(8):
    enemy = Enemy()
    all_sprites_list.add(enemy)
    mobs.add(enemy)

shootLoop = 0

score = 0

run = True

while run:

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if shootLoop > 3:
        shootLoop = 0
    else:
        shootLoop += 1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and shootLoop == 0:
        player.shoot()
    # update section

    all_sprites_list.update()

    hit_list = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hit_list:
        m = Enemy()
        all_sprites_list.add(m)
        mobs.add(m)
        score += 5

    # check to see if mobs hit the player
    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        run = False

    win.fill(black)
    win.blit(bg_img, bg_rect)
    all_sprites_list.draw(win)
    font = pygame.font.SysFont('comicsans', 30, True)
    text = font.render('Score: ' + str(score), 1, (255, 0, 0))
    win.blit(text, (WIDTH - 200, 50))
    pygame.display.flip()

pygame.quit()
