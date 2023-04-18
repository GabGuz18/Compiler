import pygame,sys
#create display window
import pygame,sys
from DragBox import DraggableRectangle
from Dropzone import DropZone
import button
from compilador import Compilador
from level_five import level_five
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
drag_box = DraggableRectangle(85, 510,100,50,"Mientras","Mientras")
drag_box2 = DraggableRectangle(205, 510,100,50,"Beber","Beber")
drag_box3 = DraggableRectangle(85, 590,100,50,"5",5)
drag_box4 = DraggableRectangle(205, 590,100,50,"id","id")
Opciones = [drag_box,drag_box2,drag_box3,drag_box4]

#Creamos los Dropzone
rect1 = DropZone(513, 132, 100, 50, "")
rect2 = DropZone(580, 275, 100, 50, "")
Zonas = [rect1,rect2]

#Botones
start_img = pygame.image.load('Compiler/Game/Img/start_btn.png').convert_alpha()
start_button = button.Button(880,550 ,start_img, 0.8)

#Cracion de Ventana
layout_opc = pygame.image.load('Compiler/Game/Img/layout_opc.png').convert_alpha()
layout_ventana = pygame.image.load('Compiler/Game/Img/layout_ventana.png').convert_alpha()
background = pygame.image.load('Compiler/Game/Img/background.png').convert_alpha()
layout_reto = pygame.image.load('Compiler/Game/Img/layout_reto.png').convert_alpha()
level__txt = pygame.image.load('Compiler/Game/Img/Level_tree.png').convert_alpha()
comp = Compilador()

# Creamos un grupo de sprites para actualizar y dibujar
#all_sprites = pygame.sprite.Group()
#all_sprites.add(drag_box,drag_box2,drag_box3)
def Checar(Opciones,Zonas):
    #Checar el Dropzone si colisiona
    for Zona in Zonas:
        for Opcion in Opciones:
            if Zona.contains(Opcion):
                Opcion.rect.center = Zona.rect.center
                Opcion.status = True
                Zona.Opcion = Opcion.Opcion

def level_four(): 
    running = True
    print("level four")
    error = None
    while running:
        #Condicion de Nivel
        

        #Manipulador eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                drag_box.handle_event(event)
                drag_box2.handle_event(event)
                drag_box3.handle_event(event)
                drag_box4.handle_event(event)
            
        #Checar el Dropzone si colisiona
        Checar(Opciones,Zonas)
        #if rect2.contains(rect1):
        #    rect1.rect.center = rect2.rect.center
        #    rect1.status = True
        # Actualizamos los sprites
        #all_sprites.update()
        
        # Dibujamos todo
        screen.blit(background, [0,0])
        screen.blit(layout_opc,[40,480])
        screen.blit(layout_ventana,[40,40])
        screen.blit(layout_reto,[440,40])
        screen.blit(level__txt,[510,130])
        #all_sprites.draw(screen)
        rect1.draw(screen)
        rect2.draw(screen)

        drag_box.draw(screen)
        drag_box2.draw(screen)
        drag_box3.draw(screen)
        drag_box4.draw(screen)

        #Boton Compilar
        if rect1.Opcion != None:
            if start_button.draw(screen):
                #Creamos el compilador y reiniciamos
                opc = rect1.Opcion
                opc2 = rect2.Opcion
                print(opc)
                error = comp.ciclo(opc,opc2)
        
        if error == False:
            comp.Print_txt(screen)
        elif error == True:
            level_five()

        # Actualizamos la pantalla
        pygame.display.flip()
        
        # Esperamos un poco para mantener el FPS
        clock.tick(FPS)
    pygame.quit()
      
      
      