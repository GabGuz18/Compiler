import pygame
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


#Clase DropZone
class DropZone:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = pygame.font.SysFont('Minecraft', 22).render(text, True, WHITE)
        self.Opcion = None
        self.image = pygame.image.load('Compiler/Game/Img/Dropzone2.png').convert_alpha()
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, (self.rect.x+self.rect.width/2-self.text.get_width()/2, self.rect.y+self.rect.height/2-self.text.get_height()/2))
        
    def contains(self, rect):
        return self.rect.collidepoint(rect.rect.center)