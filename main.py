# main.py

import pygame
import sys
from config import WIDTH, HEIGHT, WHITE
from car import Car
from road import Road
from controls import Controls
from sensor import Sensor

class CarGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Toy Car with Scrolling Road")
        self.clock = pygame.time.Clock()
        self.running = True

        self.controls = Controls()
        self.road = Road(WIDTH // 2, 200)
        self.car = Car(self.road.get_lane_center(1), HEIGHT // 2)
        self.sensors = Sensor(self.car)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.controls.update()
            self.car.update(self.controls)
            self.road.update(self.car.speed)
            self.sensors.update(self.road.borders)

            self.screen.fill(WHITE)
            self.road.draw(self.screen)
            self.car.draw(self.screen)
            self.sensors.draw(self.screen)  # <- ✅ Add this line

            pygame.display.flip()
            self.clock.tick(60)


        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    CarGame().run()