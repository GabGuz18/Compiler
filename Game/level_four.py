import pygame,sys
#create display window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def level_four(): 
    running = True
    while running:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        
        pygame.display.update()
      