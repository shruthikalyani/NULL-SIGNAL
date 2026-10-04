# main.py

import pygame
import sys
from settings import *
from game.player import Player
from game.room import Room

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(GAME_TITLE)
    clock = pygame.time.Clock()

    player = Player(screen.get_rect().center)
    room = Room()

    running = True
    while running:
        dt = clock.tick(FPS) / 1000  # Get delta time in seconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(DARK_BLUE)

        player.update(dt)
        room.update(dt)
        player.draw(screen)
        room.draw(screen, player)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
