#Create your own shooter

import pygame as gm
from random import randint

class Gamesprite(gm.sprite.Sprite):
    def __init__(self, img, x, y, width, height, speed):
        gm.sprite.Sprite.__init__(self)
        self.img = gm.transform.scale(gm.image.load(img), (width, height))
        self.image = gm.transform.scale(gm.image.load(img), (width, height))
        self.speed = speed
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        mw.blit(self.img, (self.rect.x, self.rect.y))

class player (Gamesprite):
    def update(self):
        keys = gm.key.get_pressed()
        if keys[gm.K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[gm.K_RIGHT] and self.rect.x < 420:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet ("bullet.png", self.rect.centerx, self.rect.top, 15, 20, -10)
        bullets.add(bullet)

class Enenmy (Gamesprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 500:
            self.rect.x = randint(80, 620)
            self.rect.y = 0
            lost += 1


class Bullet(Gamesprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y <0:
            self.kil()

rocket = player("rocket.png", 5, 400, 80, 100, 10)
monsters = gm.sprite.Group()
for i in range(1, 6):
    monster = Enenmy("ufo.png", randint(80, 620), 0, 80, 50, randint(1, 5))
    monsters.add (monster)





gm.init()
mw = gm.display.set_mode((700, 500))
gm.display.set_caption("Shooter game")
bg = gm.transform.scale(gm.image.load("galaxy.jpg"), (700, 500))
fps = gm.time.Clock()

gm.mixer.init()
gm.mixer.music.load("space.ogg")
gm.mixer.music.set_volume(0.1)
gm.mixer.music.play(loops=True)
finish = False
score = 0
lost = 0




bullets = gm.sprite.Group()
gm.font.init()
font1 = gm.font.Font(None, 80)
win = font1.render("YOU WIN!", True, (255, 255, 255))
lose = font1.render("YOU LOSE!", True, (180, 0, 0))



while True:
    for e in gm.event.get():
        if e.type == gm.QUIT:
            break

        elif e.type == gm.KEYDOWN:
            if e.key == gm.K_SPACE:
                sound = gm.mixer.Sound("fire.ogg")
                sound.play()
                rocket.fire()


    if not finish:
            mw.blit(bg, (0,0))
            rocket.update()
            rocket.reset()
            monsters.draw(mw)
            monsters.update()
            bullets.update()
            bullets.draw(mw)
            gm.font.init()
            font2 = gm.font.Font(None, 36)
            missed = font2.render(f"Missed: {lost}", 1, gm.Color("white"))
            mw.blit(missed, (10, 50))
            scored = font2.render(f"Score: {score}", 1, gm.Color("white"))
            mw.blit(scored, (10, 20))
            
            collides = gm.sprite.groupcollide(monsters, bullets, True, True)
            for c in collides:
                score += 1
                monster = Enenmy("ufo.png", randint(80, 620), 0, 80, 50, randint (1, 5))
                monsters.add (monster)

            if gm.sprite.spritecollide(rocket, monsters, False) or lost >= 5:
                finish = True
                game = "lose"

            if score >= 10: 
                finish = True
                game = "win"


    else:
        if game == "win":
            mw.blit(win, (200, 200))
        else: 
            mw.blit(lose, (200, 200))

    gm.display.update()
    fps.tick(60)