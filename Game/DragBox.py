import pygame
#Colores constantes
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# Clase para la caja que se arrastra
class DragBox(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((100, 50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dragging = False

    def update(self):
        if self.dragging:
            pos = pygame.mouse.get_pos()
            self.rect.x = pos[0] - 50
            self.rect.y = pos[1] - 25

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
