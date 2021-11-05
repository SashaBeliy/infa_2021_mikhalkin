import pygame
from pygame.draw import *
from random import randint

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
FPS = 10
width = 1200
height = 900
border = 100
ball_max_rad = 100
num_of_balls = 3

def ball_make():
    '''creates parameters of a new ball

    Returns:
    --------
    list
        a list of ball's parameters:
            x: int - horizontal coordinate of ball's center
            y: int - vertical coordinate of ball's center
            r: int - ball's radius
            vx: int - how much ball moves in x+ direction with each frame change
            vy: int - how much ball moves in y+ direction with each frame change
            color: tuple - RGB color of the ball

    '''
    x = randint(border, width - border)
    y = randint(border, height - border)
    r = randint(10, 100)
    vx = randint(-10,10)
    vy = randint(-10,10)
    color = COLORS[randint(0, 5)]
    return [x, y, r, vx, vy, color]

def balls_move():
    '''draws the next frame of moving balls
    '''
    for ball in balls:
        if ball[0] < border or ball[0] > (width - border):
            ball[3] = - ball[3]
        if ball[1] < border or ball[1] > (height - border):
            ball[4] = - ball[4]
        ball[0] += ball[3]
        ball[1] += ball[4]
        circle(screen, ball[5], (ball[0], ball[1]), ball[2])

def click_process(click_pos):
    '''processess mouse clicks

    Parameters
    --------
    click_pos: tuple
        Click coordinates
    '''
    global SCORE
    for i in range(num_of_balls):
        if (balls[i][0] - click_pos[0])**2 + (balls[i][1] - click_pos[1])**2 <= balls[i][2]**2:
            balls[i] = ball_make()
            SCORE += 1



pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.update()
clock = pygame.time.Clock()
finished = False
balls = [ball_make() for _ in range(num_of_balls)]
SCORE = 0

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            print('Your score: ', SCORE)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_process(event.pos)

    balls_move()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
