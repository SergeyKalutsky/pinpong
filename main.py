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


class Pokemon(GameSprite):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        self.speed = 3

    def update(self):
        self.rect.x += self.speed
        if self.speed > 0 and self.rect.x > WIDTH - 350:
            self.speed *= -1
        if self.speed < 0 and self.rect.x < 200:
            self.speed *= -1


class Arrow():
    def __init__(self, w, h, x, y, color):
        self.rect = pg.Rect(w, h, x, y)
        self.speed = 5
        self.count = 0
        self.side = True
        self.color = color

    def draw(self):
        pg.draw.rect(screen, self.color, self.rect)

    def update(self):

        if self.count <= 0:
            self.count = randint(0, 2) * 60
        if self.count > 0:
            self.count -= 1

        if self.side and self.rect.y > 50:
            self.side -= self.speed
        elif not self.side and self.rect.y < 550:
            self.side += self.speed


bg = GameSprite('background.png', 0, 0)
ball = GameSprite('ball.png', 450, 450)
pokemons = os.listdir("pokemons")
pokemon = Pokemon(f'pokemons\{choice(pokemons)}', 450, 50)

aqua_arrow = Arrow(100, 50, 40, 500, 'aqua')
player_arrow = Arrow(100, randint(50, 500-70), 40, 70, 'orange')


while True:
    bg.draw()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    ball.draw()
    aqua_arrow.draw()

    pokemon.update()
    pokemon.draw()

    player_arrow.update()
    player_arrow.draw()

    pg.display.update()
    clock.tick(FPS)
