import pygame
pygame.init()

# Colors
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)

# Game variables
quit_game=False
game_over=False
screen_width=500
screen_height=500
x_snake=200
y_snake=200
snake_size=20

window=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snake Game")
pygame.display.update()



# Game loop
while not quit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit_game=True

    window.fill(white)
    pygame.draw.rect(window,green,[x_snake,y_snake,snake_size,snake_size])
    pygame.display.update()

pygame.quit()
quit()

