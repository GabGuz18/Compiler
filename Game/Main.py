import pygame
import button
from level_one import level_one
from level_two import level_two
from level_tree import level_tree
from level_four import level_four
from DragBox import DraggableRectangle

# Definimos algunas constantes para el juego
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

# Creamos la ventana
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#Nombre de la Ventana
pygame.display.set_caption("Menu")

#Imagenes iniciales
start_img = pygame.image.load('Compiler/Game/Img/start_btn.png').convert_alpha()
exit_img = pygame.image.load('Compiler/Game//Img/exit_btn.png').convert_alpha()

#Crear botones
start_button = button.Button(300, 300, start_img, 0.8)
exit_button = button.Button(650, 300, exit_img, 0.8)


#Loop del juego
run = True
while run:

	screen.fill((202, 228, 241))

    #Accion boton Start
	if start_button.draw(screen):
		#Nos envia al nivel Uno
		level_one()
	
    #Accion Boton Exit
	if exit_button.draw(screen):
		run = False

	#Manipulador eventos
	for event in pygame.event.get():
		#Salir del Juego
		if event.type == pygame.QUIT:
			run = False	

	pygame.display.update()
	

pygame.quit()