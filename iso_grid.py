import pygame
from tile import Tile

class Iso_Grid(object):
    def __init__(self, tilewidth: int, tileheight: int, offset: pygame.Vector2):
        self.tiles = pygame.sprite.Group()
        self.tilewidth = tilewidth
        self.tileheight = tileheight
        self.conversion = 1 / (
            (0.5 * tilewidth * 0.25 * tileheight)
            - (-0.5 * tilewidth * 0.25 * tileheight)
        )

        self.offset = offset

    def tile_to_screen(self, position: pygame.Vector2):
        return pygame.Vector2(
            (position.x - position.y) * (self.tilewidth * 0.5) - (self.tilewidth * .5),
            (position.x + position.y) * (self.tileheight * 0.25),
        )

    def scren_to_tile(self, tile: pygame.Vector2):
        return self.conversion * pygame.Vector2(
            (tile.x - tile.y) * (0.25 * self.tileheight),
            (tile.x + tile.y) * (0.5 * self.tilewidth),
        )

    def create_map(self, width: int, height: int, image: str):
        tile_img = pygame.image.load(image)
        tile_img.set_colorkey((0, 0, 0))
        for y in range(height):
            for x in range(width):
                self.tiles.add(
                    Tile(
                        self.tile_to_screen(pygame.Vector2(x, y)) + self.offset,
                        tile_img
                    )
                )
