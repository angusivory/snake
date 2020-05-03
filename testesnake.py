#snake game from Edureka blog
import random
import time
import pygame
pygame.init()

#set up window
window_width = 400
window_height = 350
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake game')

#define constant variables

black = (0,0,0)
green = (0,255,0)
blue = (0,0,255)
red = (255,0,0)


def gameLoop():
    #define variables that are reset for each game
    score = 0
    game_over = False
    game_close = False
    x1 = window_width/2
    y1 = 150
    x1change = 0
    y1change = 0
    direction = ""  #in snake you cannot do a U-turn!
    newpos = True
    clock = pygame.time.Clock()
    snake_speed = 20

    #put text on the screen
    font_style = pygame.font.SysFont(None, 50)
    def message(msg, color, msgx, msgy):
        mesg = font_style.render(msg, True, color)
        window.blit(mesg, [msgx, msgy])

    #event loop
    while not game_over:

        while game_close == True:
            #game over: display stats
            window.fill(black)
            if score == 1:
                message("You scored {} point".format(score), blue, 0, 300)
            else:
                message("You scored {} points".format(score), blue, 0, 300)
            message("Game over", red, 0, 10)
            message("Press Q to quit or C to play again", red, 0, 60)
            pygame.display.update()
            #HIGHSCORE FUNCTION - save highscore between runs (and an all time leaderboard via a separate document???)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not direction == "right":
                        x1change = -10
                        y1change = 0
                        direction = "left"
                elif event.key == pygame.K_RIGHT:
                    if not direction == "left":
                        x1change = 10
                        y1change = 0
                        direction = "right"
                elif event.key == pygame.K_UP:
                    if not direction == "down":
                        x1change = 0
                        y1change = -10
                        direction = "up"
                elif event.key == pygame.K_DOWN:
                    if not direction == "up":
                        x1change = 0
                        y1change = 10
                        direction = "down"
        #position apple
        if newpos == True:
            applex = random.randint(0, window_width-10)
            applex = round(applex/10) * 10
            appley = random.randint(0, window_height-60)
            appley = round(appley/10) * 10
            newpos = False

        x1 += x1change
        y1 += y1change
        window.fill(black)

        #check if snake is outside of game area
        if x1 >= window_width or x1 < 0 or y1 >= (window_height-50) or y1 < 0: 
            game_close = True
        
        if x1 == applex and y1 == appley:
            newpos = True
            score += 1
            #display a message saying "yum" somehow - it isn't working :()

        pygame.draw.rect(window, (255,0,0), [applex, appley, 10, 10])
        pygame.draw.rect(window, green, [x1,y1,10,10])
        #display score
        pygame.draw.rect(window, (255,255,255,), [0,300,400,50])
        message("Score: {}".format(score), blue, 0, 300)

        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()