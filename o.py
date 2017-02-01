import pygame
from pygame import *
import sys
import pygame.mixer


ktory=1
plansza1 = pygame.image.load("/home/klaudia/PycharmProjects/nechee/mapa1.png")
plansza2 = pygame.image.load("/home/klaudia/PycharmProjects/nechee/mapa2.png")
plansza3 = pygame.image.load("/home/klaudia/PycharmProjects/nechee/mapa3.png")
screen = pygame.display.set_mode((1000, 1000))
black = (0, 0, 0)
zycie = 3
poziom = 1

level = ["WWWWWWWWWWWWWWWWWWWW",
         "W                 RW",
         "W           WWWWWWWW",
         "W  B  B            W",
         "W WWWWWWW          W",
         "W           WB     W",
         "W            W    BW",
         "W                 WW",
         "W      B           W",
         "W     WW     WW    W",
         "WB                 W",
         "WWWW               W",
         "W     WWW     B    W",
         "W            WWW   W",
         "W     B            W",
         "W     WWWWW        W",
         "W                  W",
         "W             W    W",
         "W    BB      B  B  W",
         "WW  WWWW  WWWWWWWWWW"]
level2 = ["WWWWWWWWWWWWWWWWWWWW",
          "W                 RW",
          "W     W  B       WWW",
          "W        W         W",
          "W             W    W",
          "W                B W",
          "W       B        W W",
          "W       W     W    W",
          "W                  W",
          "W    W             W",
          "W      B           W",
          "W      W    W      W",
          "W                  W",
          "W              W   W",
          "W           B      W",
          "W           W      W",
          "W   W              W",
          "W       W          W",
          "W   B        B  B  W",
          "WW  W  W  W  W  W  W"]
level3 = ["WWWWWWWWWWWWWWWWWWWW",
          "W                 RW",
          "W                 WW",
          "W     B          WWW",
          "W          WW      W",
          "W      B           W",
          "W      WWW         W",
          "W                  W",
          "W            W     W",
          "W        B        BW",
          "W   WW   WW    WWWWW",
          "WW                 W",
          "WB                 W",
          "WWWW               W",
          "W      WW    B     W",
          "W            W     W",
          "W                B W",
          "W       B        WWW",
          "W      WW   WW     W",
          "WWW                W"]

kotImg1 = pygame.image.load('/home/klaudia/PycharmProjects/nechee/kot1.png')
kotImg11 = pygame.image.load('/home/klaudia/PycharmProjects/nechee/kot11.png')
kotImg2 = pygame.image.load('/home/klaudia/PycharmProjects/nechee/kot2.png')
kotImg22= pygame.image.load('/home/klaudia/PycharmProjects/nechee/kot22.png')
punktImg = pygame.image.load('/home/klaudia/PycharmProjects/nechee/bonus.png')

platformaImg1 = pygame.image.load('/home/klaudia/PycharmProjects/nechee/blok1.png')
platformaImg2 = pygame.image.load('/home/klaudia/PycharmProjects/nechee/blok2.png')
platformaImg3 = pygame.image.load('/home/klaudia/PycharmProjects/nechee/blok33.png')
pygame.mixer.init()


ryba = pygame.image.load('/home/klaudia/PycharmProjects/nechee/ryba.png')
SerceImg =pygame.image.load('/home/klaudia/PycharmProjects/nechee/serce.gif')
batImg=pygame.image.load('/home/klaudia/PycharmProjects/nechee/bat.gif')


