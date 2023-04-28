import pygame
import time
import os
from sys import exit
from iso_grid import Iso_Grid
from tile import Tile

WIDTH = 1200
HEIGHT = 800

def main():
    pygame.init()
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Platformer Test")
    clock = pygame.time.Clock()

    test_grid = Iso_Grid(32, 32, pygame.Vector2(WIDTH / 2, HEIGHT / 2))
    test_grid.create_map(10, 10, "assets/tile_01.png")

    last_time = time.time()

    while True:
        dt = time.time() - last_time
        last_time = time.time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False

        display.fill((255, 241, 232))

        test_grid.tiles.draw(display)

        pygame.display.update()


"""------------- Main -------------"""

if __name__ == "__main__":
    main()
    pygame.quit()
    exit()
