import pygame

plansza = pygame.image.load("/home/klaudia/PycharmProjects/nechee/mapa3.png")

class Bonus(object):
    def __init__(self, pos):
        bonusy.append(self)
        self.rect = pygame.Rect(pos[0],pos[1],30, 30)
    def rysu(self, kobraz, x):
        self.bonus = pygame.image.load("/home/klaudia/PycharmProjects/nechee/bonus.png")
        kobraz.blit(self.bonus, (x))
    def kk(self,kobraz):
        kobraz.fill((0,0,0))

class Gracz(object):
    def __init__(self):
        self.rect = pygame.Rect(50, 900, 50, 50)
    def move(self, dx, dy):
        if dx != 0:
            self.kolizja(dx, 0)
        if dy != 0:
            self.kolizja(0, dy)
    def rysu(self,kobraz,x):
        #kobraz.fill(0)
        self.kot = pygame.image.load("/home/klaudia/PycharmProjects/nechee/kot.png")
        kobraz.blit(self.kot, (x))
    def kolizja(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

        for blok in bloki:
            if self.rect.colliderect(blok.rect):
                if dx > 0:
                    self.rect.right = blok.rect.left
                if dx < 0:
                    self.rect.left = blok.rect.right
                if dy > 0:
                    self.rect.bottom = blok.rect.top
                if dy < 0:
                    self.rect.top = blok.rect.bottom

        for bonus in bonusy:
            if self.rect.colliderect(bonus.rect):
                if dx > 0:
                    bonus.delete()
                if dx < 0:
                    bonus.fill()
                if dy > 0:
                    bonus.fill()
                if dy < 0:
                    bonus.fill()
class Blok(object):

    def __init__(self, pos):
        bloki.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 50, 50)
    def rysu(self,kobraz,x):
        self.blok = pygame.image.load("/home/klaudia/PycharmProjects/nechee/plansza3.png")
        kobraz.blit(self.blok, (x))

screen = pygame.display.set_mode((1000, 1000))

clock = pygame.time.Clock()
bloki = []
bonusy = []
gracz = Gracz()
level = ["WWWWWWWWWWWWWWWWWWWW",
         "W                  W",
         "W            WWWW  W",
         "W                  W",
         "W WWWWWWW   W      W",
         "W                  W",
         "W                  W",
         "W                  W",
         "W      WWW         W",
         "W                  W",
         "W                  W",
         "W                  W",
         "W                  W",
         "W                  W",
         "W                  W",
         "W     WWWWW        W",
         "W                  W",
         "WWWWWW             W",
         "W                  W",
         "WWWWWWWWWWWWWWWWWWWW"]
x = y = 0
for w in level:
    for kol in w:
        if kol == "W":
            Blok((x, y))
        if kol == "B":
            Bonus((x,y))
        x += 50
    y += 50
    x = 0

running=True
while running:

    clock.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        gracz.move(-5, 0)
    if key[pygame.K_RIGHT]:
        gracz.move(5, 0)
    if key[pygame.K_UP]:
        gracz.move(0, -5)
    if key[pygame.K_DOWN]:
        gracz.move(0, 5)
    if key[pygame.K_SPACE]:
        gracz.move(0,50)
        for x in range(1,50):
         gracz.move(0,-1)


    screen.fill((0, 0, 0))
    screen.blit(plansza, (0, 0))
    for blok in bloki:
        blok.rysu(screen, blok.rect)
    for bonus in bonusy:
        bonus.rysu(screen,bonus.rect)


    gracz.rysu(screen,gracz.rect)
    pygame.display.flip()