class Kot(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.dx = 0
        self.dy = 0
        self.ziemia= False

        self.image = kotImg1

        self.rect = self.image.get_rect()

        self.rect.left = x
        self.rect.top = y
        self.kroki = 1
        self.pu =0

    def chodzi(self, gora, lewo, prawo, platforms, punkty, wszystko):
        if poziom == 1:

            if lewo:
                self.kroki=self.kroki+1
                if self.kroki%4 ==0:
                    self.image = kotImg2
                else:
                    self.image = kotImg22
                self.dx = -5

            if prawo:
                self.kroki = self.kroki + 1
                if self.kroki % 4 == 0:
                    self.image = kotImg1
                else:
                    self.image = kotImg11
                self.dx = 5

            if gora:
                if self.ziemia:
                    self.dy = -10
            if not self.ziemia:
                self.dy += .5
            if not (lewo or prawo):
                self.dx = 0

            self.rect.left += self.dx
            self.kolizja1(self.dx, 0, platforms,punkty,wszystko)

            self.rect.top += self.dy
            self.ziemia = False
            self.kolizja1(0, self.dy, platforms,punkty,wszystko)

            if self.rect.top >1000:
                pygame.mixer.music.load(open("/home/klaudia/PycharmProjects/nechee/bum.wav"))
                pygame.mixer.music.play()
                self.rect.left = 50
                self.rect.top = 950

        else:
            pass
    def kolizja1(self, dx, dy, platforms, punkty,wszystko):

        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if dx > 0:
                    self.rect.right = p.rect.left
                if dx < 0:
                    self.rect.left = p.rect.right
                if dy > 0:
                    self.rect.bottom = p.rect.top
                    self.ziemia= True
                    #self.yv = 0
                if dy < 0:
                    self.rect.top = p.rect.bottom
        for x in punkty:
            if pygame.sprite.collide_rect(self, x):
                print self.pu
                self.pu = self.pu + 1
                pygame.mixer.music.load(open("/home/klaudia/PycharmProjects/nechee/ml.wav"))
                pygame.mixer.music.play()
                punkty.remove(x)
                wszystko.remove(x)

class Bat(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)

        self.image=batImg

        self.rect=self.image.get_rect()

        self.rect.left = x
        self.rect.top = y
        self.dx = 5

    def chodzi(self):
        self.rect.left+=self.dx
        if self.rect.left > 1000:
            self.rect.left = x
            self.rect.top = 100

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y,poziom):
        pygame.sprite.Sprite.__init__(self)

        if poziom ==1:
            self.image = platformaImg1
        if poziom ==2:
            self.image = platformaImg2
        if poziom ==3:
            self.image = platformaImg3

        self.rect = self.image.get_rect()
        self.rect = Rect(x, y, 50, 50)

    def update(self):
        pass

class Ryba(pygame.sprite.Sprite):

    def __init__(self,x,y):

        pygame.sprite.Sprite.__init__(self)
        self.image = ryba
        self.rect = self.image.get_rect()
        self.rect = Rect(x, y, 30, 30)

    def update(self):
        pass

