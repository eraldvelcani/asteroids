import pygame
import sys
from constants import *
from player import Player
from asteroidfield import AsteroidField
from circleshape import CircleShape
from asteroid import Asteroid

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroidss = pygame.sprite.Group()
    
    Asteroid.containers = (asteroidss, drawable, updatable)
    AsteroidField.containers =  updatable
    asteroid_field = AsteroidField()
    
    Player.containers = (drawable, updatable)
    

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    
    dt = 0


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        
        updatable.update(dt)
        for asteroid in asteroidss:
            if collision_check(player):
                print("Game Over!")
                sys.exit()

        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

   
if __name__ == "__main__":
    main()
