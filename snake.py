import pygame
import random

pygame.init()

# Game variables
white = (84, 62, 62)
black = (0, 0, 0)
cyan = (0, 226, 255)    #snake color 1
red = (255, 0, 0)       # food color
cyan2 = (0,255,129)     # snake color 2
white2 = (255,255,255)
border_color = (25,185,105)

########### rainbow snake color ######## color matches with documentation
r1 = (1,162,255)
r2 = (115,253,233)
r3 = (136,250,78)
r4 = (251,226,50)
r5 = (255,100,78)
###########

# screen size
x = 600
y = 600






# size of cube on screen
block_size = 30
score = [0]

# global variable


# Window and title display
display_window = pygame.display.set_mode((x, y))
pygame.display.set_caption("Snake Game")
font = pygame.font.Font("myfont.ttf", 50)
text_font = pygame.font.Font("myfont.ttf",25)
pygame.display.update()
refresh_rate = pygame.time.Clock()
########################

def draw_eyes(snake_coordinates):
    x = snake_coordinates[-1][0]
    y = snake_coordinates[-1][1]
    pygame.draw.circle(display_window,black,(x+10,y+10),3,3)
    pygame.draw.circle(display_window,black,(x+20,y+10),3,3)
    pygame.draw.circle(display_window, white2, (x + 10, y + 10), 1, 1)
    pygame.draw.circle(display_window, white2, (x + 20, y + 10), 1, 1)

##########################

# draw grid
# black background , white lines and white border

def grid(w, rows, surface):
    sizeBtn = w // rows
    i = 0
    j = 60
    for k in range(rows):
        i += sizeBtn
        j += sizeBtn
        # draws lines for grid
        pygame.draw.line(surface, white, (i, 90), (i, w))
        pygame.draw.line(surface, white, (0, j), (w, j))
    pygame.draw.line(surface, white, (570, 90), (570, 90))
    pygame.draw.line(surface, white, (0, 570), (w, 570))
    # draws lines for border



    pygame.draw.rect(surface, border_color, [0, 0, 5, 600])
    pygame.draw.rect(surface, border_color, [0, 0, 600, 30])
    pygame.draw.rect(surface, border_color, [0,595 ,600, 5])
    pygame.draw.rect(surface, border_color, [595 ,0, 5, 600])
    pygame.draw.rect(surface, border_color, [0, 90, 600, 5])

    """pygame.draw.line(surface, white, (0.5, 0.5), (w - 0.5, 0.5))
    pygame.draw.line(surface, white, (0.5, 0.5), (0.5, w - 0.5))
    pygame.draw.line(surface, white, (w - 0.5, 0.5), (w - 0.5, w - 0.5))
    pygame.draw.line(surface, white, (0, w - 0.5), (w - 0.5, w - 0.5))
    pygame.draw.line(surface, white, (1.5, 1.5), (w - 1.5, 1.5))
    pygame.draw.line(surface, white, (1.5, 1.5), (1.5, w - 1.5))
    pygame.draw.line(surface, white, (w - 1.5, 1.5), (w - 1.5, w - 1.5))
    pygame.draw.line(surface, white, (0, w - 1.5), (w - 1.5, w - 1.5))"""






##############################
def show_text(text):
    screen_text = text_font.render(text,True,red,None)
    display_window.blit(screen_text,[300,300])

def show_score(score):
    screen_text = font.render("SCORE : " + str(score[0]),True,white2,None)
    display_window.blit(screen_text,[200,40])

#############################

def get_food_coordinate(food_coordinates):
    food_coordinates[0] = random.randrange(2, 19) * 30 + 5
    food_coordinates[1] = random.randrange(6, 19) * 30 + 5


##############################
# change the function name
def check_eaten(food_coordinates, snake_coordinates, snake_length):
    x1 = food_coordinates[0]
    y1 = food_coordinates[1]
    x2 = snake_coordinates[-1][0]
    y2 = snake_coordinates[-1][1]
    if (abs(x1 - x2) < 10 and abs(y1 - y2) < 10):
        snake_length[0] += 1
        score[0] += 1
        get_food_coordinate(food_coordinates)
#############################

def check_hit(snake_coordinates,display_window):
    x1 = snake_coordinates[-1][0]
    y1 = snake_coordinates[-1][1]
    if( (0>=x1 or x1>=570) or (90>=y1 or y1>=570)):
        draw_dead_snake(snake_coordinates,display_window)
        return 0
    else:
        return 1

#############################

