from random import choice, randint
import pygame as pg
import sys
import os


FPS = 60
pg.init()
pg.font.init()

WIDTH, HEIGHT = 1070, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
pg.display.set_caption("Pokemon")


class GameSprite(pg.sprite.Sprite):
    def __init__(self, image, x, y):
        self.image = pg.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Ball(GameSprite):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        self.limit = 60
        self.x = x 
        self.direction = 'right'

    def update(self):
        self.rect.y -= 1
        if self.direction == 'right':
            self.rect.x += 4
            if self.rect.x >= self.x + self.limit:
                self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= 4
            if self.rect.x <= self.x - self.limit:
                self.direction = 'right'


class Pokemon(GameSprite):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        self.speed = 5

    def update(self):
        self.rect.x += self.speed
        if self.speed > 0 and self.rect.x > WIDTH - 350:
            self.speed *= -1
        if self.speed < 0 and self.rect.x < 200:
            self.speed *= -1

    def decrease_speed(self):
        if self.speed > 0:
            self.speed -= 1
        if self.speed < 0:
            self.speed += 1

    def increase_speed(self):
        if self.speed > 0:
            self.speed += 1
        if self.speed < 0:
            self.speed -= 1


class Arrow():
    def __init__(self, x, y, w, h, color):
        self.rect = pg.Rect(x, y, w, h)
        self.speed = 5
        self.count = 0
        self.side = True
        self.color = color

    def draw(self):
        pg.draw.rect(screen, self.color, self.rect)


class Bar(Arrow):
    def __init__(self, x, y, w, h, color):
        super().__init__(x, y, w, h, color)
        self.speed = 3
        self.h = h

    def update(self):
        self.rect.y += self.speed
        if self.speed > 0 and self.rect.y >= 550 - self.h:
            self.speed *= -1
        if self.speed < 0 and self.rect.y <= 50:
            self.speed *= -1

    def decrease_speed(self):
        if self.speed > 1:
            self.speed -= 1
        if self.speed < -1:
            self.speed += 1

    def increase_speed(self):
        if self.speed > 0:
            self.speed += 1
        if self.speed < 0:
            self.speed -= 1


bg = GameSprite('background.png', 0, 0)
ball = Ball('ball.png', 450, 450)
pokemons = os.listdir("pokemons")
pokemon = Pokemon(f'pokemons\{choice(pokemons)}', 450, 50)

aqua_arrow = Arrow(100, 50, 40, 500, 'aqua')
player_arrow = Arrow(100, randint(50, 500-70), 40, 70, 'orange')
bar = Bar(80, 150, 80, 15, 'black')


while True:
    bg.draw()
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                if player_arrow.rect.colliderect(bar.rect):
                    pokemon.decrease_speed()
                    bar.increase_speed()
                    player_arrow.rect.y = randint(50, 500-70)
                else:
                    bar.decrease_speed()
                    pokemon.increase_speed()
        if event.type == pg.QUIT:
            sys.exit()

    ball.draw()
    aqua_arrow.draw()
    bar.update()
    ball.update()
    pokemon.update()
    pokemon.draw()

    player_arrow.draw()
    bar.draw()

    pg.display.update()
    clock.tick(FPS)
