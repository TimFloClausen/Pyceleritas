import pygame

pygame.init()


DELAY = 16 # Time in milliseconds between frames
WIN_SIZE_W = 700  # Window size (width) in pixels
WIN_SIZE_H = 900  # Window size (height) in pixels



window = pygame.display.set_mode((WIN_SIZE_W, WIN_SIZE_H))
pygame.display.set_caption("Pyceleritas")
       
        
        





run = True
while run:
    
   
    
    


         
    
    
    
    
    
         

    

                
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False