import pygame

BLUE = (0, 0, 255)

class Tail(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Tail piece setup
        self.image = pygame.Surface((15, 15)) # Make it the same size as the head
        self.image.fill(BLUE) # Make it blue
        self.rect = self.image.get_rect() # Set the rect to be the same as the image
        self.rect.centerx = x # Starting x position at given
        self.rect.centery = y # Starting y position at given

    def update(self, x, y, colorScale):
        self.rect.centerx = x # update the x based off given
        self.rect.centery = y # update the y based off given
        # Scale the color based on where in tail piece is
        self.image.fill((0, 0, 255 / ((colorScale * 0.1) + 1)))
