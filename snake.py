import pygame
pygame.init()

#Game variables
white=(255,255,255)
black=(0,0,0)
x=600
y=600
block_size=10
quit_game=False

#Window and title display
display_window=pygame.display.set_mode((x,y))
pygame.display.set_caption("Snake Game")
pygame.display.update()

#draw grid
def grid(w,rows,surface):
    sizeBtn=w//rows
    i=0
    j=0
    for k in range(rows):
        i+=sizeBtn
        j+=sizeBtn

        pygame.draw.line(surface,white,(i,0),(i,w))
        pygame.draw.line(surface,white,(0,j),(w,j))
        pygame.draw.line(surface,white,(0,0),(w,0))
        pygame.draw.line(surface,white,(w,0),(w,w))
        pygame.draw.line(surface,white,(w,w),(0,w))
        pygame.draw.line(surface,white,(0,w),(0,0))

#Build body of snake
#def snake_body:
 #   pygame.draw.rect(display_window,black,)
while not quit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit_game=True

    grid(x,20,display_window)
    pygame.display.update()

pygame.quit()
quit()

