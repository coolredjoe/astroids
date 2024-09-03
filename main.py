import pygame
import player
from constants import *

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    main_player = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        main_player.update(dt)
        pygame.Surface.fill(screen, (0, 0, 0))
        main_player.draw(screen)
        pygame.display.flip()

        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()
