import pygame as pg
import math
import random

# Initialize Pygame
pg.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Physics Simulation")

# Set up clock for FPS
clock = pg.time.Clock()
FPS = 60

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # ...draw/update simulation here...

    pg.display.flip()
    clock.tick(FPS)

pg.quit()


