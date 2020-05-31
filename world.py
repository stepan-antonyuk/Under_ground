import pygame


class World:

    def __init__(self, lineList, stationList):
        self.lineList = lineList
        self.stationList = stationList

    def connecting_station_line(self, pos1, pos2):
        for line in self.lineList:
            if line[0] == pos1 and line[1] == pos2:
                print("already exist")
                return None
        print("add new line")
        self.lineList.append([pos1, pos2])

    def draw_lines(self, surface):
        for line in self.lineList:
            try:
                pygame.draw.line(surface, (0, 0, 0), line[0], line[1], 10)
                pygame.draw.line(surface, (255, 255, 255), line[0], line[1], 4)
            except TypeError as e:
                print(line)
                raise e

    def change_line_pos(self, pos, stationPos):
        counter = 0
        for linePos in self.lineList:
            if linePos[0] == stationPos:
                self.lineList[counter][0] = pos
            elif linePos[1] == stationPos:
                self.lineList[counter][1] = pos
            counter += 1

    def find_object(self, pos):
        for station in self.stationList:
            if station.on_station(pos):
                return station
        return None
