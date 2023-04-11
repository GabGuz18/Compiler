import pygame,sys
from DragBox import DragBox

#Colores constantes
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Definimos algunas constantes para el juego
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

# Creamos la ventana
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Nivel Uno")

#Fotogramas
clock = pygame.time.Clock()

# Creamos la caja que se arrastra
drag_box = DragBox(0, 700)
drag_box2 = DragBox(75, 700)
drag_box3 = DragBox(150, 700)

# Creamos un grupo de sprites para actualizar y dibujar
all_sprites = pygame.sprite.Group()
all_sprites.add(drag_box,drag_box2,drag_box3)


#Modulo del Nivel Uno   
def level_one(): 
    running = True
    print("level One")
    while running:
        screen.fill((0,0,0))


        #Manipulador eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                drag_box.handle_event(event)
                drag_box2.handle_event(event)
                drag_box3.handle_event(event)
            
        # Actualizamos los sprites
        all_sprites.update()

        # Dibujamos todo
        screen.fill(WHITE)
        all_sprites.draw(screen)

        # Actualizamos la pantalla
        pygame.display.flip()

        # Esperamos un poco para mantener el FPS
        clock.tick(FPS)
    pygame.quit()






