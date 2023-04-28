import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, position: pygame.Vector2, image: pygame.Surface, *groups):
        super().__init__(*groups)
        self.position = position
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position