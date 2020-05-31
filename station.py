import pygame
import math

__station_counter = 0


def next_station_name():
    global __station_counter
    __station_counter += 1
    return "station%s" % __station_counter


class Station:

    def __init__(self, pos, r=20, color=(255, 0, 0)):
        self.name = next_station_name()
        self.pos = pos
        self.r = r
        self.color = color

    def draw_station(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, self.r)
        pygame.draw.circle(surface, (255, 255, 255), self.pos, self.r - 7)

    def change_pos(self, pos):
        self.pos = pos

    def get_pos(self):
        return self.pos

    def on_station(self, pos):
        if self.r >= math.sqrt((pos[0] - self.pos[0])**2 + (pos[1] - self.pos[1])**2):
            return True
        else:
            return False

    def draw_line_from_station(self, pos, surface):
        pygame.draw.line(surface, (0, 0, 0), self.pos, pos, 10)
        pygame.draw.line(surface, (255, 255, 255), self.pos, pos, 4)
