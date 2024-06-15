import pygame
import time

class Window:
    def __init__(self, width, height, fullscreen, title):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height), fullscreen)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(title)

    def swapBuffers(self):
        pygame.display.flip()

    def clear(self):
        self.window.fill((0, 0, 0))


class Player:
    def __init__(self,window, pos, velocity, radius, color):
        self.window = window
        self.windowSurface = window.window
        self.pos = pos
        self.velocity = velocity
        self.radius = radius
        self.color = color

    def update(self):
        self.pos += self.velocity
        self.prevPos = self.pos

    def draw(self):
        pygame.draw.circle(self.windowSurface, self.color, (self.pos.x, self.pos.y), self.radius)
