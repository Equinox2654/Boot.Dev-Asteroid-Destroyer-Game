import pygame
import sys

from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

from logger import log_state
from logger import log_event

from constants import SCREEN_WIDTH, SCREEN_HEIGHT 

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)
    
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)    
    asteroidfield = AsteroidField()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill("black")

        updatable.update(dt)
        for draw_obj in drawable:
            draw_obj.draw(screen)
        for a in asteroids:
            if a.collides_with(player):
                log_event("player_hit")
                print("Game Over!")
                running = False
            for s in shots:
                if s.collides_with(a):
                    s.kill()
                    a.split()
                    log_event("asteroid_shot")

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        log_state()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
