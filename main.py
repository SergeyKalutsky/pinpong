import pygame as pg
import sys

FPS = 60
pg.init()
pg.font.init()

screen = pg.display.set_mode((1070, 600))
clock = pg.time.Clock()

class GameSprite(pg.sprite.Sprite):
    def __init__(self, image, x, y):
        self.image = pg.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

bg = GameSprite('background.png', 0, 0)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            
    bg.draw()  
    pg.display.update()
    clock.tick(FPS)