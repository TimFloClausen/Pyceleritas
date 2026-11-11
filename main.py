import pygame

pygame.init()


DELAY = 16 # Time in milliseconds between frames
WIN_SIZE_W = 700  # Window size (width) in pixels
WIN_SIZE_H = 900  # Window size (height) in pixels

fullscreen = False
mooniter_size = [pygame.display.Info().current_w,pygame.display.Info().current_h,]
screen = pygame.display.set_mode((WIN_SIZE_W, WIN_SIZE_H))





screen = pygame.display.set_mode((WIN_SIZE_W, WIN_SIZE_H))
pygame.display.set_caption("Pyceleritas")

def fullscreen_on_of(screen, fullscreen, mooniter_size):
    keys = pygame.key.get_pressed()         
        
    if keys[pygame.K_k]:
        fullscreen = not fullscreen
    if fullscreen:
        screen = pygame.display.set_mode((mooniter_size), pygame.FULLSCREEN)
        return screen, fullscreen
        
    else:
        screen = pygame.display.set_mode((WIN_SIZE_W, WIN_SIZE_H))
        return screen, fullscreen
        
       
        
        





run = True
while run:

    screen, fullscreen = fullscreen_on_of(screen, fullscreen, mooniter_size)
    
    
   
    
    


         
    
    
    
    
    
         

    


    
    
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False