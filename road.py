# road.py

import pygame
import math
from config import HEIGHT, GRAY, WHITE
from utils import lerp

class Road:
    def __init__(self, x, width, lane_count=3):
        self.x = x
        self.width = width
        self.lane_count = lane_count

        self.left = x - width / 2
        self.right = x + width / 2

        infinity = 1000000
        self.top = -infinity
        self.bottom = infinity

        top_left = (self.left, self.top)
        top_right = (self.right, self.top)
        bottom_left = (self.left, self.bottom)
        bottom_right = (self.right, self.bottom)

        self.borders = [
            [top_left, bottom_left],
            [top_right, bottom_right]
        ]

        self.offset = 0  # for vertical dashed scrolling

    def get_lane_center(self, lane_index):
        lane_width = self.width / self.lane_count
        return self.left + lane_width / 2 + min(lane_index, self.lane_count - 1) * lane_width

    def update(self, speed):
        self.offset -= speed  # simulate forward motion
        self.offset %= 40     # keep dashed lines looping

    def draw(self, screen):
        # Fill road background
        pygame.draw.rect(screen, GRAY, (self.left, 0, self.width, screen.get_height()))

        # Draw lane lines
        for i in range(1, self.lane_count):
            x = lerp(self.left, self.right, i / self.lane_count)
            y = -self.offset
            while y < screen.get_height():
                pygame.draw.line(screen, WHITE, (x, y), (x, y + 20), 2)
                y += 40

        # Draw road borders
        for border in self.borders:
            pygame.draw.line(screen, WHITE, border[0], border[1], 5)