'''This is my first python project
   Title : Classic Snake Game
   Level : Beginner
   Author : Dinesh 
   mail id: india.dinesh09@gmail.com'''
import pygame
import random
pygame.init()

#game colors
white= (255,255,255)
red = (255,0,0)
green= (0,255,0)
blue =(0,0,255)
custom = (126,200,228)

#game window
screen_width= 800
screen_height=500
gamewindow = pygame.display.set_mode((screen_width,screen_height))

#game titles
pygame.display.set_caption("Snake game")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,55)

def plot_snake(gamewindow,color,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gamewindow, color, [x,y, snake_size, snake_size])


#To display something on screen
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])

#welcome window
def welcome():
    exit_game=False
    while not exit_game:
        gamewindow.fill(custom)
        text_screen("Welcome to Game",white,200,220)
        text_screen("Press spacebar to play", white, 180, 270)
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                quit()
                exit_game =True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
        pygame.display.update()
        clock.tick(60)



#game loop
def gameloop():
    # game vars
    exit_game = False
    game_over = False
    score = 0
    snake_x = 55
    snake_y = 55
    snake_size = 20
    food_size = 20
    velocity_x = 0
    velocity_y = 0
    fps = 30
    food_x = random.randint(0, screen_width / 2)
    food_y = random.randint(0, screen_height / 2)

    snake_list = []
    snake_length = 1
    #For highscore reading from database
    with open("highscore.txt", "r") as f:
        highscore = f.read()

    while not exit_game :
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            gamewindow.fill(custom)
            text_screen("Game Over!Press Spacebar For Home",red,50,250)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    exit_game = True

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    exit_game = True

                #It controls direction of snake
                if event.type == pygame.KEYDOWN:
                    if event.key== pygame.K_RIGHT:
                        velocity_x = 4
                        velocity_y = 0
                    if event.key== pygame.K_LEFT:
                        velocity_x = -10
                        velocity_y = 0
                    if event.key== pygame.K_UP:
                        velocity_y = -10
                        velocity_x = 0
                    if event.key== pygame.K_DOWN:
                        velocity_y = 10
                        velocity_x = 0
                    if event.key == pygame.K_c:
                        score+=10
            snake_x=snake_x + velocity_x
            snake_y = snake_y + velocity_y

            #When snake eats food.
            if abs(snake_x-food_x)<12 and abs(snake_y-food_y)<12:

                score+= 10
                food_x = random.randint(0, screen_width/2)
                food_y = random.randint(0, screen_height/2)
                snake_length+= 5

                #when new highscore achived
                if score > int(highscore):
                    highscore=score

            #To display score on game window
            gamewindow.fill(white)
            text_screen("score: " + str(score) + "  HighScore:" +str(highscore), red, 5, 5)

            pygame.draw.rect(gamewindow,green, [food_x,food_y, food_size, food_size])
            #It increases size of snake
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            #It controls snake length and corrects length.
            if len(snake_list)>snake_length:
                del snake_list[0]

            #When snake bites himself
            if head in snake_list[:-1]:
                game_over = True

            #when snake strike to borders
            if snake_x < 0 or snake_x>screen_width or snake_y <0 or snake_y>screen_height:
                game_over = True

            plot_snake(gamewindow,blue,snake_list,snake_size)
        pygame.display.update()
        clock.tick(fps)

welcome()
pygame.quit()
quit()
