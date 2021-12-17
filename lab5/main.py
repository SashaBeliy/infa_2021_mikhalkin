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
FPS = 30
width = 1200
height = 900
border = 100
ball_max_rad = 100
num_of_balls = 3
num_of_imposters = 3
imposter_speed_multiplier = 1/200
time_limit = 2000

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

def imposter_make():
    x = randint(border, width - border)
    y = randint(border, height - border)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    return [x, y, r, color]


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

def imposters_move():
    '''
    '''
    for imposter in imposters:
        vx = pygame.mouse.get_pos()[0] - imposter[0]
        vy = pygame.mouse.get_pos()[1] - imposter[1]
        imposter[0] += vx * imposter_speed_multiplier
        imposter[1] += vy * imposter_speed_multiplier
        circle(screen, imposter[3], (imposter[0], imposter[1]), imposter[2])



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
            imposters[randint(0,num_of_imposters-1)] = imposter_make()
            SCORE += 1
    for i in range(num_of_imposters):
        if (imposters[i][0] - click_pos[0])**2 + (imposters[i][1] - click_pos[1])**2 <= imposters[i][2]**2:
            SCORE -= 1



pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.update()
clock = pygame.time.Clock()
finished = False
balls = [ball_make() for _ in range(num_of_balls)]
imposters = [imposter_make() for _ in range(num_of_imposters)]
SCORE = 0

while not finished:
    clock.tick(FPS)
    play_time = pygame.time.get_ticks()
    if time_limit - play_time <= 0:
        finished = True
        print('Your score: ', SCORE)
        break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            print('Your score: ', SCORE)
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_process(event.pos)
    balls_move()
    imposters_move()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
records = open("records.txt", "r+")
lines = []
record_written = False
new_record = str(input("Enter your nickname to record a score:")) + " " + str(SCORE)
for line in records.readlines():
    if int(line.split()[2]) < SCORE and not record_written:
        lines.append(new_record + "\n")
        record_written = True
    lines.append(line.split(" ", 1)[1])
records.seek(0)
records.truncate()
for line in lines:
    records.write(str(lines.index(line)+1) + " " + line)
if not record_written:
    records.write(str(len(lines)+1) + " " + new_record + "\n")
records.close()
