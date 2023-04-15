import pygame,sys

# Initialize pygame
pygame.init()

# Set up the window
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Drag Rectangle")

# Set up the colors
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)

# Set up the font
font = pygame.font.SysFont('Arial', 32)

class DraggableRectangle:
    def __init__(self, x, y, width, height, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x,self.y, self.width, self.height)
        self.text = font.render(text, True, WHITE)
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
        
class DropZone:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = font.render(text, True, WHITE)
    
    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect, 2)
        screen.blit(self.text, (self.rect.x+self.rect.width/2-self.text.get_width()/2, self.rect.y+self.rect.height/2-self.text.get_height()/2))
        
    def contains(self, rect):
        return self.rect.collidepoint(rect.rect.center)
    
# Set up the rectangles
rect1 = DraggableRectangle(100, 100, 100, 50, "Drag me!")
rect2 = DropZone(400, 200, 100, 50, "Drop zone")

# Set up the clock
clock = pygame.time.Clock()

# Set up the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        else:
            rect1.handle_event(event)
            
    # Check if rect1 is inside rect2
    if rect2.contains(rect1):
        rect1.rect.center = rect2.rect.center
        rect1.status = True
    
    # Clear the screen
    screen.fill(GRAY)
    
    # Draw the rectangles
    rect2.draw(screen)
    rect1.draw(screen)
    
    # Update the display
    pygame.display.update()
    
    # Tick the clock
    clock.tick(60)
