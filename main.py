import pygame
from player import Player
from astroids import Asteroid
from astroidfield import AsteroidField
from constants import *

def main():
    pygame.init
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()

    asteroids = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable

    asteroid_field = AsteroidField()
    main_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updateable:
            obj.update(dt)

        pygame.Surface.fill(screen, (0, 0, 0))

        for obj in drawable:
            obj.draw(screen)
        
        for asteroid in asteroids:
            if asteroid.collides_with(main_player):
                print("Game over!")
                return

        pygame.display.flip()

        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()
