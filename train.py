
class Train:
    def __init__(self, pos, r=20, color=(255, 0, 0)):
        self.name = next_station_name()
        self.pos = pos
        self.r = r
        self.color = color