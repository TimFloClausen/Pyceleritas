import pygame
import math

pygame.init()


DELAY = 10000 # Time in milliseconds between frames
WIN_SIZE_W = 1400  # Window size (width) in pixels
WIN_SIZE_H = 700  # Window size (height) in pixels
X = 400
Y = 400
angle = 0

fullscreen = False
fullscreen_check = 1
mooniter_size = [pygame.display.Info().current_w,pygame.display.Info().current_h,]
screen = pygame.display.set_mode((WIN_SIZE_W, WIN_SIZE_H))



pygame.display.set_caption("Pyceleritas")

def fullscreen_on_of(screen, fullscreen, mooniter_size, fullscreen_check):
    keys = pygame.key.get_pressed()
        
        
    if keys[pygame.K_k]:
        if fullscreen_check == 1:
            screen = pygame.display.set_mode((mooniter_size), pygame.FULLSCREEN)
            fullscreen_check = 2
            return screen, fullscreen, fullscreen_check
        elif fullscreen_check == 2: 
            screen = pygame.display.set_mode((WIN_SIZE_W, WIN_SIZE_H))
            fullscreen_check = 1
            return screen, fullscreen, fullscreen_check
    else:
        return screen, fullscreen, fullscreen_check
    
            

            


        

    
def car(X, Y,):
    car_img = pygame.image.load("assets/car/placeholder_car.png").convert_alpha()
    screen.blit(car_img, (X, Y))
    
    






run = True
while run:
    screen.fill((250, 250, 250))
    screen, fullscreen, fullscreen_check = fullscreen_on_of(screen, fullscreen, mooniter_size, fullscreen_check)
    keys = pygame.key.get_pressed()
    
    
    
    
    car(X, Y)

    if keys[pygame.K_w]:
        X += 0.5
    elif keys[pygame.K_s]:
            X -= 0.5
    
  
    

    

    

    
    


         
    
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False