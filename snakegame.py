#snake game from Edureka blog
import random
import time
import pygame
pygame.init()


#define constant variables
                                    #blocklength = 0         #ADD A PROCEDURE to ask the user if they want big snake or small snake. Choose skin colour as well???
white = (255, 255, 255)
black = (0,0,0)
green = (0,255,0)
darkgreen = (220, 255, 10)
blue = (0,0,255)
red = (255,0,0)
gold = (255, 223, 0)    #212, 175, 55
silver = (192, 192, 192)
highscore = 0
game_start = False
sizeconfirm = False
speedconfirm = False
small = False
medium = False
large = False
slow = False
mediumspeed = False
fast = False

#put text on the screen
font_style = pygame.font.SysFont(None, 50)
def message(msg, color, msgx, msgy):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [msgx, msgy])


#start screen
while not game_start:
    window = pygame.display.set_mode((400, 350))
    message("Choose snake size:", blue, 0, 0)
    pygame.draw.rect(window, (0, 200, 250), [10, 60, 100, 40])
    if small == True:
        message("small", green, 10, 60)
    else:
        message("small", white, 10, 60)
    
    pygame.draw.rect(window, (0, 200, 250), [120, 60, 140, 40])
    if medium == True:
        message("medium", green, 120, 60)
    else:
        message("medium", white, 120, 60)
    
    pygame.draw.rect(window, (0, 200, 250), [270, 60, 100, 40])
    if large == True:
        message("large", green, 280, 60)
    else:
        message("large", white, 280, 60)
    
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 10 <= mouse[0] <= 110 and 60 <= mouse[1] <= 100:
                blocklength = 10
                sizeconfirm = True
                small = True
                medium = False
                large = False
            elif 120 <= mouse[0] <= 240 and 60 <= mouse[1] <= 100:
                blocklength = 20
                sizeconfirm = True
                small = False
                medium = True
                large = False
            elif 270 <= mouse[0] <= 370 and 60 <= mouse[1] <= 100:
                blocklength = 30
                sizeconfirm = True
                small = False
                medium = False
                large = True

            if 10 <= mouse[0] <= 110 and 200 <= mouse[1] <= 240:
                snake_speed = 10
                speedconfirm = True
                slow = True
                mediumspeed = False
                fast = False
            elif 120 <= mouse[0] <= 240 and 200 <= mouse[1] <= 240:
                snake_speed = 20
                speedconfirm = True
                slow = False
                mediumspeed = True
                fast = False
            elif 270 <= mouse[0] <= 370 and 200 <= mouse[1] <= 240:
                snake_speed = 30
                speedconfirm = True
                slow = False
                mediumspeed = False
                fast = True

    message("Choose snake speed:", blue, 0, 140)
    pygame.draw.rect(window, (0, 200, 250), [10, 200, 100, 40])
    if slow == True:
        message("slow", green, 20, 200)
    else:
        message("slow", white, 20, 200)
    
    pygame.draw.rect(window, (0, 200, 250), [120, 200, 140, 40])
    if mediumspeed == True:
        message("medium", green, 120, 200)
    else:
        message("medium", white, 120, 200)
    
    pygame.draw.rect(window, (0, 200, 250), [270, 200, 100, 40])
    if fast == True:
        message("fast", green, 280, 200)
    else:
        message("fast", white, 280, 200)


    if sizeconfirm == True and speedconfirm == True:
        game_start = True

    pygame.display.update()



#set up window
window_width = blocklength * 40
window_height = blocklength * 35
if window_width > 1400 or window_height > 1000:
    window_width = 1400
    window_height = 1000
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake game')





