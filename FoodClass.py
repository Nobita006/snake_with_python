import pygame

WHITE = (255, 255, 255)

class Food(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Food image Setup
        self.image = pygame.Surface((12, 12)) # Make the food slightly smaller than the head/tail
        self.image.fill(WHITE) # Make the food white
        self.rect = self.image.get_rect() #set the rect to the image rect
        self.rect.centerx = x # Set the x to given x
        self.rect.centery = y # Set the y to given y

    def ate(self):
        self.kill() # Kill the current food
