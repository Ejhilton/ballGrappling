import pygame
import time

class Window:
    def __init__(self, width, height, fullscreen, title):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height), fullscreen)
        pygame.display.set_caption(title)

    def swapBuffers(self):
        pygame.display.flip()

    def clear(self):
        self.window.fill((0, 0, 0))

    def getDt(self):
        currentTime = time.time()
        dt = currentTime - self.previousTime
        self.previousTime = currentTime
        return dt
