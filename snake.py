import pygame
import random


pygame.init()

#Game variables
white=(255,255,255)
black=(0,0,0)
cyan = (0,226,255)

#screen size
x=600
y=600

#size of cube on screen
block_size=30

#global variable
eaten =  1
snake_coordinates = [[300,300]]
refresh_rate = pygame.time.Clock()
snake_velocity_x = 0
snake_velocity_y = 0
velocity = 30
food_coordinates= [245,245]


##################

quit_game=False

#Window and title display
display_window=pygame.display.set_mode((x,y))
pygame.display.set_caption("Snake Game")
pygame.display.update()

##########################

#draw grid
#black background , white lines and white border

def grid(w,rows,surface):
    sizeBtn=w//rows
    i=0
    j=0
    for k in range(rows):
        i+=sizeBtn
        j+=sizeBtn
#draws lines for grid
        pygame.draw.line(surface,white,(i,0),(i,w))
        pygame.draw.line(surface,white,(0,j),(w,j))
        pygame.draw.line(surface,white,(0,0),(w,0))
        pygame.draw.line(surface,white,(w,0),(w,w))
#draws lines for border
    pygame.draw.line(surface,white,(0.5,0.5),(w-0.5,0.5))
    pygame.draw.line(surface,white,(0.5,0.5),(0.5,w-0.5))
    pygame.draw.line(surface, white, (w-0.5,0.5), (w-0.5,w-0.5))
    pygame.draw.line(surface, white, (0,w-0.5), (w-0.5,w-0.5))
    pygame.draw.line(surface, white, (1.5, 1.5), (w - 1.5, 1.5))
    pygame.draw.line(surface, white, (1.5, 1.5), (1.5, w - 1.5))
    pygame.draw.line(surface, white, (w - 1.5, 1.5), (w - 1.5, w - 1.5))
    pygame.draw.line(surface, white, (0, w - 1.5), (w - 1.5, w - 1.5))

##############################

def get_food_coordinate(food_coordinates) :
   food_coordinates[0] = random.randrange(1, 19) * 30 + 5
   food_coordinates[1] = random.randrange(1, 19) * 30 + 5

##############################
#change the function name
def check(food_coordinates,snake_coordinates):
    x1 = food_coordinates[0]
    y1 = food_coordinates[1]
    x2 = snake_coordinates[0][0]
    y2 = snake_coordinates[0][1]
    if( abs(x1-x2)<10 and abs(y1-y2)<10):
        get_food_coordinate(food_coordinates)


##############################


class food:

    def draw_food(self,x,y):

           image = pygame.image.load("food.png")
           display_window.blit(image,(x,y))
              # food is eaten



class snake:



    def draw_snake(self,list,display):   #here list is for coordinates of body
        snake_coordinates[0][0] += snake_velocity_x
        snake_coordinates[0][1] += snake_velocity_y
        for x,y in list:
            pygame.draw.rect(display,cyan,[x,y,30,30])




    #head



    #body






#Build body of snake
#def snake_body:
 #   pygame.draw.rect(display_window,black,)
food = food()
snake = snake()


########### main ##############


while not quit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit_game=True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake_velocity_x==0:
                snake_velocity_x = velocity
                snake_velocity_y = 0

            if event.key == pygame.K_LEFT and snake_velocity_x==0:
                snake_velocity_x = -velocity
                snake_velocity_y = 0

            if event.key == pygame.K_DOWN and snake_velocity_y==0:
                snake_velocity_x = 0
                snake_velocity_y = velocity

            if event.key == pygame.K_UP and snake_velocity_y==0:
                snake_velocity_x = 0
                snake_velocity_y = -velocity

    display_window.fill(black)

    grid(x,20,display_window)

    check(food_coordinates,snake_coordinates)
    print(food_coordinates)

    food.draw_food(food_coordinates[0],food_coordinates[1])

    snake.draw_snake(snake_coordinates, display_window)




    pygame.display.update()



    refresh_rate.tick(7)

pygame.quit()
quit()
