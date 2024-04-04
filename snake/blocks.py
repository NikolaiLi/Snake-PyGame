import pygame
import random
from constants import *


class Blocks(pygame.sprite.Sprite):
    def __init__(self, screen, coords):
        super().__init__()
        self.screen = screen
        self.color = (232, 204, 125)
        self.image = pygame.Surface((300, 70))
        self.image.fill(self.color)
        
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = coords[0]-self.rect.width/2, coords[1]
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)    
