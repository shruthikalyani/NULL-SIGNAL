# game/player.py

import pygame
from settings import *

class Player:
    def __init__(self, position):
        self.rect = pygame.Rect(position, (50, 50))
        self.velocity = pygame.math.Vector2(0, 0)
        self.speed = 200

    def update(self, dt):
        keys = pygame.key.get_pressed()
        dx = 0
        dy = 0

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            dy -= 1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            dy += 1
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx -= 1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx += 1

        self.velocity.x = dx * self.speed * dt
        self.velocity.y = dy * self.speed * dt

        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        # Collision with walls
        self.rect.clamp_ip(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)
        pygame.draw.circle(screen, BLUE, (self.rect.centerx, 
self.rect.centery), 10)