class Mleko(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = punktImg
        self.rect = self.image.get_rect()
        self.rect = Rect(x, y, 30, 30)
    def update(self):
        pass

class Serce(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = SerceImg
        self.rect = self.image.get_rect()
        self.rect = Rect(x, y, 50, 50)
    def update(self):
        pass

def poziom1(zy):
    start = True
    gora = lewo = prawo = False
    bg = Surface((50, 50))
    bg.convert()
    bg.fill(black)
    gracz = Kot(50, 950)
    baat=Bat(50,100)

    bat =[]
    rybaa = []
    platforms = []
    punkty = []
    serce = []

    allSprites = pygame.sprite.Group(gracz)
    bSprites = pygame.sprite.Group()
    bat.append(baat)
    allSprites.add(baat)


    x = y = 0
    for row in level:
        for col in row:
            if col == "W":
                p = Platform(x, y,1)
                platforms.append(p)
                allSprites.add(p)
            if col == "B":
                m = Mleko(x, y)
                punkty.append(m)
                allSprites.add(m)
            if col == "R":
                m = Ryba(x, y)
                print x
                print y
                rybaa.append(m)
                allSprites.add(m)
            x += 50
        y += 50
        x = 0

    j = Serce(50, 50)
    serce.append(j)
    allSprites.add(j)

    d = Serce(100, 50)
    serce.append(d)
    allSprites.add(d)

    t = Serce(150, 50)
    serce.append(t)
    allSprites.add(t)

    while start == True:

        for e in pygame.event.get():
            if e.type == KEYDOWN:
                if e.key == K_UP:
                    gora = True
                    pygame.mixer.music.load(open("/home/klaudia/PycharmProjects/nechee/skok.wav"))
                    pygame.mixer.music.play()

                if e.key == K_LEFT:
                    lewo = True

                if e.key == K_RIGHT:
                    prawo = True

                if e.key == 27:
                    pygame.quit()
                    sys.exit()

            if e.type == KEYUP:
                if e.key == K_UP:
                    gora = False
                if e.key == K_RIGHT:
                    prawo = False
                if e.key == K_LEFT:
                    lewo = False

            if gracz.rect.left > 850 and gracz.rect.top == 50 and gracz.pu ==12:
                start = False
                pygame.mixer.music.load(open("/home/klaudia/PycharmProjects/nechee/ry.wav"))
                pygame.mixer.music.play()
            for z in bat:
                if pygame.sprite.collide_rect(gracz, z):
                    if e.type == KEYUP:
                        if e.key == K_UP:
                            gora = False
                        if e.key == K_RIGHT:
                            prawo = False
                        if e.key == K_LEFT:
                            lewo = False
                    gracz.rect.left = 50
                    gracz.rect.top= 950



        for y in range(32):
            for x in range(32):
                screen.blit(bg, (x * 32, y * 32))

        allSprites.clear(screen, bg)
        bSprites.clear(screen, bg)
        screen.blit(plansza1, (0, 0))

        if gracz.rect.top == 950:
            zy = zy - 1
            print zy
            if zy == 2:
                allSprites.remove(t)
                serce.remove(t)
            if zy == 1:
                allSprites.remove(d)
                serce.remove(d)
            if zy == 0:
                start = False

        baat.chodzi()
        gracz.chodzi(gora, lewo, prawo, platforms, punkty, allSprites)

        bSprites.update()
        allSprites.draw(screen)
        bSprites.draw(screen)
        pygame.display.flip()
        pygame.display.update()
        pygame.display.flip()

    if start == False:
        poziom2(zy+1)

def poziom2(zyc):
    gora = lewo = prawo = False

    bg = Surface((50, 50))
    bg.convert()

    bg.fill(black)
    gracz = Kot(50, 950)
    rybaa = []
    platforms = []
    punkty = []
    serce=[]
    start = 1

    allSprites = pygame.sprite.Group(gracz)
    bSprites = pygame.sprite.Group()

    j = Serce(50, 50)
    serce.append(j)
    allSprites.add(j)

    d = Serce(100, 50)
    serce.append(d)
    allSprites.add(d)

    t = Serce(150, 50)
    serce.append(t)
    allSprites.add(t)
    x = y = 0

    for row in level2:
        for col in row:
            if col == "W":
                p = Platform(x, y,2)
                platforms.append(p)
                allSprites.add(p)
            if col == "B":
                m = Mleko(x, y)
                punkty.append(m)
                allSprites.add(m)
            if col == "R":
                m = Ryba(x, y)
                rybaa.append(m)
                allSprites.add(m)
            x += 50
        y += 50
        x = 0

    while start == 1:
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit()

            if e.type == KEYDOWN:
                if e.key == K_UP:
                    gora = True
                    pygame.mixer.music.load(open("/home/klaudia/PycharmProjects/nechee/skok.wav"))
                    pygame.mixer.music.play()
                if e.key == K_LEFT:
                    lewo = True
                if e.key == K_RIGHT:
                    prawo = True

                if e.key == 27:
                    pygame.quit()
                    sys.exit()

            if e.type == KEYUP:
                if e.key == K_UP:
                   gora = False
                if e.key == K_RIGHT:
                    prawo= False
                if e.key == K_LEFT:
                    lewo= False

            if gracz.rect.left > 850 and gracz.rect.top == 50 and gracz.pu ==8:
                pygame.mixer.music.load(open("/home/klaudia/PycharmProjects/nechee/ry.wav"))
                pygame.mixer.music.play()
                start = False

        for y in range(32):
            for x in range(32):
                screen.blit(bg, (x * 32, y * 32))

        allSprites.clear(screen, bg)
        bSprites.clear(screen, bg)
        screen.blit(plansza2, (0, 0))

        if gracz.rect.top == 950:
            zyc = zyc - 1
            print zyc
            if zyc == 2:
                allSprites.remove(t)
                serce.remove(t)
            if zyc == 1:
                allSprites.remove(d)
                serce.remove(d)
            if zyc == 0:
                start = False

        gracz.chodzi(gora, lewo, prawo, platforms, punkty, allSprites)

        bSprites.update()
        allSprites.draw(screen)
        bSprites.draw(screen)
        pygame.display.flip()
        pygame.display.update()
        pygame.display.flip()
        if start == False:
            poziom3(zyc+1)

def poziom3(zyci):
    start = True
    gora = lewo = prawo = False

    bg = Surface((50, 50))
    bg.convert()

    bg.fill(black)

    gracz = Kot(50, 950)
    rybaa = []
    platforms = []
    punkty = []
    serce = []

    allSprites = pygame.sprite.Group(gracz)
    bSprites = pygame.sprite.Group()
    j = Serce(50, 50)
    serce.append(j)
    allSprites.add(j)

    d = Serce(100, 50)
    serce.append(d)
    allSprites.add(d)

    t = Serce(150, 50)
    serce.append(t)
    allSprites.add(t)

    x = y = 0
    for row in level3:
        for col in row:
            if col == "W":
                p = Platform(x, y,3)
                platforms.append(p)
                allSprites.add(p)
            if col == "B":
                m = Mleko(x, y)
                punkty.append(m)
                allSprites.add(m)
            if col == "R":
                m = Ryba(x, y)
                print x
                print y
                rybaa.append(m)
                allSprites.add(m)
            x += 50
        y += 50
        x = 0

    while start == True:

        for e in pygame.event.get():
            if e.type == KEYDOWN:
                if e.key == K_UP:
                    gora = True
                    pygame.mixer.music.load(open("/home/klaudia/PycharmProjects/nechee/skok.wav"))
                    pygame.mixer.music.play()
                if e.key == K_LEFT:
                    lewo = True

                if e.key == K_RIGHT:
                    prawo = True

                if e.key == 27:
                    pygame.quit()
                    sys.exit()

            if e.type == KEYUP:
                if e.key == K_UP:
                    gora = False
                if e.key == K_RIGHT:
                    prawo = False
                if e.key == K_LEFT:
                    lewo = False

                if gracz.rect.left > 850 and gracz.rect.top == 50 and gracz.pu==8:
                    pygame.mixer.music.load(open("/home/klaudia/PycharmProjects/nechee/ry.wav"))
                    pygame.mixer.music.play()
                    start = False

        for y in range(32):
            for x in range(32):
                screen.blit(bg, (x * 32, y * 32))

        allSprites.clear(screen, bg)
        bSprites.clear(screen, bg)
        screen.blit(plansza3, (0, 0))
        if gracz.rect.top == 950:
            zyci = zyci - 1
            print zyci
            if zyci == 2:
                allSprites.remove(t)
                serce.remove(t)
            if zyci == 1:
                allSprites.remove(d)
                serce.remove(d)
            if zyci == 0:
                start = False
        gracz.chodzi(gora, lewo, prawo, platforms, punkty, allSprites)

        bSprites.update()
        allSprites.draw(screen)
        bSprites.draw(screen)
        pygame.display.flip()
        pygame.display.update()
        pygame.display.flip()

while True:
    zycie = 4
    screen.fill((255, 255, 255))
    y = pygame.image.load("/home/klaudia/PycharmProjects/nechee/menu.png")
    screen.blit(y, (0, 0))
    while zycie > 0:

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                running = False

        screen.fill((255,255,255))
        y = pygame.image.load("/home/klaudia/PycharmProjects/nechee/menu.png")
        screen.blit(y,(0,0))
        key = pygame.key.get_pressed()

        if key[pygame.K_s]:
            x = 0
            if x == 0:
                poziom1(zycie)

        pygame.display.flip()

