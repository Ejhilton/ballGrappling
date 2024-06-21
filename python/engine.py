import pygame
import time
import math



class Window:
    def __init__(self, width, height, fullscreen, title):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height), fullscreen)
        pygame.display.set_caption(title)
        self.previousTime = time.time()
        self.rect = pygame.Rect(0, 0, width, height)

    def swapBuffers(self):
        pygame.display.flip()

    def clear(self):
        self.window.fill((0, 0, 0))

    def getDt(self):
        currentTime = time.time()
        dt = currentTime - self.previousTime
        self.previousTime = currentTime
        return dt


class Player:
    def __init__(self,window, pos, velocity, radius, color):
        self.window = window
        self.windowSurface = window.window
        self.pos = pos
        self.lastPos = pos
        self.velocity = velocity
        self.angle = 0
        self.radius = radius
        self.playerSpeed = 100
        self.color = color
        self.turnLeft = False
        self.turnRight = False
        self.moveForward = False
        self.moveBackward = False
        self.turnSpeed = 0.35
        self.turnSharp = False
        self.maxSpeed = 1000
        # self.gravity = pygame.math.Vector2(0, 0.98)

        # image info
        self.image = pygame.image.load("../images/simple-travel-car-top_view.png")
        self.image = pygame.transform.scale(self.image, (180, 100))
        self.rotateImage = self.image

    def update(self, dt):
        self.rotateImage = self.image

        # self.velocity += self.gravity
        if self.turnRight:
            if self.turnSharp:
                self.angle += self.turnSpeed * 1.5
            else:
                self.angle += self.turnSpeed

        if self.turnLeft:
            if self.turnSharp:
                self.angle += -self.turnSpeed * 1.5
            else:
                self.angle += -self.turnSpeed

        if self.moveForward and self.velocity.length() < self.maxSpeed:
            self.velocity += self.calculate_normalized_direction(self.angle) * 3

        if self.moveBackward and self.velocity.length() < self.maxSpeed:
            self.velocity += -(self.calculate_normalized_direction(self.angle) * 2)

        self.velocity *= 0.997
        self.pos += self.velocity * dt
        self.lastPos = self.pos

        self.rotateImage = pygame.transform.rotate(self.rotateImage, -self.angle)

    def isOffscreen(self, window):
        if self.pos.x < 0:
            self.pos.x = 0
            return "left"
        elif self.pos.x > window.width:
            self.pos.x = window.width
            return "right"
        elif self.pos.y < 0:
            self.pos.y = 0
            return "top"
        elif self.pos.y > window.height:
            self.pos.y = window.height
            return "bottom"
        else:
            return None


    def bounce(self, normal):
        dotProduct = self.velocity.dot(normal)
        print(2 * dotProduct * normal)
        self.velocity -= 2 * dotProduct * normal


    @staticmethod
    def calculate_endpoint(start_x, start_y, angle_degrees, distance):
        angle_radians = math.radians(angle_degrees)
        end_x = start_x + distance * math.cos(angle_radians)
        end_y = start_y + distance * math.sin(angle_radians)
        return end_x, end_y

    @staticmethod
    def calculate_normalized_direction(angle_degrees):
        # Convert angle to radians
        angle_radians = math.radians(angle_degrees)

        # Calculate direction components
        direction_x = math.cos(angle_radians)
        direction_y = math.sin(angle_radians)

        # Create the direction vector
        direction_vector = (direction_x, direction_y)

        # Calculate the magnitude of the vector
        magnitude = math.sqrt(direction_x**2 + direction_y**2)

        # Normalize the vector
        normalized_direction = (direction_x / magnitude, direction_y / magnitude)

        return pygame.math.Vector2(normalized_direction)


    def draw(self):
        # rotate image in the center of it
        player_rectangle = self.rotateImage.get_rect(center=(self.pos.x,self.pos.y))
        pygame.draw.circle(self.windowSurface, self.color, (self.pos.x, self.pos.y), self.radius)
        player_centre = (self.pos.x, self.pos.y)
        player_outerPoint = self.calculate_endpoint(self.pos.x, self.pos.y, self.angle, 50)
        pygame.draw.line(self.windowSurface, "Red", player_centre, player_outerPoint, 10)
        self.windowSurface.blit(self.rotateImage, player_rectangle.topleft)