def gameLoop(highscore, snakes_peed):
    #define variables that are reset for each game
    score = 0
    game_over = False
    round_over = False
    x1 = window_width/2
    x1 = round(x1/blocklength) * blocklength
    
    y1 = (window_height-50)/2
    y1 = round(y1/blocklength) * blocklength

    snakecoords = [x1, y1]
    x1change = 0
    y1change = 0
    direction = ""  #in snake you cannot do a U-turn!
    newpos = True
    clock = pygame.time.Clock()



    #event loop
    while not game_over:

        if round_over == True:
            #game over: display stats
            window.fill(black)
            if score == 1:
                message("You scored {} point".format(score), blue, 0, 300)
            else:
                message("You scored {} points".format(score), blue, 0, 300)
            message("Game over", red, 100, 10)
            message("Press Q to quit or space", red, 0, 60)
            message("to play again", red, 0, 110)
            if score <= highscore:
                message("Your highscore is {}".format(highscore), silver, 0, 180)
            else:
                message("New highscore!", gold, 0, 180)
                highscore = score

            pygame.display.update()

            while not game_over:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            round_over = False
                        if event.key == pygame.K_SPACE:
                            gameLoop(highscore, snake_speed)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                #if not direction == "right":
                    x1change = -blocklength
                    y1change = 0
                    direction = "left"
                elif event.key == pygame.K_RIGHT:
                #if not direction == "left":
                    x1change = blocklength
                    y1change = 0
                    direction = "right"
                elif event.key == pygame.K_UP:
                #if not direction == "down":
                    x1change = 0
                    y1change = -blocklength
                    direction = "up"
                elif event.key == pygame.K_DOWN:
                #if not direction == "up":
                    x1change = 0
                    y1change = blocklength
                    direction = "down"
        #position apple
        if newpos == True:
            applex = random.randint(0, window_width - blocklength)
            applex = round(applex/blocklength) * blocklength
            appley = random.randint(0, window_height - (blocklength + 50))
            appley = round(appley/blocklength) * blocklength
            
            while applex in snakecoords and appley in snakecoords:
                applex = random.randint(0, window_width - blocklength)
                applex = round(applex/blocklength) * blocklength
                appley = random.randint(0, window_height - (blocklength + 50))
                appley = round(appley/blocklength) * blocklength
            
            newpos = False


            if direction == "left":
                snakecoords.append(x1 + blocklength)
                snakecoords.append(y1)
            elif direction == "right":
                snakecoords.append(x1 - blocklength)
                snakecoords.append(y1)
            elif direction == "up":
                snakecoords.append(x1)
                snakecoords.append(y1 + blocklength)
            elif direction == "down":
                snakecoords.append(x1)
                snakecoords.append(y1 - blocklength)

        #update positions
        x1 += x1change
        y1 += y1change

        if score >= 1:
            for i in range(0, len(snakecoords), 2):
                if snakecoords[i] == x1:
                    if snakecoords[i + 1] == y1:
                        round_over = True

        #update positions list to move snake
        snakecoords.remove(snakecoords[0])
        snakecoords.remove(snakecoords[0])
        snakecoords.append(x1)
        snakecoords.append(y1)

        window.fill(black)

        #check if snake is outside of game area
        if x1 >= window_width or x1 < 0 or y1 >= (window_height-50) or y1 < 0: 
            round_over = True
        
        if x1 == applex and y1 == appley:
            newpos = True
            score += 1
            #display a message saying "yum" somehow - it isn't working :()

        pygame.draw.rect(window, (255,0,0), [applex, appley, blocklength, blocklength])
        number = 0
        for itemno in range(0,len(snakecoords)):
            if not itemno%2 == 1:
                if number%4 == 0:
                    pygame.draw.rect(window, green, [snakecoords[number],snakecoords[number+1],blocklength,blocklength])
                else:
                    pygame.draw.rect(window, darkgreen, [snakecoords[number],snakecoords[number+1],blocklength,blocklength])
                number += 2

        #display score
        pygame.draw.rect(window, (255,255,255,), [0, window_height - 50, window_width, 50])
        message("Score: {}".format(score), blue, 0, window_height - 50)

        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop(highscore, snake_speed)