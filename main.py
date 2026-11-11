import pygame

pygame.init()


DELAY = 10000 # Time in milliseconds between frames
WIN_SIZE_W = 1400  # Window size (width) in pixels
WIN_SIZE_H = 700  # Window size (height) in pixels
X = 400
Y = 400

fullscreen = False
mooniter_size = [pygame.display.Info().current_w,pygame.display.Info().current_h,]
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
        
       
        
    
def car(X, Y):
    car_img = pygame.image.load("assets/car/placeholder_car.png")
    screen.blit(car_img, (X, Y))


run = True
while run:
    screen.fill((200, 200, 200))
    screen, fullscreen = fullscreen_on_of(screen, fullscreen, mooniter_size)
    keys = pygame.key.get_pressed()
    
    
    car(X, Y)

    if keys[pygame.K_w]:
        X += 1
    elif keys[pygame.K_s]:
        X -= 1

    

    
    


         
    
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False