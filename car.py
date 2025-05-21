import pygame
import math
from config import CAR_WIDTH, CAR_HEIGHT, RED

class Car:
    def __init__(self, x, y):
        # Use floats for smooth position internally
        self.x = float(x)
        self.y = float(y)  # fixed vertical position
        self.fixed_y = y

        self.image = self.create_car_surface()
        self.rect = self.image.get_rect(center=(x, y))

        self.angle = 0.0  # store as float degrees
        self.speed = 0.0

        self.rotation_speed = 2.0
        self.acceleration = 0.2
        self.max_speed = 5.0
        self.friction = 0.05

    def create_car_surface(self):
        surface = pygame.Surface((CAR_WIDTH, CAR_HEIGHT), pygame.SRCALPHA)
        surface.fill((0, 0, 0, 0))
        pygame.draw.rect(surface, RED, (0, 0, CAR_WIDTH, CAR_HEIGHT))
        return surface

    def update(self, controls):
        # Accelerate or decelerate
        if controls.up:
            self.speed += self.acceleration
        elif controls.down:
            self.speed -= self.acceleration
        else:
            # Apply friction to gradually slow down
            if self.speed > 0:
                self.speed -= self.friction
                if self.speed < 0:
                    self.speed = 0
            elif self.speed < 0:
                self.speed += self.friction
                if self.speed > 0:
                    self.speed = 0

        # Clamp speed
        self.speed = max(-self.max_speed, min(self.max_speed, self.speed))

        # Rotate car
        if controls.left:
            self.angle += self.rotation_speed
        if controls.right:
            self.angle -= self.rotation_speed

        # Convert angle to radians for movement calculation
        rad = math.radians(self.angle)

        # this.x-=Math.sin(this.angle)*this.speed;
        # this.y-=Math.cos(this.angle)*this.speed;
        # Update position based on speed and angle
        self.x -= math.sin(rad)* self.speed
        # y stays fixed (horizontal road scroll), so y = fixed_y
        self.y = math.cos(rad) * self.speed 

        # Update rect center for rendering (rounded to int)
        self.rect.center = (int(self.x), int(self.y))

    def draw(self, screen):
        # Rotate the car image around its center by self.angle degrees
        rotated = pygame.transform.rotate(self.image, -self.angle)
        new_rect = rotated.get_rect(center=self.rect.center)
        screen.blit(rotated, new_rect.topleft)