def check_touch(snake_coordinates,display):
    head = snake_coordinates[-1]
    snake_body = snake_coordinates[:]
    snake_body.remove(head)
    if(head in snake_body):
        draw_dead_snake(snake_coordinates, display)
        return 0
    else:
        return 1


#############################

def draw_dead_snake(list_coor,display):
    #draw_eyes(snake_coordinates)
    #x1,y1 = list_coor[0]
    #pygame.draw.rect(display,white2,[x1,y1,30,30])
    for x,y in list_coor:
        pygame.draw.rect(display,white2,[x,y,30,30])

def pause_game():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    return


##############################

class food:

    def draw_food(self, food_coordinates, snake_coordinates):
        for i,j in snake_coordinates:
            if(abs(food_coordinates[0]-i)<10 and abs(food_coordinates[1]-j)<10):
                get_food_coordinate(food_coordinates)
        pygame.draw.rect(display_window, red, [food_coordinates[0], food_coordinates[1], 20, 20])
    # image = pygame.image.load("food.png")
    # display_window.blit(image,(x,y))
    # food is eaten


class snake:

    def draw_snake(self, list_coor, display):  # here list is for coordinates of body
        c = 1
        for x, y in list_coor:

            #### rainbow snake implemantation ####

            if (c == 1):
                color = r1
                c = 2

            elif(c==2):
                color = r2
                c = 3

            elif(c==3):
                color = r3
                c = 4

            elif(c==4):
                color = r4
                c = 5

            elif(c==5):
                color = r5
                c = 1

            pygame.draw.rect(display, color , [x, y, 30, 30])


                #### gradient color implementation ###
            #R,B,G = (0, 226, 255)
            #color = (R+(c*10),B,G)
            #pygame.draw.rect(display, color , [x, y, 30, 30])
            #c += 1

                #### check type color implementation ###

    """        if(c==1):
               c = 0
               pygame.draw.rect(display, cyan, [x, y, 30, 30])
            else:
                c = 1
            pygame.draw.rect(display, cyan2 ,[x,y,30,30])    """

# Build body of snake
# def snake_body:
#   pygame.draw.rect(display_window,black,)
food = food()
snake = snake()
#########
"""def button(text,button_x,button_y,width,height,bc,ac,Act=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if button_x<mouse[0]<button_x+width and button_y<mouse[1]<button_y+height:
        pygame.draw.rect(display_window,ac,(button_x,button_y,width,height))
        message_display(text,40,button_x+width/2,button_y+height/2)
        if click[0]==1 and Act!=None:
            if Act=="go":
                countdown()
            elif Act=="exit":
                pygame.quit()
                quit()
            elif Act=="rules":"""
########### main ##############

def main():
    snake_x = 300
    snake_y = 300
    snake_coordinates = [[snake_x, snake_y]]
    eaten = 1

    snake_velocity_x = 0
    snake_velocity_y = 0
    snake_length = [1]
    velocity = 30
    food_coordinates = [245, 245]



    ##################

    quit_game = False
    while not quit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and snake_velocity_x == 0:
                    snake_velocity_x = velocity
                    snake_velocity_y = 0

                if event.key == pygame.K_LEFT and snake_velocity_x == 0:
                    snake_velocity_x = -velocity
                    snake_velocity_y = 0

                if event.key == pygame.K_DOWN and snake_velocity_y == 0:
                    snake_velocity_x = 0
                    snake_velocity_y = velocity

                if event.key == pygame.K_UP and snake_velocity_y == 0:
                    snake_velocity_x = 0
                    snake_velocity_y = -velocity

                if event.key == pygame.K_SPACE:
                    show_text("PAUSE")
                    pause_game()
        snake_x += snake_velocity_x
        snake_y += snake_velocity_y
        display_window.fill(black)

        show_score(score)

        check_eaten(food_coordinates, snake_coordinates, snake_length)
        food.draw_food(food_coordinates,snake_coordinates)

        status1 = check_hit(snake_coordinates,display_window)
        status2 = check_touch(snake_coordinates,display_window)

        grid(x, 20, display_window)
        temp_list = []
        temp_list.append(snake_x)
        temp_list.append(snake_y)



        if(status1==1 and status2==1):
            snake_coordinates.append(temp_list)
            if len(snake_coordinates) > snake_length[0]:
                del snake_coordinates[0]

            snake.draw_snake(snake_coordinates, display_window)
            draw_eyes(snake_coordinates)

        pygame.display.update()
        refresh_rate.tick(10)

    pygame.quit()
    quit()
main()
