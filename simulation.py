import pygame as pg
import math
import random
from Ball import Ball
from Dropper import Dropper

# Initialize Pygame
pg.init()

# Set up display
WIDTH, HEIGHT = 540, 960
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Physics Simulation")

# Set up clock for FPS
clock = pg.time.Clock()
FPS = 60

# Lists of balls
balls = []
dropped_balls = []

# Colors
white = (255, 255, 255)


# Ball settings
number_of_balls = 10
radius_of_balls = 10
color_of_balls = white


# Generate Balls using ball settings
for i in range(number_of_balls):
    new_ball = Ball(
        x= WIDTH //2,
        y= HEIGHT //2,
        xv=0,
        yv=0,
        radius=radius_of_balls,
        color=color_of_balls
    )

    # append all the new balls to the "undropped_balls" list
    balls.append(new_ball)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # PHYSICS SIM

    for ball in dropped_balls:
        ball.update()
        # Draw the ball
        pg.draw.circle(screen, ball.color, (int(ball.x), int(ball.y)), ball.radius)























    pg.display.flip()
    clock.tick(FPS)

pg.quit()


