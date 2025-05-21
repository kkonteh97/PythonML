import math
from utils import get_intersection, lerp
import pygame


class Sensor:
    def __init__(self, car, ray_count=3, ray_length=150, ray_spread=math.pi / 2):
        self.car = car
        self.ray_count = ray_count
        self.ray_length = ray_length
        self.ray_spread = ray_spread

        self.rays = []
        self.readings = []

    def update(self, road_borders):
        self._cast_rays()
        self.readings = []

        for ray in self.rays:
            reading = self._get_reading(ray, road_borders)
            self.readings.append(reading)

    def _get_reading(self, ray, road_borders):
        touches = []

        for border in road_borders:
            touch = get_intersection(ray[0], ray[1], border[0], border[1])
            if touch:
                touches.append(touch)

        if not touches:
            return None

        offsets = [t["offset"] for t in touches]
        min_offset = min(offsets)
        return next(t for t in touches if t["offset"] == min_offset)

    def _cast_rays(self):
        self.rays = []
        cx, cy = self.car.rect.center
        car_angle_rad = math.radians(self.car.angle)  # Convert degrees to radians

        for i in range(self.ray_count):
            ratio = i / (self.ray_count - 1) if self.ray_count > 1 else 0.5
            ray_angle = lerp(self.ray_spread / 2, -self.ray_spread / 2, ratio) + math.radians(self.car.angle)

            start = (cx, cy)
            end = (
                cx - math.sin(ray_angle) * self.ray_length,
                cy - math.cos(ray_angle) * self.ray_length
            )
            self.rays.append((start, end))


    def draw(self, screen):
        for i in range(self.ray_count):
            start = self.rays[i][0]
            if self.readings[i] is not None:
                end = (self.readings[i]["x"], self.readings[i]["y"])
            else:
                end = self.rays[i][1]

            pygame.draw.aaline(screen, (255, 255, 0), (start[0], start[1]), (end[0], end[1]))

            if self.readings[i] is not None:
                pygame.draw.aaline(screen, (0, 0, 0), (end[0], end[1]), (self.rays[i][1][0], self.rays[i][1][1]))
