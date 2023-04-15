import pygame,sys
#Colores constantes
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

pygame.font.init()

# Clase para la caja que se arrastra
class DraggableRectangle:
    def __init__(self, x, y, width, height, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x,self.y, self.width, self.height)
        self.text = pygame.font.SysFont('Arial', 22).render(text, True, WHITE)
        self.dragging = False
        self.status = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.status == True:
                    self.rect = pygame.Rect(self.x,self.y, self.width, self.height)
                    self.status = False
                else:
                    self.dragging = True

        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                self.rect.move_ip(event.rel)

    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.rect)
        screen.blit(self.text, (self.rect.x+self.rect.width/2-self.text.get_width()/2, self.rect.y+self.rect.height/2-self.text.get_height()/2))
