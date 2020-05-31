import pygame

from station import Station


class Editor:
    def __init__(self, screen, world):
        self.move_mode = MoveEditorMode(world)
        self.line_mode = LineEditorMode(screen, world)
        self.create_mode = CreateEditorMode(world)

        self.mode = self.move_mode
        self.screen = screen
        self.world = world

        self.button_pressed = False
        self.time = 0

    def on_pressed(self, pressed):
        if pressed[pygame.K_m]:
            self.mode = self.move_mode
        elif pressed[pygame.K_l]:
            self.mode = self.line_mode
        elif pressed[pygame.K_c]:
            self.mode = self.create_mode


class EditorMode:
    def before(self):
        raise NotImplementedError()

    def on_left_pressed(self):
        raise NotImplementedError()

    def on_left_released(self):
        raise NotImplementedError()


class MoveEditorMode(EditorMode):

    def __init__(self, world):
        self.world = world
        self.current_object = None
        self.dragging = False

    def before(self):
        print("move editor")

    def on_left_pressed(self):
        obj = self.world.find_object(pygame.mouse.get_pos())
        if obj is not None and not self.dragging:
            print("found object, start dragging")
            self.dragging = True
            self.current_object = obj
        elif self.dragging:
            print("dragging")
            self.world.change_line_pos(pygame.mouse.get_pos(), self.current_object.get_pos())
            self.current_object.change_pos(pygame.mouse.get_pos())

    def on_left_released(self):
        print("waiting for command")
        self.dragging = False


class CreateEditorMode(EditorMode):
    counter = 0

    def __init__(self, world):
        self.world = world
        self.was_pressed = False

    def before(self):
        print("station editor mode on")

    def on_left_pressed(self):
        if not self.was_pressed:
            print("made new station")
            self.was_pressed = True
            self.world.stationList.append(Station(pygame.mouse.get_pos()))
            self.counter += 1
            print(self.counter)
            print(self.world.stationList[-1])
        else:
            print("moving station")
            self.world.stationList[self.counter - 1].change_pos(pygame.mouse.get_pos())

    def on_left_released(self):
        if self.was_pressed:
            print("placing station")
            self.world.stationList[self.counter - 1].change_pos(pygame.mouse.get_pos())
            self.was_pressed = False


class LineEditorMode(EditorMode):

    def __init__(self, screen, world):
        self.world = world
        self.screen = screen
        self.initial_obj = None
        self.drawing_line = False

    def before(self):
        print("line editor mod on")

    def on_left_pressed(self):
        obj = self.world.find_object(pygame.mouse.get_pos())
        if obj is not None and not self.drawing_line:
            print("on station")
            self.drawing_line = True
            self.initial_obj = obj
        elif self.drawing_line:
            print("drawing line")
            self.initial_obj.draw_line_from_station(pygame.mouse.get_pos(), self.screen)
            if obj is not None and self.initial_obj != obj:
                print("found second station")

    def on_left_released(self):
        obj = self.world.find_object(pygame.mouse.get_pos())
        if self.drawing_line and obj is not None and self.initial_obj != obj:
            print("connecting stations")
            self.world.connecting_station_line(
                self.initial_obj.get_pos(), obj.get_pos())
        else:
            print("none")
        self.drawing_line = False
