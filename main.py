import pygame

from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT 

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        screen.fill("black")
        log_state()
        for event in pygame.event.get():
            if event == pygame.QUIT:
                return

        pygame.display.flip()


if __name__ == "__main__":
    main()
