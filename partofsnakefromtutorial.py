#snake game from Edureka blog
import time
import pygame
pygame.init()

#set up window
window_width = 400
window_height = 300
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake game')

#set up variables
black = (0,0,0)
green = (0,255,0)
red = (255,0,0)
game_over = False
x1 = window_width/2
y1 = window_height/2
x1change = 0
y1change = 0

clock = pygame.time.Clock()
snake_speed = 30

font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [10, 10])

#game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1change = -10
                y1change = 0
            elif event.key == pygame.K_RIGHT:
                x1change = 10
                y1change = 0
            elif event.key == pygame.K_UP:
                x1change = 0
                y1change = -10
            elif event.key == pygame.K_DOWN:
                x1change = 0
                y1change = 10
    if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0: 
        game_over = True

    x1 += x1change
    y1 += y1change
    window.fill(black)
    pygame.draw.rect(window, green, [x1,y1,10,10])

    pygame.display.update()
    clock.tick(snake_speed)

message("You lost", red)
pygame.display.update()
time.sleep(1)
pygame.quit()
quit()