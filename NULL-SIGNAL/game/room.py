# game/room.py

import pygame
from settings import *

class Room:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.walls = [
            pygame.Rect(0, 0, SCREEN_WIDTH, 50),  # Top
            pygame.Rect(0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50),  # Bottom
            pygame.Rect(0, 0, 50, SCREEN_HEIGHT),  # Left
            pygame.Rect(SCREEN_WIDTH - 50, 0, 50, SCREEN_HEIGHT)  # Right
        ]

    def update(self, dt):
        pass

    def draw(self, screen, player):
        # Draw walls
        for wall in self.walls:
            pygame.draw.rect(screen, WHITE, wall)

        # Draw flashlight cone
        flashlight_rect = pygame.Rect(player.rect.center, 
(FLASHLIGHT_RADIUS * 2, FLASHLIGHT_RADIUS * 2))
        flashlight_mask = pygame.mask.from_threshold(flashlight_rect, 
pygame.Surface((FLASHLIGHT_RADIUS * 2, FLASHLIGHT_RADIUS * 2)), (255, 255, 
255), 1)
        player_mask = pygame.mask.from_surface(screen.subsurface(player.rect))

        offset = pygame.math.Vector2(player.rect.center) - pygame.math.Vector2(flashlight_rect.center)
        if flashlight_mask.overlap(player_mask, offset):
            pygame.draw.circle(screen, WHITE, player.rect.center, FLASHLIGHT_RADIUS, 0)
            pygame.draw.circle(screen, BLUE, player.rect.center, FLASHLIGHT_RADIUS, 1)