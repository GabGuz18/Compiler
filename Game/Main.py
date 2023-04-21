import pygame
import button
from level_one import level_one
from level_two import level_two
from level_tree import level_tree
from level_four import level_four
from level_five import level_five

#Niel 1: (1),id ,Diez,20
#Nivel 2: (id), 1 , Cinco, Si
#Nivel 3: (Si, Correr), 20, Mientras 
#Nivel 4: (Mientras, Beber), , 5 , id
#Nivel 5: (Mientras,Divertido), 5 , Si   

# Definimos algunas constantes para el juego
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

# Creamos la ventana
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#Nombre de la Ventana
pygame.display.set_caption("Menu")

#Imagenes iniciales
start_img = pygame.image.load('Game/Img/start_btn.png').convert_alpha()
exit_img = pygame.image.load('Game//Img/exit_btn.png').convert_alpha()

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